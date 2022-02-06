#
# check_snippets.py
#

from pathlib import Path
import sys
print(f"Python version: {sys.version}\n")

test_dir = Path(__file__).parent
project_dir = test_dir.parent
snippet_files = project_dir.rglob("*.py")

# do they compile?
total_files = 0
fail_snip_files = []
for snip_file in snippet_files:
    log_snip = str(snip_file.relative_to(project_dir))
    total_files += 1
    try:
        compile(snip_file.read_text(encoding="UTF-8"), str(snip_file), "exec")
    except Exception as exc:
        print(f"Failed to compile {log_snip}")
        print(exc)
        fail_snip_files.append((snip_file, str(exc)))
    else:
        print(f"Successfully compiled {log_snip}")

print()
if fail_snip_files:
    print(f"{len(fail_snip_files)} of {total_files} files failed to compile:")
    for snip_file, exc_msg in fail_snip_files:
        print(f"- {snip_file}\n    {exc_msg}\n")
else:
    print(f"All {total_files} .py files compiled")

sys.exit(0 if not fail_snip_files else 1)
