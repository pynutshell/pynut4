from enum import Flag
import stat


class Permission(Flag):
    EXEC_OTH = stat.S_IXOTH
    WRITE_OTH = stat.S_IWOTH
    READ_OTH = stat.S_IROTH
    EXEC_GRP = stat.S_IXGRP
    WRITE_GRP = stat.S_IWGRP
    READ_GRP = stat.S_IRGRP
    EXEC_USR = stat.S_IXUSR
    WRITE_USR = stat.S_IWUSR
    READ_USR = stat.S_IRUSR

    @classmethod
    def from_mode(cls, mode):
        return cls(mode & 0o777)


from pathlib import Path

cur_dir = Path.cwd()
dir_perm = Permission.from_mode(cur_dir.stat().st_mode)
if dir_perm & Permission.READ_OTH:
    print("directory is readable")

# raises TypeError
print(Permission.READ_USR > Permission.READ_OTH)
