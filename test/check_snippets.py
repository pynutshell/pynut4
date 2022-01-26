#
# check_snippets.py
#

from pathlib import Path

test_dir = Path(__file__).parent
project_dir = test_dir.parent
snippets = project_dir.rglob("*.py")

# do they compile?
total = 0
fail_snips = []
for snip in snippets:
    total += 1
    try:
        compile(snip.read_text(), str(snip), "exec")
    except Exception as exc:
        print(f"Failed to compile {snip}")
        print(exc)
        fail_snips.append((snip, str(exc)))
    else:
        print(f"Successfully compiled {snip}")

print()
if fail_snips:
    print(f"{len(fail_snips)} of {total} files failed to compile:")
    for snip, msg in fail_snips:
        print(f"- {snip}\n    {msg}")
else:
    print(f"All {total} .py files compiled")
