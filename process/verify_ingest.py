"""Local integrity, link targets and selected arithmetic checks; no model replication."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "extracted/remaining_verified_results.json").read_text(encoding="utf-8"))
checks = []

def check(name, actual, expected, tolerance):
    checks.append(dict(name=name, actual=actual, expected=expected,
                       tolerance=tolerance, passed=abs(actual-expected) <= tolerance))

p2, p4, p8, p9 = (data[k] for k in ("P02", "P04", "P08", "P09"))
check("P02 PD reduction approximate percent", (1-p2["property_damage"]["ADS"]/p2["property_damage"]["human"])*100, 76, .2)
check("P02 PD absolute frequency difference", 3.26-.78, 2.48, .00001)
check("P04 national vehicle rate", p4["national_all_vehicle_involvements"]/p4["national_million_vehicle_miles"], 3.29, .005)
check("P04 vehicles per crash approximate", p4["national_all_vehicle_involvements"]/p4["national_crashes"], 1.78, .005)
check("P04 SF to national ratio", 5.82/1.76, 3.31, .005)
check("P04 SF percent higher", (5.82/1.76-1)*100, 231, .5)
check("P04 nonfatal inverse reporting factor", 1/(1-p4["nonfatal_underreporting_fraction"]), 1.47, .005)
check("P08 hypothetical operation count", p8["vehicles"]*p8["operations_per_vehicle_hour"], p8["fleet_operations_per_hour"], 0)
check("P09 sample grouping", p9["responsible"]+p9["not_responsible"], p9["sample"], 0)
check("P09 unadjusted OR only", (78*251)/(43*210), p9["unadjusted_intense_OR"], .005)
check("P09 intense percent responsible", 78/453*100, 17, .5)
check("P09 intense percent not responsible", 43/502*100, 9, .5)

mds = sorted(ROOT.rglob("*.md"))
missing, link_count = [], 0
for f in mds:
    for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", f.read_text(encoding="utf-8-sig")):
        target = raw.strip().strip("<>")
        if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target) or target.startswith("#"):
            continue
        target = unquote(target.split("#")[0])
        if not target:
            continue
        link_count += 1
        if not (f.parent / target).exists():
            missing.append(dict(file=str(f.relative_to(ROOT)), target=raw))

pdf_results = []
for entry in json.loads((ROOT/"sources/download_manifest.json").read_text(encoding="utf-8-sig")):
    if entry.get("status") not in ("confirmed_core", "confirmed_supplementary"):
        continue
    path = ROOT / entry["path"]
    payload = path.read_bytes()
    pdf_results.append(dict(id=entry["id"], size_matches=len(payload)==entry["bytes"],
                            sha256_matches=hashlib.sha256(payload).hexdigest()==entry["sha256"],
                            pdf_header=payload.startswith(b"%PDF"), pages=len(PdfReader(path).pages)))

json_paths = sorted((ROOT/"sources").glob("*.json")) + sorted((ROOT/"extracted").glob("*verified_results.json"))
for path in json_paths:
    json.loads(path.read_text(encoding="utf-8-sig"))

visual = {"P02":[4,5], "P04":[8,9,22,25,29], "P05":[5,13,14], "P08":[2,3,6], "P09":[2,6,7]}
previews = [ROOT/f"extracted/previews/{key}_remaining_p{p}.png" for key,pages in visual.items() for p in pages]
report = dict(date_taipei="2026-11-21", markdown_files_scanned=len(mds), local_links_checked=link_count,
              missing_local_links=missing, retained_pdf_integrity=pdf_results, arithmetic_checks=checks,
              parsed_json_files=[str(p.relative_to(ROOT)) for p in json_paths],
              reviewed_visual_pages=visual, visual_preview_files_present=all(p.exists() for p in previews),
              excluded_pdfs_absent=not any((ROOT/"raw/papers").glob("P03*.pdf")) and not any((ROOT/"raw/papers").glob("P06*.pdf")),
              limits="Link targets only; no Markdown/Mermaid UI rendering, external URL availability, HTML/offline checks, or original statistical replication")
ok = not missing and all(c["passed"] for c in checks) and all(p["size_matches"] and p["sha256_matches"] and p["pdf_header"] for p in pdf_results) and report["visual_preview_files_present"] and report["excluded_pdfs_absent"]
report["checks_passed"] = ok
(ROOT/"process/remaining_checks_2026-11-21.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps(dict(checks_passed=ok, markdown_files=len(mds), local_links=link_count, missing=missing,
                     pdfs=len(pdf_results), arithmetic_checks=len(checks)), ensure_ascii=False))
raise SystemExit(0 if ok else 1)
