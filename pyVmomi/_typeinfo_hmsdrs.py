# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******
from .VmomiSupport import CreateDataType, CreateManagedType
from .VmomiSupport import CreateEnumType
from .VmomiSupport import AddVersion, AddVersionParent
from .VmomiSupport import AddBreakingChangesInfo
from .VmomiSupport import F_LINK, F_LINKABLE
from .VmomiSupport import F_OPTIONAL, F_SECRET
from .VmomiSupport import newestVersions, ltsVersions
from .VmomiSupport import dottedVersions, oldestVersions

AddVersion("vmodl.query.version.version4", "", "", 0, "vim25")
AddVersion("vmodl.query.version.version3", "", "", 0, "vim25")
AddVersion("vmodl.query.version.version2", "", "", 0, "vim25")
AddVersion("hmsdrs.version.version6", "hmsdrsrv", "6.0", 0, "hmsdrsrv")
AddVersion("vmodl.query.version.version1", "", "", 0, "vim25")
AddVersion("vim.version.version8", "vim25", "5.1", 0, "vim25")
AddVersion("vim.version.version9", "vim25", "5.5", 0, "vim25")
AddVersion("vim.version.version6", "vim25", "4.1", 0, "vim25")
AddVersion("vim.version.version7", "vim25", "5.0", 0, "vim25")
AddVersion("vim.version.version1", "vim2", "2.0", 0, "vim25")
AddVersion("vim.version.version4", "vim25", "2.5u2server", 0, "vim25")
AddVersion("vim.version.version5", "vim25", "4.0", 0, "vim25")
AddVersion("vim.version.version2", "vim25", "2.5", 0, "vim25")
AddVersion("vim.version.version3", "vim25", "2.5u2", 0, "vim25")
AddVersion("vmodl.version.version0", "", "", 0, "vim25")
AddVersion("vmodl.version.version1", "", "", 0, "vim25")
AddVersion("vmodl.version.version2", "", "", 0, "vim25")
AddVersion("vmodl.reflect.version.version1", "reflect", "1.0", 0, "reflect")
AddVersionParent("vmodl.query.version.version4", "vmodl.query.version.version4")
AddVersionParent("vmodl.query.version.version4", "vmodl.query.version.version3")
AddVersionParent("vmodl.query.version.version4", "vmodl.query.version.version2")
AddVersionParent("vmodl.query.version.version4", "vmodl.query.version.version1")
AddVersionParent("vmodl.query.version.version4", "vmodl.version.version0")
AddVersionParent("vmodl.query.version.version4", "vmodl.version.version1")
AddVersionParent("vmodl.query.version.version4", "vmodl.version.version2")
AddVersionParent("vmodl.query.version.version3", "vmodl.query.version.version3")
AddVersionParent("vmodl.query.version.version3", "vmodl.query.version.version2")
AddVersionParent("vmodl.query.version.version3", "vmodl.query.version.version1")
AddVersionParent("vmodl.query.version.version3", "vmodl.version.version0")
AddVersionParent("vmodl.query.version.version3", "vmodl.version.version1")
AddVersionParent("vmodl.query.version.version2", "vmodl.query.version.version2")
AddVersionParent("vmodl.query.version.version2", "vmodl.query.version.version1")
AddVersionParent("vmodl.query.version.version2", "vmodl.version.version0")
AddVersionParent("vmodl.query.version.version2", "vmodl.version.version1")
AddVersionParent("hmsdrs.version.version6", "vmodl.query.version.version4")
AddVersionParent("hmsdrs.version.version6", "vmodl.query.version.version3")
AddVersionParent("hmsdrs.version.version6", "vmodl.query.version.version2")
AddVersionParent("hmsdrs.version.version6", "hmsdrs.version.version6")
AddVersionParent("hmsdrs.version.version6", "vmodl.query.version.version1")
AddVersionParent("hmsdrs.version.version6", "vim.version.version8")
AddVersionParent("hmsdrs.version.version6", "vim.version.version9")
AddVersionParent("hmsdrs.version.version6", "vim.version.version6")
AddVersionParent("hmsdrs.version.version6", "vim.version.version7")
AddVersionParent("hmsdrs.version.version6", "vim.version.version1")
AddVersionParent("hmsdrs.version.version6", "vim.version.version4")
AddVersionParent("hmsdrs.version.version6", "vim.version.version5")
AddVersionParent("hmsdrs.version.version6", "vim.version.version2")
AddVersionParent("hmsdrs.version.version6", "vim.version.version3")
AddVersionParent("hmsdrs.version.version6", "vmodl.version.version0")
AddVersionParent("hmsdrs.version.version6", "vmodl.version.version1")
AddVersionParent("hmsdrs.version.version6", "vmodl.version.version2")
AddVersionParent("hmsdrs.version.version6", "vmodl.reflect.version.version1")
AddVersionParent("vmodl.query.version.version1", "vmodl.query.version.version1")
AddVersionParent("vmodl.query.version.version1", "vmodl.version.version0")
AddVersionParent("vim.version.version8", "vmodl.query.version.version4")
AddVersionParent("vim.version.version8", "vmodl.query.version.version3")
AddVersionParent("vim.version.version8", "vmodl.query.version.version2")
AddVersionParent("vim.version.version8", "vmodl.query.version.version1")
AddVersionParent("vim.version.version8", "vim.version.version8")
AddVersionParent("vim.version.version8", "vim.version.version6")
AddVersionParent("vim.version.version8", "vim.version.version7")
AddVersionParent("vim.version.version8", "vim.version.version1")
AddVersionParent("vim.version.version8", "vim.version.version4")
AddVersionParent("vim.version.version8", "vim.version.version5")
AddVersionParent("vim.version.version8", "vim.version.version2")
AddVersionParent("vim.version.version8", "vim.version.version3")
AddVersionParent("vim.version.version8", "vmodl.version.version0")
AddVersionParent("vim.version.version8", "vmodl.version.version1")
AddVersionParent("vim.version.version8", "vmodl.version.version2")
AddVersionParent("vim.version.version8", "vmodl.reflect.version.version1")
AddVersionParent("vim.version.version9", "vmodl.query.version.version4")
AddVersionParent("vim.version.version9", "vmodl.query.version.version3")
AddVersionParent("vim.version.version9", "vmodl.query.version.version2")
AddVersionParent("vim.version.version9", "vmodl.query.version.version1")
AddVersionParent("vim.version.version9", "vim.version.version8")
AddVersionParent("vim.version.version9", "vim.version.version9")
AddVersionParent("vim.version.version9", "vim.version.version6")
AddVersionParent("vim.version.version9", "vim.version.version7")
AddVersionParent("vim.version.version9", "vim.version.version1")
AddVersionParent("vim.version.version9", "vim.version.version4")
AddVersionParent("vim.version.version9", "vim.version.version5")
AddVersionParent("vim.version.version9", "vim.version.version2")
AddVersionParent("vim.version.version9", "vim.version.version3")
AddVersionParent("vim.version.version9", "vmodl.version.version0")
AddVersionParent("vim.version.version9", "vmodl.version.version1")
AddVersionParent("vim.version.version9", "vmodl.version.version2")
AddVersionParent("vim.version.version9", "vmodl.reflect.version.version1")
AddVersionParent("vim.version.version6", "vmodl.query.version.version3")
AddVersionParent("vim.version.version6", "vmodl.query.version.version2")
AddVersionParent("vim.version.version6", "vmodl.query.version.version1")
AddVersionParent("vim.version.version6", "vim.version.version6")
AddVersionParent("vim.version.version6", "vim.version.version1")
AddVersionParent("vim.version.version6", "vim.version.version4")
AddVersionParent("vim.version.version6", "vim.version.version5")
AddVersionParent("vim.version.version6", "vim.version.version2")
AddVersionParent("vim.version.version6", "vim.version.version3")
AddVersionParent("vim.version.version6", "vmodl.version.version0")
AddVersionParent("vim.version.version6", "vmodl.version.version1")
AddVersionParent("vim.version.version7", "vmodl.query.version.version4")
AddVersionParent("vim.version.version7", "vmodl.query.version.version3")
AddVersionParent("vim.version.version7", "vmodl.query.version.version2")
AddVersionParent("vim.version.version7", "vmodl.query.version.version1")
AddVersionParent("vim.version.version7", "vim.version.version6")
AddVersionParent("vim.version.version7", "vim.version.version7")
AddVersionParent("vim.version.version7", "vim.version.version1")
AddVersionParent("vim.version.version7", "vim.version.version4")
AddVersionParent("vim.version.version7", "vim.version.version5")
AddVersionParent("vim.version.version7", "vim.version.version2")
AddVersionParent("vim.version.version7", "vim.version.version3")
AddVersionParent("vim.version.version7", "vmodl.version.version0")
AddVersionParent("vim.version.version7", "vmodl.version.version1")
AddVersionParent("vim.version.version7", "vmodl.version.version2")
AddVersionParent("vim.version.version7", "vmodl.reflect.version.version1")
AddVersionParent("vim.version.version1", "vmodl.query.version.version1")
AddVersionParent("vim.version.version1", "vim.version.version1")
AddVersionParent("vim.version.version1", "vmodl.version.version0")
AddVersionParent("vim.version.version4", "vmodl.query.version.version1")
AddVersionParent("vim.version.version4", "vim.version.version1")
AddVersionParent("vim.version.version4", "vim.version.version4")
AddVersionParent("vim.version.version4", "vim.version.version2")
AddVersionParent("vim.version.version4", "vim.version.version3")
AddVersionParent("vim.version.version4", "vmodl.version.version0")
AddVersionParent("vim.version.version5", "vmodl.query.version.version2")
AddVersionParent("vim.version.version5", "vmodl.query.version.version1")
AddVersionParent("vim.version.version5", "vim.version.version1")
AddVersionParent("vim.version.version5", "vim.version.version4")
AddVersionParent("vim.version.version5", "vim.version.version5")
AddVersionParent("vim.version.version5", "vim.version.version2")
AddVersionParent("vim.version.version5", "vim.version.version3")
AddVersionParent("vim.version.version5", "vmodl.version.version0")
AddVersionParent("vim.version.version5", "vmodl.version.version1")
AddVersionParent("vim.version.version2", "vmodl.query.version.version1")
AddVersionParent("vim.version.version2", "vim.version.version1")
AddVersionParent("vim.version.version2", "vim.version.version2")
AddVersionParent("vim.version.version2", "vmodl.version.version0")
AddVersionParent("vim.version.version3", "vmodl.query.version.version1")
AddVersionParent("vim.version.version3", "vim.version.version1")
AddVersionParent("vim.version.version3", "vim.version.version2")
AddVersionParent("vim.version.version3", "vim.version.version3")
AddVersionParent("vim.version.version3", "vmodl.version.version0")
AddVersionParent("vmodl.version.version0", "vmodl.version.version0")
AddVersionParent("vmodl.version.version1", "vmodl.version.version0")
AddVersionParent("vmodl.version.version1", "vmodl.version.version1")
AddVersionParent("vmodl.version.version2", "vmodl.version.version0")
AddVersionParent("vmodl.version.version2", "vmodl.version.version1")
AddVersionParent("vmodl.version.version2", "vmodl.version.version2")
AddVersionParent("vmodl.reflect.version.version1", "vmodl.version.version0")
AddVersionParent("vmodl.reflect.version.version1", "vmodl.version.version1")
AddVersionParent("vmodl.reflect.version.version1", "vmodl.version.version2")
AddVersionParent("vmodl.reflect.version.version1", "vmodl.reflect.version.version1")

newestVersions.Add("hmsdrs.version.version6")
ltsVersions.Add("hmsdrs.version.version6")
dottedVersions.Add("hmsdrs.version.version6")
oldestVersions.Add("hmsdrs.version.version6")

CreateDataType("hmsdrs.HbrDrmCollectionMoveSpec", "HmsSdrsHbrDrmCollectionMoveSpec", "vmodl.DynamicData", "hmsdrs.version.version6", [("collectionId", "string", "hmsdrs.version.version6", 0), ("diskSpecs", "hmsdrs.HbrDrmDiskMoveSpec[]", "hmsdrs.version.version6", 0)])
CreateDataType("hmsdrs.HbrDrmDiskBase", "HmsSdrsHbrDrmDiskBase", "vmodl.DynamicData", "hmsdrs.version.version6", [("diskId", "string", "hmsdrs.version.version6", 0), ("collectionId", "string", "hmsdrs.version.version6", 0), ("name", "string", "hmsdrs.version.version6", 0), ("datastoreMoId", "string", "hmsdrs.version.version6", 0), ("spaceRequirement", "long", "hmsdrs.version.version6", 0)])
CreateDataType("hmsdrs.HbrDrmDiskCollection", "HmsSdrsHbrDrmCollection", "vmodl.DynamicData", "hmsdrs.version.version6", [("collectionId", "string", "hmsdrs.version.version6", 0), ("name", "string", "hmsdrs.version.version6", 0), ("placeholderVmMoId", "string", "hmsdrs.version.version6", F_OPTIONAL), ("disks", "hmsdrs.HbrDrmDiskBase[]", "hmsdrs.version.version6", 0)])
CreateDataType("hmsdrs.HbrDrmDiskMoveSpec", "HmsSdrsHbrDrmMoveSpec", "vmodl.DynamicData", "hmsdrs.version.version6", [("diskId", "string", "hmsdrs.version.version6", 0), ("sourceDatastoreMoId", "string", "hmsdrs.version.version6", 0), ("destinationDatastoreMoId", "string", "hmsdrs.version.version6", 0)])
CreateDataType("hmsdrs.ImmovableHbrDrmDisk", "HmsSdrsImmovableHbrDrmDisk", "hmsdrs.HbrDrmDiskBase", "hmsdrs.version.version6", None)
CreateManagedType("hmsdrs.ReplicaMoveManager", "HmsReplicaMoveManager", "vmodl.ManagedObject", "hmsdrs.version.version6", None, [("queryCollections", "HmsReplicaMoveManagerQueryCollections", "hmsdrs.version.version6", (("datastoreMoIds", "string[]", "hmsdrs.version.version6", F_OPTIONAL, None),), (F_OPTIONAL, "hmsdrs.HbrDrmDiskCollection[]", "hmsdrs.HbrDrmDiskCollection[]"), "System.View", None), ("retrieveCurrentMoveTasks", "HmsReplicaMoveManagerRetrieveCurrentMoveTasks", "hmsdrs.version.version6", (("datastoreMoIds", "string[]", "hmsdrs.version.version6", F_OPTIONAL, None),), (F_OPTIONAL, "hmsdrs.ReplicaMoveManager.MoveTaskInfo[]", "hmsdrs.ReplicaMoveManager.MoveTaskInfo[]"), "System.View", None), ("moveCollection", "HmsReplicaMoveManagerMoveCollection_Task", "hmsdrs.version.version6", (("spec", "hmsdrs.HbrDrmCollectionMoveSpec", "hmsdrs.version.version6", 0, None),("allowCrossHostMove", "boolean", "hmsdrs.version.version6", F_OPTIONAL, None),), (0, "vim.Task", "void"), "Host.Hbr.HbrManagement", ["hmsdrs.fault.InvalidCollection", "hmsdrs.fault.MoveAlreadyInProgress", "hmsdrs.fault.DiskNotMovable", "hmsdrs.fault.CannotMoveAcrossHosts", ])])
CreateDataType("hmsdrs.ReplicaMoveManager.MoveTaskInfo", "HmsReplicaMoveManagerMoveTaskInfo", "vmodl.DynamicData", "hmsdrs.version.version6", [("moveSpec", "hmsdrs.HbrDrmCollectionMoveSpec", "hmsdrs.version.version6", 0), ("task", "vim.Task", "hmsdrs.version.version6", 0)])
CreateManagedType("hmsdrs.SdrsServiceInstance", "HmsSdrsServiceInstance", "vmodl.ManagedObject", "hmsdrs.version.version6", [("content", "hmsdrs.SdrsServiceInstanceContent", "hmsdrs.version.version6", 0, "System.Anonymous")], [("currentTime", "HmsSdrsServiceInstanceCurrentTime", "hmsdrs.version.version6", (), (0, "vmodl.DateTime", "vmodl.DateTime"), "System.View", None), ("ping", "HmsSdrsServiceInstancePing", "hmsdrs.version.version6", (), (0, "void", "void"), "System.Anonymous", None)])
CreateDataType("hmsdrs.SdrsServiceInstanceContent", "HmsSdrsServiceInstanceContent", "vmodl.DynamicData", "hmsdrs.version.version6", [("instanceUuid", "string", "hmsdrs.version.version6", 0), ("solutionUsername", "string", "hmsdrs.version.version6", 0), ("sessionManager", "hmsdrs.SdrsSessionManager", "hmsdrs.version.version6", 0), ("replicaMoveManager", "hmsdrs.ReplicaMoveManager", "hmsdrs.version.version6", 0)])
CreateManagedType("hmsdrs.SdrsSessionManager", "HmsSdrsSessionManager", "vmodl.ManagedObject", "hmsdrs.version.version6", None, [("loginByToken", "HmsSdrsSessionManagerLoginByToken", "hmsdrs.version.version6", (("delegatedToken", "string", "hmsdrs.version.version6", 0, None),("locale", "string", "hmsdrs.version.version6", F_OPTIONAL, None),), (0, "void", "void"), "System.Anonymous", ["vim.fault.InvalidLogin", "hmsdrs.fault.AlreadyLoggedIn", "hmsdrs.fault.CannotVerifyCredentialsFault", ]), ("logout", "HmsSdrsSessionManagerLogout", "hmsdrs.version.version6", (), (0, "void", "void"), "System.View", None)])
CreateDataType("hmsdrs.fault.SdrsFault", "HmsSdrsFault", "vmodl.MethodFault", "hmsdrs.version.version6", [("originalMessage", "string", "hmsdrs.version.version6", F_OPTIONAL)])
CreateDataType("hmsdrs.HbrDrmDisk", "HmsSdrsHbrDrmDisk", "hmsdrs.HbrDrmDiskBase", "hmsdrs.version.version6", [("movable", "boolean", "hmsdrs.version.version6", 0), ("datastoresForSingleHostMove", "vim.Datastore[]", "hmsdrs.version.version6", F_OPTIONAL)])
CreateDataType("hmsdrs.fault.AlreadyLoggedIn", "HmsSdrsFaultAlreadyLoggedIn", "hmsdrs.fault.SdrsFault", "hmsdrs.version.version6", None)
CreateDataType("hmsdrs.fault.CannotMoveAcrossHosts", "HmsSdrsFaultCannotMoveAcrossHosts", "hmsdrs.fault.SdrsFault", "hmsdrs.version.version6", None)
CreateDataType("hmsdrs.fault.CannotVerifyCredentialsFault", "HmsSdrsFaultCannotVerifyCredentialsFault", "hmsdrs.fault.SdrsFault", "hmsdrs.version.version6", None)
CreateDataType("hmsdrs.fault.DiskNotMovable", "HmsSdrsFaultDiskNotMovable", "hmsdrs.fault.SdrsFault", "hmsdrs.version.version6", [("nonMovableDisksIds", "string[]", "hmsdrs.version.version6", 0)])
CreateDataType("hmsdrs.fault.InvalidCollection", "HmsSdrsFaultInvalidCollection", "hmsdrs.fault.SdrsFault", "hmsdrs.version.version6", None)
CreateDataType("hmsdrs.fault.MoveAlreadyInProgress", "HmsSdrsFaultMoveAlreadyInProgress", "hmsdrs.fault.SdrsFault", "hmsdrs.version.version6", [("taskInProgress", "vim.Task", "hmsdrs.version.version6", 0)])
CreateDataType("hmsdrs.fault.MoveCanceled", "HmsSdrsFaultMoveCanceled", "hmsdrs.fault.SdrsFault", "hmsdrs.version.version6", None)
