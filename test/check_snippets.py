#
# check_snippets.py
#

from pathlib import Path
import sys

test_dir = Path(__file__).parent
project_dir = test_dir.parent
snippets = project_dir.rglob("*.py")

# do they compile?
total = 0
fail_snips = []
for snip in snippets:
    log_snip = str(snip.relative_to(project_dir))
    total += 1
    try:
        compile(snip.read_text(), str(snip), "exec")
    except Exception as exc:
        print(f"Failed to compile {log_snip}")
        print(exc)
        fail_snips.append((snip, str(exc)))
    else:
        print(f"Successfully compiled {log_snip}")

print()
if fail_snips:
    print(f"{len(fail_snips)} of {total} files failed to compile:")
    for snip, msg in fail_snips:
        print(f"- {snip}\n    {msg}")
else:
    print(f"All {total} .py files compiled")

sys.exit(0 if not fail_snips else 1)
