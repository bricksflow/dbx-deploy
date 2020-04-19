from pathlib import PurePosixPath
from dbxdeploy.git.CurrentBranchResolver import CurrentBranchResolver

class WorkspaceBaseDirFactory:

    def __init__(
        self,
        workspaceBaseDirTemplate: str,
        currentBranchResolver: CurrentBranchResolver,
    ):
        self.__workspaceBaseDirTemplate = workspaceBaseDirTemplate
        self.__currentBranchResolver = currentBranchResolver

    def create(self):
        currentGitBranch = self.__currentBranchResolver.resolve()

        return PurePosixPath(self.__workspaceBaseDirTemplate.replace('{currentBranch}', currentGitBranch))
