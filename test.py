import subprocess

p = subprocess.Popen(
    [
        "rg",
        "test.log",
        "-e", r"(?:Traceback \(most recent call last\):|File \".*\",\s+line\s+\d+,\s+in).*\n(?:.*\n)*?.*?\S*(?:Error|Exception|Interrupt)(?:\:.*)?$",
        "--json",
        "--multiline",
        "--debug",
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
stdout, stderr = p.communicate()
print("# === STDERR ===================")
print(stderr)
print("# ==============================")

import json
import io
with io.StringIO(stdout.decode("utf-8")) as fin:
    for line in fin:
        content = json.loads(line)
        if content["type"] != "match":
            continue
        print(json.dumps(content, indent=2))
        for submatch_idx, submatch in enumerate(content["data"]["submatches"]):
            print(f"""Match length: {len(content["data"]["lines"]["text"])}""")
            print(f"""Submatch start/end: {(submatch["start"], submatch["end"])}""")
            print(f"""Submatch length: {len(submatch["match"]["text"])}""")
            print(f"""Submatch start + length: {submatch["start"] + len(submatch["match"]["text"])}""")
