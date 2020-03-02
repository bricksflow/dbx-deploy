from dbxdeploy.notebook.NotebooksLocator import NotebooksLocator
from dbxdeploy.package.PackageMetadata import PackageMetadata
from dbxdeploy.notebook.NotebooksDeployer import NotebooksDeployer

class CurrentAndReleaseDeployer:

    def __init__(
        self,
        createReleases: bool,
        notebooksLocator: NotebooksLocator,
        notebooksDeployer: NotebooksDeployer,
    ):
        self.__createReleases = createReleases
        self.__notebooksLocator = notebooksLocator
        self.__notebooksDeployer = notebooksDeployer

    def deploy(self, packageMetadata: PackageMetadata):
        notebooks = self.__notebooksLocator.locate()

        if self.__createReleases:
            self.__notebooksDeployer.deployRelease(packageMetadata, notebooks)
            self.__notebooksDeployer.deployCurrent(packageMetadata, notebooks)
        else:
            self.__notebooksDeployer.deployRoot(packageMetadata, notebooks)
