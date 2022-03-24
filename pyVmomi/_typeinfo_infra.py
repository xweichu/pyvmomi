# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******
from .VmomiSupport import CreateDataType, CreateManagedType
from .VmomiSupport import CreateEnumType
from .VmomiSupport import AddVersion, AddVersionParent
from .VmomiSupport import AddBreakingChangesInfo
from .VmomiSupport import F_LINK, F_LINKABLE
from .VmomiSupport import F_OPTIONAL, F_SECRET
from .VmomiSupport import newestVersions, ltsVersions
from .VmomiSupport import dottedVersions, oldestVersions

AddVersion("vmodl.version.version0", "", "", 0, "vim25")
AddVersion("vmodl.version.version1", "", "", 0, "vim25")
AddVersion("vmodl.version.version2", "", "", 0, "vim25")
AddVersion("vmodl.infra.version.version1", "infra", "1.0", 0, "vim25")
AddVersionParent("vmodl.version.version0", "vmodl.version.version0")
AddVersionParent("vmodl.version.version1", "vmodl.version.version0")
AddVersionParent("vmodl.version.version1", "vmodl.version.version1")
AddVersionParent("vmodl.version.version2", "vmodl.version.version0")
AddVersionParent("vmodl.version.version2", "vmodl.version.version1")
AddVersionParent("vmodl.version.version2", "vmodl.version.version2")
AddVersionParent("vmodl.infra.version.version1", "vmodl.version.version0")
AddVersionParent("vmodl.infra.version.version1", "vmodl.version.version1")
AddVersionParent("vmodl.infra.version.version1", "vmodl.version.version2")
AddVersionParent("vmodl.infra.version.version1", "vmodl.infra.version.version1")

newestVersions.Add("vmodl.infra.version.version1")
ltsVersions.Add("vmodl.infra.version.version1")
dottedVersions.Add("vmodl.infra.version.version1")
oldestVersions.Add("vmodl.infra.version.version1")

CreateManagedType("vmodl.infra.VmodlNs", "InfraVmodlNs", "vmodl.ManagedObject", "vmodl.infra.version.version1", None, [("selectCommonVersions", "SelectCommonVersions", "vmodl.infra.version.version1", (("versionList", "vmodl.infra.VmodlNs.VersionId[]", "vmodl.infra.version.version1", 0, None),), (F_OPTIONAL, "vmodl.infra.VmodlNs.SelectedVersions", "vmodl.infra.VmodlNs.SelectedVersions"), "System.Anonymous", None)])
CreateDataType("vmodl.infra.VmodlNs.VersionId", "InfraVmodlNsVersionId", "vmodl.DynamicData", "vmodl.infra.version.version1", [("ns", "string", "vmodl.infra.version.version1", 0), ("id", "string", "vmodl.infra.version.version1", 0)])
CreateDataType("vmodl.infra.VmodlNs.SelectedVersions", "InfraVmodlNsSelectedVersions", "vmodl.DynamicData", "vmodl.infra.version.version1", [("compositeVersionId", "vmodl.infra.VmodlNs.VersionId", "vmodl.infra.version.version1", 0), ("versionList", "vmodl.infra.VmodlNs.VersionId[]", "vmodl.infra.version.version1", 0)])
