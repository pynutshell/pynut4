import enum
import stat


class Permission(enum.Flag):
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
    def from_stat(cls, stat_result):
        return cls(stat_result.st_mode & 0o777)


from pathlib import Path

cur_dir = Path.cwd()
dir_perm = Permission.from_stat(cur_dir.stat())
if dir_perm & Permission.READ_OTH:
    print(f'{cur_dir} is readable by users outside the owner group')

# the following raises TypeError; Flag enums do not support order comparisons
print(Permission.READ_USR > Permission.READ_OTH)
