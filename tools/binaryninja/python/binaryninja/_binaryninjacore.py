from __future__ import absolute_import
import ctypes, os

# Load core module
import platform
core = None
_base_path = None
if platform.system() == "Darwin":
	_base_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "MacOS")
	core = ctypes.CDLL(os.path.join(_base_path, "libbinaryninjacore.dylib"))

elif platform.system() == "Linux":
	_base_path = os.path.join(os.path.dirname(__file__), "..", "..")
	core = ctypes.CDLL(os.path.join(_base_path, "libbinaryninjacore.so.1"))

elif platform.system() == "Windows":
	_base_path = os.path.join(os.path.dirname(__file__), "..", "..")
	core = ctypes.CDLL(os.path.join(_base_path, "binaryninjacore.dll"))
else:
	raise Exception("OS not supported")

# Type definitions
ActionTypeEnum = ctypes.c_int
class BNAddressRange(ctypes.Structure):
	pass
class BNAnalysisCompletionEvent(ctypes.Structure):
	pass
class BNAnalysisProgress(ctypes.Structure):
	pass
AnalysisStateEnum = ctypes.c_int
class BNArchitecture(ctypes.Structure):
	pass
class BNArchitectureAndAddress(ctypes.Structure):
	pass
class BNBackgroundTask(ctypes.Structure):
	pass
class BNBasicBlock(ctypes.Structure):
	pass
class BNBasicBlockEdge(ctypes.Structure):
	pass
class BNBinaryDataNotification(ctypes.Structure):
	pass
class BNBinaryReader(ctypes.Structure):
	pass
class BNBinaryView(ctypes.Structure):
	pass
class BNBinaryViewType(ctypes.Structure):
	pass
class BNBinaryWriter(ctypes.Structure):
	pass
class BNBoolWithConfidence(ctypes.Structure):
	pass
BranchTypeEnum = ctypes.c_int
class BNCallingConvention(ctypes.Structure):
	pass
CallingConventionNameEnum = ctypes.c_int
class BNCallingConventionWithConfidence(ctypes.Structure):
	pass
class BNConstantReference(ctypes.Structure):
	pass
class BNCustomArchitecture(ctypes.Structure):
	pass
class BNCustomBinaryView(ctypes.Structure):
	pass
class BNCustomBinaryViewType(ctypes.Structure):
	pass
class BNCustomCallingConvention(ctypes.Structure):
	pass
class BNCustomTransform(ctypes.Structure):
	pass
class BNDataBuffer(ctypes.Structure):
	pass
class BNDataVariable(ctypes.Structure):
	pass
DisassemblyOptionEnum = ctypes.c_int
class BNDisassemblySettings(ctypes.Structure):
	pass
class BNDisassemblyTextLine(ctypes.Structure):
	pass
EndiannessEnum = ctypes.c_int
class BNEnumeration(ctypes.Structure):
	pass
class BNEnumerationMember(ctypes.Structure):
	pass
class BNFileAccessor(ctypes.Structure):
	pass
class BNFileMetadata(ctypes.Structure):
	pass
FindFlagEnum = ctypes.c_int
FlagRoleEnum = ctypes.c_int
class BNFormInputField(ctypes.Structure):
	pass
FormInputFieldTypeEnum = ctypes.c_int
class BNFunction(ctypes.Structure):
	pass
class BNFunctionGraph(ctypes.Structure):
	pass
class BNFunctionGraphBlock(ctypes.Structure):
	pass
class BNFunctionGraphEdge(ctypes.Structure):
	pass
FunctionGraphTypeEnum = ctypes.c_int
class BNFunctionParameter(ctypes.Structure):
	pass
class BNFunctionRecognizer(ctypes.Structure):
	pass
class BNHighlightColor(ctypes.Structure):
	pass
HighlightColorStyleEnum = ctypes.c_int
HighlightStandardColorEnum = ctypes.c_int
ILBranchDependenceEnum = ctypes.c_int
class BNILBranchInstructionAndDependence(ctypes.Structure):
	pass
ImplicitRegisterExtendEnum = ctypes.c_int
class BNIndirectBranchInfo(ctypes.Structure):
	pass
class BNInstructionInfo(ctypes.Structure):
	pass
class BNInstructionTextLine(ctypes.Structure):
	pass
class BNInstructionTextToken(ctypes.Structure):
	pass
InstructionTextTokenContextEnum = ctypes.c_int
InstructionTextTokenTypeEnum = ctypes.c_int
IntegerDisplayTypeEnum = ctypes.c_int
class BNInteractionHandlerCallbacks(ctypes.Structure):
	pass
class BNLinearDisassemblyLine(ctypes.Structure):
	pass
LinearDisassemblyLineTypeEnum = ctypes.c_int
class BNLinearDisassemblyPosition(ctypes.Structure):
	pass
LogLevelEnum = ctypes.c_int
class BNLogListener(ctypes.Structure):
	pass
class BNLookupTableEntry(ctypes.Structure):
	pass
LowLevelILFlagConditionEnum = ctypes.c_int
class BNLowLevelILFunction(ctypes.Structure):
	pass
class BNLowLevelILInstruction(ctypes.Structure):
	pass
class BNLowLevelILLabel(ctypes.Structure):
	pass
LowLevelILOperationEnum = ctypes.c_int
class BNMainThreadAction(ctypes.Structure):
	pass
class BNMainThreadCallbacks(ctypes.Structure):
	pass
class BNMediumLevelILFunction(ctypes.Structure):
	pass
class BNMediumLevelILInstruction(ctypes.Structure):
	pass
class BNMediumLevelILLabel(ctypes.Structure):
	pass
MediumLevelILOperationEnum = ctypes.c_int
MemberAccessEnum = ctypes.c_int
class BNMemberAccessWithConfidence(ctypes.Structure):
	pass
MemberScopeEnum = ctypes.c_int
class BNMemberScopeWithConfidence(ctypes.Structure):
	pass
MessageBoxButtonResultEnum = ctypes.c_int
MessageBoxButtonSetEnum = ctypes.c_int
MessageBoxIconEnum = ctypes.c_int
class BNMetadata(ctypes.Structure):
	pass
MetadataTypeEnum = ctypes.c_int
class BNMetadataValueStore(ctypes.Structure):
	pass
ModificationStatusEnum = ctypes.c_int
NameTypeEnum = ctypes.c_int
class BNNamedTypeReference(ctypes.Structure):
	pass
NamedTypeReferenceClassEnum = ctypes.c_int
class BNNavigationHandler(ctypes.Structure):
	pass
class BNObjectDestructionCallbacks(ctypes.Structure):
	pass
class BNParameterVariablesWithConfidence(ctypes.Structure):
	pass
class BNPerformanceInfo(ctypes.Structure):
	pass
class BNPlatform(ctypes.Structure):
	pass
class BNPluginCommand(ctypes.Structure):
	pass
PluginCommandTypeEnum = ctypes.c_int
PluginLoadOrderEnum = ctypes.c_int
PluginOriginEnum = ctypes.c_int
PluginTypeEnum = ctypes.c_int
PluginUpdateStatusEnum = ctypes.c_int
class BNPoint(ctypes.Structure):
	pass
PointerSuffixEnum = ctypes.c_int
class BNPossibleValueSet(ctypes.Structure):
	pass
class BNQualifiedName(ctypes.Structure):
	pass
class BNQualifiedNameAndType(ctypes.Structure):
	pass
class BNReferenceSource(ctypes.Structure):
	pass
ReferenceTypeEnum = ctypes.c_int
class BNRegisterInfo(ctypes.Structure):
	pass
class BNRegisterOrConstant(ctypes.Structure):
	pass
class BNRegisterSetWithConfidence(ctypes.Structure):
	pass
class BNRegisterValue(ctypes.Structure):
	pass
RegisterValueTypeEnum = ctypes.c_int
class BNRegisterValueWithConfidence(ctypes.Structure):
	pass
class BNRepoPlugin(ctypes.Structure):
	pass
class BNRepository(ctypes.Structure):
	pass
class BNRepositoryManager(ctypes.Structure):
	pass
class BNScriptingInstance(ctypes.Structure):
	pass
class BNScriptingInstanceCallbacks(ctypes.Structure):
	pass
class BNScriptingOutputListener(ctypes.Structure):
	pass
class BNScriptingProvider(ctypes.Structure):
	pass
class BNScriptingProviderCallbacks(ctypes.Structure):
	pass
ScriptingProviderExecuteResultEnum = ctypes.c_int
ScriptingProviderInputReadyStateEnum = ctypes.c_int
class BNSection(ctypes.Structure):
	pass
SectionSemanticsEnum = ctypes.c_int
class BNSegment(ctypes.Structure):
	pass
SegmentFlagEnum = ctypes.c_int
class BNSizeWithConfidence(ctypes.Structure):
	pass
class BNStackVariableReference(ctypes.Structure):
	pass
class BNStringReference(ctypes.Structure):
	pass
StringTypeEnum = ctypes.c_int
class BNStructure(ctypes.Structure):
	pass
class BNStructureMember(ctypes.Structure):
	pass
StructureTypeEnum = ctypes.c_int
class BNSymbol(ctypes.Structure):
	pass
SymbolTypeEnum = ctypes.c_int
class BNSystemCallInfo(ctypes.Structure):
	pass
class BNTemporaryFile(ctypes.Structure):
	pass
class BNTransform(ctypes.Structure):
	pass
class BNTransformParameter(ctypes.Structure):
	pass
class BNTransformParameterInfo(ctypes.Structure):
	pass
TransformTypeEnum = ctypes.c_int
class BNType(ctypes.Structure):
	pass
TypeClassEnum = ctypes.c_int
class BNTypeParserResult(ctypes.Structure):
	pass
class BNTypeWithConfidence(ctypes.Structure):
	pass
class BNUndoAction(ctypes.Structure):
	pass
class BNUpdateChannel(ctypes.Structure):
	pass
UpdateResultEnum = ctypes.c_int
class BNUpdateVersion(ctypes.Structure):
	pass
class BNValueRange(ctypes.Structure):
	pass
class BNVariable(ctypes.Structure):
	pass
class BNVariableNameAndType(ctypes.Structure):
	pass
VariableSourceTypeEnum = ctypes.c_int

# Structure definitions
BNAddressRange._fields_ = [
		("start", ctypes.c_ulonglong),
		("end", ctypes.c_ulonglong),
	]
BNAnalysisProgress._fields_ = [
		("state", AnalysisStateEnum),
		("count", ctypes.c_ulonglong),
		("total", ctypes.c_ulonglong),
	]
BNArchitectureAndAddress._fields_ = [
		("arch", ctypes.POINTER(BNArchitecture)),
		("address", ctypes.c_ulonglong),
	]
BNBasicBlockEdge._fields_ = [
		("type", BranchTypeEnum),
		("target", ctypes.POINTER(BNBasicBlock)),
		("backEdge", ctypes.c_bool),
	]
BNBinaryDataNotification._fields_ = [
		("context", ctypes.c_void_p),
		("dataWritten", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("dataInserted", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("dataRemoved", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("functionAdded", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.POINTER(BNFunction))),
		("functionRemoved", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.POINTER(BNFunction))),
		("functionUpdated", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.POINTER(BNFunction))),
		("dataVariableAdded", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.POINTER(BNDataVariable))),
		("dataVariableRemoved", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.POINTER(BNDataVariable))),
		("dataVariableUpdated", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.POINTER(BNDataVariable))),
		("stringFound", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), StringTypeEnum, ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("stringRemoved", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), StringTypeEnum, ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("typeDefined", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.POINTER(BNQualifiedName), ctypes.POINTER(BNType))),
		("typeUndefined", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.POINTER(BNQualifiedName), ctypes.POINTER(BNType))),
	]
BNBoolWithConfidence._fields_ = [
		("value", ctypes.c_bool),
		("confidence", ctypes.c_ubyte),
	]
BNCallingConventionWithConfidence._fields_ = [
		("convention", ctypes.POINTER(BNCallingConvention)),
		("confidence", ctypes.c_ubyte),
	]
BNConstantReference._fields_ = [
		("value", ctypes.c_longlong),
		("size", ctypes.c_ulonglong),
		("pointer", ctypes.c_bool),
		("intermediate", ctypes.c_bool),
	]
BNCustomArchitecture._fields_ = [
		("context", ctypes.c_void_p),
		("init", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNArchitecture))),
		("getEndianness", ctypes.CFUNCTYPE(EndiannessEnum, ctypes.c_void_p)),
		("getAddressSize", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p)),
		("getDefaultIntegerSize", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p)),
		("getMaxInstructionLength", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p)),
		("getOpcodeDisplayLength", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p)),
		("getAssociatedArchitectureByAddress", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ulonglong))),
		("getInstructionInfo", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_ulonglong, ctypes.c_ulonglong, ctypes.POINTER(BNInstructionInfo))),
		("getInstructionText", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_ulonglong, ctypes.POINTER(ctypes.c_ulonglong), ctypes.POINTER(ctypes.POINTER(BNInstructionTextToken)), ctypes.POINTER(ctypes.c_ulonglong))),
		("freeInstructionText", ctypes.CFUNCTYPE(None, ctypes.POINTER(BNInstructionTextToken), ctypes.c_ulonglong)),
		("getInstructionLowLevelIL", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_ulonglong, ctypes.POINTER(ctypes.c_ulonglong), ctypes.POINTER(BNLowLevelILFunction))),
		("getRegisterName", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)),
		("getFlagName", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)),
		("getFlagWriteTypeName", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)),
		("getFullWidthRegisters", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ulonglong))),
		("getAllRegisters", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ulonglong))),
		("getAllFlags", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ulonglong))),
		("getAllFlagWriteTypes", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ulonglong))),
		("getFlagRole", ctypes.CFUNCTYPE(FlagRoleEnum, ctypes.c_void_p, ctypes.c_uint)),
		("getFlagsRequiredForFlagCondition", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, LowLevelILFlagConditionEnum, ctypes.POINTER(ctypes.c_ulonglong))),
		("getFlagsWrittenByFlagWriteType", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.POINTER(ctypes.c_ulonglong))),
		("getFlagWriteLowLevelIL", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p, LowLevelILOperationEnum, ctypes.c_ulonglong, ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(BNRegisterOrConstant), ctypes.c_ulonglong, ctypes.POINTER(BNLowLevelILFunction))),
		("getFlagConditionLowLevelIL", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p, LowLevelILFlagConditionEnum, ctypes.POINTER(BNLowLevelILFunction))),
		("freeRegisterList", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint))),
		("getRegisterInfo", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_uint, ctypes.POINTER(BNRegisterInfo))),
		("getStackPointerRegister", ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_void_p)),
		("getLinkRegister", ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_void_p)),
		("getGlobalRegisters", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ulonglong))),
		("assemble", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_ulonglong, ctypes.POINTER(BNDataBuffer), ctypes.POINTER(ctypes.c_char_p))),
		("isNeverBranchPatchAvailable", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("isAlwaysBranchPatchAvailable", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("isInvertBranchPatchAvailable", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("isSkipAndReturnZeroPatchAvailable", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("isSkipAndReturnValuePatchAvailable", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("convertToNop", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("alwaysBranch", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("invertBranch", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("skipAndReturnValue", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_ulonglong, ctypes.c_ulonglong, ctypes.c_ulonglong)),
	]
BNCustomBinaryView._fields_ = [
		("context", ctypes.c_void_p),
		("init", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p)),
		("freeObject", ctypes.CFUNCTYPE(None, ctypes.c_void_p)),
		("read", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("write", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_void_p, ctypes.c_ulonglong)),
		("insert", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_void_p, ctypes.c_ulonglong)),
		("remove", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("getModification", ctypes.CFUNCTYPE(ModificationStatusEnum, ctypes.c_void_p, ctypes.c_ulonglong)),
		("isValidOffset", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_ulonglong)),
		("isOffsetReadable", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_ulonglong)),
		("isOffsetWritable", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_ulonglong)),
		("isOffsetExecutable", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_ulonglong)),
		("isOffsetBackedByFile", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_ulonglong)),
		("getNextValidOffset", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p, ctypes.c_ulonglong)),
		("getStart", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p)),
		("getLength", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p)),
		("getEntryPoint", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p)),
		("isExecutable", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p)),
		("getDefaultEndianness", ctypes.CFUNCTYPE(EndiannessEnum, ctypes.c_void_p)),
		("getAddressSize", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p)),
		("save", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(BNFileAccessor))),
	]
BNCustomBinaryViewType._fields_ = [
		("context", ctypes.c_void_p),
		("create", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(BNBinaryView))),
		("isValidForData", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(BNBinaryView))),
	]
BNCustomCallingConvention._fields_ = [
		("context", ctypes.c_void_p),
		("freeObject", ctypes.CFUNCTYPE(None, ctypes.c_void_p)),
		("getCallerSavedRegisters", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ulonglong))),
		("getIntegerArgumentRegisters", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ulonglong))),
		("getFloatArgumentRegisters", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ulonglong))),
		("freeRegisterList", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint))),
		("areArgumentRegistersSharedIndex", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p)),
		("isStackReservedForArgumentRegisters", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p)),
		("isStackAdjustedOnReturn", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p)),
		("getIntegerReturnValueRegister", ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_void_p)),
		("getHighIntegerReturnValueRegister", ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_void_p)),
		("getFloatReturnValueRegister", ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_void_p)),
		("getGlobalPointerRegister", ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_void_p)),
		("getImplicitlyDefinedRegisters", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ulonglong))),
		("getIncomingRegisterValue", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_uint, ctypes.POINTER(BNFunction), ctypes.POINTER(BNRegisterValue))),
		("getIncomingFlagValue", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_uint, ctypes.POINTER(BNFunction), ctypes.POINTER(BNRegisterValue))),
	]
BNCustomTransform._fields_ = [
		("context", ctypes.c_void_p),
		("getParameters", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ulonglong))),
		("freeParameters", ctypes.CFUNCTYPE(None, ctypes.POINTER(BNTransformParameterInfo), ctypes.c_ulonglong)),
		("decode", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(BNDataBuffer), ctypes.POINTER(BNDataBuffer), ctypes.POINTER(BNTransformParameter), ctypes.c_ulonglong)),
		("encode", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(BNDataBuffer), ctypes.POINTER(BNDataBuffer), ctypes.POINTER(BNTransformParameter), ctypes.c_ulonglong)),
	]
BNDataVariable._fields_ = [
		("address", ctypes.c_ulonglong),
		("type", ctypes.POINTER(BNType)),
		("autoDiscovered", ctypes.c_bool),
		("typeConfidence", ctypes.c_ubyte),
	]
BNDisassemblyTextLine._fields_ = [
		("addr", ctypes.c_ulonglong),
		("tokens", ctypes.POINTER(BNInstructionTextToken)),
		("count", ctypes.c_ulonglong),
	]
BNEnumerationMember._fields_ = [
		("name", ctypes.c_char_p),
		("value", ctypes.c_ulonglong),
		("isDefault", ctypes.c_bool),
	]
BNFileAccessor._fields_ = [
		("context", ctypes.c_void_p),
		("getLength", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p)),
		("read", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("write", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_void_p, ctypes.c_ulonglong)),
	]
BNFormInputField._fields_ = [
		("type", FormInputFieldTypeEnum),
		("prompt", ctypes.c_char_p),
		("view", ctypes.POINTER(BNBinaryView)),
		("currentAddress", ctypes.c_ulonglong),
		("choices", ctypes.POINTER(ctypes.c_char_p)),
		("count", ctypes.c_ulonglong),
		("ext", ctypes.c_char_p),
		("defaultName", ctypes.c_char_p),
		("intResult", ctypes.c_longlong),
		("addressResult", ctypes.c_ulonglong),
		("stringResult", ctypes.c_char_p),
		("indexResult", ctypes.c_ulonglong),
	]
BNFunctionGraphEdge._fields_ = [
		("type", BranchTypeEnum),
		("target", ctypes.POINTER(BNBasicBlock)),
		("points", ctypes.POINTER(BNPoint)),
		("pointCount", ctypes.c_ulonglong),
		("backEdge", ctypes.c_bool),
	]
BNFunctionRecognizer._fields_ = [
		("context", ctypes.c_void_p),
		("recognizeLowLevelIL", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.POINTER(BNFunction), ctypes.POINTER(BNLowLevelILFunction))),
	]
BNHighlightColor._fields_ = [
		("style", HighlightColorStyleEnum),
		("color", HighlightStandardColorEnum),
		("mixColor", HighlightStandardColorEnum),
		("mix", ctypes.c_ubyte),
		("r", ctypes.c_ubyte),
		("g", ctypes.c_ubyte),
		("b", ctypes.c_ubyte),
		("alpha", ctypes.c_ubyte),
	]
BNILBranchInstructionAndDependence._fields_ = [
		("branch", ctypes.c_ulonglong),
		("dependence", ILBranchDependenceEnum),
	]
BNIndirectBranchInfo._fields_ = [
		("sourceArch", ctypes.POINTER(BNArchitecture)),
		("sourceAddr", ctypes.c_ulonglong),
		("destArch", ctypes.POINTER(BNArchitecture)),
		("destAddr", ctypes.c_ulonglong),
		("autoDefined", ctypes.c_bool),
	]
BNInstructionInfo._fields_ = [
		("length", ctypes.c_ulonglong),
		("branchCount", ctypes.c_ulonglong),
		("branchDelay", ctypes.c_bool),
		("branchType", BranchTypeEnum * 3),
		("branchTarget", ctypes.c_ulonglong * 3),
		("branchArch", ctypes.POINTER(BNArchitecture) * 3),
	]
BNInstructionTextLine._fields_ = [
		("tokens", ctypes.POINTER(BNInstructionTextToken)),
		("count", ctypes.c_ulonglong),
	]
BNInstructionTextToken._fields_ = [
		("type", InstructionTextTokenTypeEnum),
		("text", ctypes.c_char_p),
		("value", ctypes.c_ulonglong),
		("size", ctypes.c_ulonglong),
		("operand", ctypes.c_ulonglong),
		("context", InstructionTextTokenContextEnum),
		("confidence", ctypes.c_ubyte),
		("address", ctypes.c_ulonglong),
	]
BNInteractionHandlerCallbacks._fields_ = [
		("context", ctypes.c_void_p),
		("showPlainTextReport", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.c_char_p, ctypes.c_char_p)),
		("showMarkdownReport", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)),
		("showHTMLReport", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)),
		("getTextLineInput", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char_p), ctypes.c_char_p, ctypes.c_char_p)),
		("getIntegerInput", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_longlong), ctypes.c_char_p, ctypes.c_char_p)),
		("getAddressInput", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ulonglong), ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(BNBinaryView), ctypes.c_ulonglong)),
		("getChoiceInput", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ulonglong), ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), ctypes.c_ulonglong)),
		("getOpenFileNameInput", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char_p), ctypes.c_char_p, ctypes.c_char_p)),
		("getSaveFileNameInput", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char_p), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)),
		("getDirectoryNameInput", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char_p), ctypes.c_char_p, ctypes.c_char_p)),
		("getFormInput", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(BNFormInputField), ctypes.c_ulonglong, ctypes.c_char_p)),
		("showMessageBox", ctypes.CFUNCTYPE(MessageBoxButtonResultEnum, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, MessageBoxButtonSetEnum, MessageBoxIconEnum)),
	]
BNLinearDisassemblyLine._fields_ = [
		("type", LinearDisassemblyLineTypeEnum),
		("function", ctypes.POINTER(BNFunction)),
		("block", ctypes.POINTER(BNBasicBlock)),
		("lineOffset", ctypes.c_ulonglong),
		("contents", BNDisassemblyTextLine),
	]
BNLinearDisassemblyPosition._fields_ = [
		("function", ctypes.POINTER(BNFunction)),
		("block", ctypes.POINTER(BNBasicBlock)),
		("address", ctypes.c_ulonglong),
	]
BNLogListener._fields_ = [
		("context", ctypes.c_void_p),
		("log", ctypes.CFUNCTYPE(None, ctypes.c_void_p, LogLevelEnum, ctypes.c_char_p)),
		("close", ctypes.CFUNCTYPE(None, ctypes.c_void_p)),
		("getLogLevel", ctypes.CFUNCTYPE(LogLevelEnum, ctypes.c_void_p)),
	]
BNLookupTableEntry._fields_ = [
		("fromValues", ctypes.POINTER(ctypes.c_longlong)),
		("fromCount", ctypes.c_ulonglong),
		("toValue", ctypes.c_longlong),
	]
BNLowLevelILInstruction._fields_ = [
		("operation", LowLevelILOperationEnum),
		("size", ctypes.c_ulonglong),
		("flags", ctypes.c_uint),
		("sourceOperand", ctypes.c_uint),
		("operands", ctypes.c_ulonglong * 4),
		("address", ctypes.c_ulonglong),
	]
BNLowLevelILLabel._fields_ = [
		("resolved", ctypes.c_bool),
		("ref", ctypes.c_ulonglong),
		("operand", ctypes.c_ulonglong),
	]
BNMainThreadCallbacks._fields_ = [
		("context", ctypes.c_void_p),
		("addAction", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNMainThreadAction))),
	]
BNMediumLevelILInstruction._fields_ = [
		("operation", MediumLevelILOperationEnum),
		("sourceOperand", ctypes.c_uint),
		("size", ctypes.c_ulonglong),
		("operands", ctypes.c_ulonglong * 5),
		("address", ctypes.c_ulonglong),
	]
BNMediumLevelILLabel._fields_ = [
		("resolved", ctypes.c_bool),
		("ref", ctypes.c_ulonglong),
		("operand", ctypes.c_ulonglong),
	]
BNMemberAccessWithConfidence._fields_ = [
		("value", MemberAccessEnum),
		("confidence", ctypes.c_ubyte),
	]
BNMemberScopeWithConfidence._fields_ = [
		("value", MemberScopeEnum),
		("confidence", ctypes.c_ubyte),
	]
BNMetadataValueStore._fields_ = [
		("size", ctypes.c_ulonglong),
		("keys", ctypes.POINTER(ctypes.c_char_p)),
		("values", ctypes.POINTER(ctypes.POINTER(BNMetadata))),
	]
BNNavigationHandler._fields_ = [
		("context", ctypes.c_void_p),
		("getCurrentView", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)),
		("getCurrentOffset", ctypes.CFUNCTYPE(ctypes.c_ulonglong, ctypes.c_void_p)),
		("navigate", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_ulonglong)),
	]
BNObjectDestructionCallbacks._fields_ = [
		("context", ctypes.c_void_p),
		("destructBinaryView", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView))),
		("destructFileMetadata", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNFileMetadata))),
		("destructFunction", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNFunction))),
	]
BNParameterVariablesWithConfidence._fields_ = [
		("vars", ctypes.POINTER(BNVariable)),
		("count", ctypes.c_ulonglong),
		("confidence", ctypes.c_ubyte),
	]
BNPerformanceInfo._fields_ = [
		("name", ctypes.c_char_p),
		("seconds", ctypes.c_double),
	]
BNPluginCommand._fields_ = [
		("name", ctypes.c_char_p),
		("description", ctypes.c_char_p),
		("type", PluginCommandTypeEnum),
		("context", ctypes.c_void_p),
		("defaultCommand", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView))),
		("addressCommand", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.c_ulonglong)),
		("rangeCommand", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("functionCommand", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.POINTER(BNFunction))),
		("defaultIsValid", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(BNBinaryView))),
		("addressIsValid", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.c_ulonglong)),
		("rangeIsValid", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.c_ulonglong, ctypes.c_ulonglong)),
		("functionIsValid", ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.POINTER(BNFunction))),
	]
BNPoint._fields_ = [
		("x", ctypes.c_float),
		("y", ctypes.c_float),
	]
BNPossibleValueSet._fields_ = [
		("state", RegisterValueTypeEnum),
		("value", ctypes.c_longlong),
		("ranges", ctypes.POINTER(BNValueRange)),
		("valueSet", ctypes.POINTER(ctypes.c_longlong)),
		("table", ctypes.POINTER(BNLookupTableEntry)),
		("count", ctypes.c_ulonglong),
	]
BNQualifiedName._fields_ = [
		("name", ctypes.POINTER(ctypes.c_char_p)),
		("nameCount", ctypes.c_ulonglong),
	]
BNQualifiedNameAndType._fields_ = [
		("name", BNQualifiedName),
		("type", ctypes.POINTER(BNType)),
	]
BNReferenceSource._fields_ = [
		("func", ctypes.POINTER(BNFunction)),
		("arch", ctypes.POINTER(BNArchitecture)),
		("addr", ctypes.c_ulonglong),
	]
BNRegisterInfo._fields_ = [
		("fullWidthRegister", ctypes.c_uint),
		("offset", ctypes.c_ulonglong),
		("size", ctypes.c_ulonglong),
		("extend", ImplicitRegisterExtendEnum),
	]
BNRegisterOrConstant._fields_ = [
		("constant", ctypes.c_bool),
		("reg", ctypes.c_uint),
		("value", ctypes.c_ulonglong),
	]
BNRegisterSetWithConfidence._fields_ = [
		("regs", ctypes.POINTER(ctypes.c_uint)),
		("count", ctypes.c_ulonglong),
		("confidence", ctypes.c_ubyte),
	]
BNRegisterValue._fields_ = [
		("state", RegisterValueTypeEnum),
		("value", ctypes.c_longlong),
	]
BNRegisterValueWithConfidence._fields_ = [
		("value", BNRegisterValue),
		("confidence", ctypes.c_ubyte),
	]
BNScriptingInstanceCallbacks._fields_ = [
		("context", ctypes.c_void_p),
		("destroyInstance", ctypes.CFUNCTYPE(None, ctypes.c_void_p)),
		("executeScriptInput", ctypes.CFUNCTYPE(ScriptingProviderExecuteResultEnum, ctypes.c_void_p, ctypes.c_char_p)),
		("setCurrentBinaryView", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView))),
		("setCurrentFunction", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNFunction))),
		("setCurrentBasicBlock", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBasicBlock))),
		("setCurrentAddress", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_ulonglong)),
		("setCurrentSelection", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_ulonglong)),
	]
BNScriptingOutputListener._fields_ = [
		("context", ctypes.c_void_p),
		("output", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_char_p)),
		("error", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_char_p)),
		("inputReadyStateChanged", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ScriptingProviderInputReadyStateEnum)),
	]
BNScriptingProviderCallbacks._fields_ = [
		("context", ctypes.c_void_p),
		("createInstance", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)),
	]
BNSection._fields_ = [
		("name", ctypes.c_char_p),
		("type", ctypes.c_char_p),
		("start", ctypes.c_ulonglong),
		("length", ctypes.c_ulonglong),
		("linkedSection", ctypes.c_char_p),
		("infoSection", ctypes.c_char_p),
		("infoData", ctypes.c_ulonglong),
		("align", ctypes.c_ulonglong),
		("entrySize", ctypes.c_ulonglong),
		("semantics", SectionSemanticsEnum),
	]
BNSegment._fields_ = [
		("start", ctypes.c_ulonglong),
		("length", ctypes.c_ulonglong),
		("dataOffset", ctypes.c_ulonglong),
		("dataLength", ctypes.c_ulonglong),
		("flags", ctypes.c_uint),
	]
BNSizeWithConfidence._fields_ = [
		("value", ctypes.c_ulonglong),
		("confidence", ctypes.c_ubyte),
	]
BNStackVariableReference._fields_ = [
		("sourceOperand", ctypes.c_uint),
		("typeConfidence", ctypes.c_ubyte),
		("type", ctypes.POINTER(BNType)),
		("name", ctypes.c_char_p),
		("varIdentifier", ctypes.c_ulonglong),
		("referencedOffset", ctypes.c_longlong),
		("size", ctypes.c_ulonglong),
	]
BNStringReference._fields_ = [
		("type", StringTypeEnum),
		("start", ctypes.c_ulonglong),
		("length", ctypes.c_ulonglong),
	]
BNStructureMember._fields_ = [
		("type", ctypes.POINTER(BNType)),
		("name", ctypes.c_char_p),
		("offset", ctypes.c_ulonglong),
		("typeConfidence", ctypes.c_ubyte),
	]
BNSystemCallInfo._fields_ = [
		("number", ctypes.c_uint),
		("name", BNQualifiedName),
		("type", ctypes.POINTER(BNType)),
	]
BNTransformParameter._fields_ = [
		("name", ctypes.c_char_p),
		("value", ctypes.POINTER(BNDataBuffer)),
	]
BNTransformParameterInfo._fields_ = [
		("name", ctypes.c_char_p),
		("longName", ctypes.c_char_p),
		("fixedLength", ctypes.c_ulonglong),
	]
BNTypeParserResult._fields_ = [
		("types", ctypes.POINTER(BNQualifiedNameAndType)),
		("variables", ctypes.POINTER(BNQualifiedNameAndType)),
		("functions", ctypes.POINTER(BNQualifiedNameAndType)),
		("typeCount", ctypes.c_ulonglong),
		("variableCount", ctypes.c_ulonglong),
		("functionCount", ctypes.c_ulonglong),
	]
BNTypeWithConfidence._fields_ = [
		("type", ctypes.POINTER(BNType)),
		("confidence", ctypes.c_ubyte),
	]
BNUndoAction._fields_ = [
		("type", ActionTypeEnum),
		("context", ctypes.c_void_p),
		("freeObject", ctypes.CFUNCTYPE(None, ctypes.c_void_p)),
		("undo", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView))),
		("redo", ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView))),
		("serialize", ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)),
	]
BNUpdateChannel._fields_ = [
		("name", ctypes.c_char_p),
		("description", ctypes.c_char_p),
		("latestVersion", ctypes.c_char_p),
	]
BNUpdateVersion._fields_ = [
		("version", ctypes.c_char_p),
		("notes", ctypes.c_char_p),
		("time", ctypes.c_ulonglong),
	]
BNValueRange._fields_ = [
		("start", ctypes.c_ulonglong),
		("end", ctypes.c_ulonglong),
		("step", ctypes.c_ulonglong),
	]
BNVariable._fields_ = [
		("type", VariableSourceTypeEnum),
		("index", ctypes.c_uint),
		("storage", ctypes.c_longlong),
	]
BNVariableNameAndType._fields_ = [
		("var", BNVariable),
		("type", ctypes.POINTER(BNType)),
		("name", ctypes.c_char_p),
		("autoDefined", ctypes.c_bool),
		("typeConfidence", ctypes.c_ubyte),
	]
BNFunctionParameter._fields_ = [
		("name", ctypes.c_char_p),
		("type", ctypes.POINTER(BNType)),
		("typeConfidence", ctypes.c_ubyte),
		("defaultLocation", ctypes.c_bool),
		("location", BNVariable),
	]

# Function definitions
BNAbortAnalysis = core.BNAbortAnalysis
BNAbortAnalysis.restype = None
BNAbortAnalysis.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
BNAbortFunctionGraph = core.BNAbortFunctionGraph
BNAbortFunctionGraph.restype = None
BNAbortFunctionGraph.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
	]
_BNAddAnalysisCompletionEvent = core.BNAddAnalysisCompletionEvent
_BNAddAnalysisCompletionEvent.restype = ctypes.POINTER(BNAnalysisCompletionEvent)
_BNAddAnalysisCompletionEvent.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_void_p,
		ctypes.CFUNCTYPE(None, ctypes.c_void_p),
	]
def BNAddAnalysisCompletionEvent(*args):
	result = _BNAddAnalysisCompletionEvent(*args)
	if not result:
		return None
	return result
BNAddAnalysisOption = core.BNAddAnalysisOption
BNAddAnalysisOption.restype = None
BNAddAnalysisOption.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
	]
BNAddAutoSection = core.BNAddAutoSection
BNAddAutoSection.restype = None
BNAddAutoSection.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		SectionSemanticsEnum,
		ctypes.c_char_p,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_ulonglong,
	]
BNAddAutoSegment = core.BNAddAutoSegment
BNAddAutoSegment.restype = None
BNAddAutoSegment.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_uint,
	]
BNAddEntryPointForAnalysis = core.BNAddEntryPointForAnalysis
BNAddEntryPointForAnalysis.restype = None
BNAddEntryPointForAnalysis.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNPlatform),
		ctypes.c_ulonglong,
	]
BNAddEnumerationMember = core.BNAddEnumerationMember
BNAddEnumerationMember.restype = None
BNAddEnumerationMember.argtypes = [
		ctypes.POINTER(BNEnumeration),
		ctypes.c_char_p,
	]
BNAddEnumerationMemberWithValue = core.BNAddEnumerationMemberWithValue
BNAddEnumerationMemberWithValue.restype = None
BNAddEnumerationMemberWithValue.argtypes = [
		ctypes.POINTER(BNEnumeration),
		ctypes.c_char_p,
		ctypes.c_ulonglong,
	]
BNAddFunctionForAnalysis = core.BNAddFunctionForAnalysis
BNAddFunctionForAnalysis.restype = None
BNAddFunctionForAnalysis.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNPlatform),
		ctypes.c_ulonglong,
	]
BNAddLowLevelILLabelForAddress = core.BNAddLowLevelILLabelForAddress
BNAddLowLevelILLabelForAddress.restype = None
BNAddLowLevelILLabelForAddress.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
BNAddOptionalPluginDependency = core.BNAddOptionalPluginDependency
BNAddOptionalPluginDependency.restype = None
BNAddOptionalPluginDependency.argtypes = [
		ctypes.c_char_p,
	]
BNAddRelatedPlatform = core.BNAddRelatedPlatform
BNAddRelatedPlatform.restype = None
BNAddRelatedPlatform.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(BNPlatform),
	]
BNAddRequiredPluginDependency = core.BNAddRequiredPluginDependency
BNAddRequiredPluginDependency.restype = None
BNAddRequiredPluginDependency.argtypes = [
		ctypes.c_char_p,
	]
BNAddStructureMember = core.BNAddStructureMember
BNAddStructureMember.restype = None
BNAddStructureMember.argtypes = [
		ctypes.POINTER(BNStructure),
		ctypes.POINTER(BNTypeWithConfidence),
		ctypes.c_char_p,
	]
BNAddStructureMemberAtOffset = core.BNAddStructureMemberAtOffset
BNAddStructureMemberAtOffset.restype = None
BNAddStructureMemberAtOffset.argtypes = [
		ctypes.POINTER(BNStructure),
		ctypes.POINTER(BNTypeWithConfidence),
		ctypes.c_char_p,
		ctypes.c_ulonglong,
	]
BNAddUndoAction = core.BNAddUndoAction
BNAddUndoAction.restype = None
BNAddUndoAction.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
		ctypes.POINTER(BNUndoAction),
	]
BNAddUserSection = core.BNAddUserSection
BNAddUserSection.restype = None
BNAddUserSection.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		SectionSemanticsEnum,
		ctypes.c_char_p,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_ulonglong,
	]
BNAddUserSegment = core.BNAddUserSegment
BNAddUserSegment.restype = None
BNAddUserSegment.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_uint,
	]
_BNAllocString = core.BNAllocString
_BNAllocString.restype = ctypes.c_void_p
_BNAllocString.argtypes = [
		ctypes.c_char_p,
	]
def BNAllocString(*args):
	result = _BNAllocString(*args)
	if not result:
		return None
	return result
_BNAllocStringList = core.BNAllocStringList
_BNAllocStringList.restype = ctypes.POINTER(ctypes.c_char_p)
_BNAllocStringList.argtypes = [
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.c_ulonglong,
	]
def BNAllocStringList(*args):
	result = _BNAllocStringList(*args)
	if not result:
		return None
	return result
BNAlwaysBranch = core.BNAlwaysBranch
BNAlwaysBranch.restype = ctypes.c_bool
BNAlwaysBranch.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
BNAppendDataBuffer = core.BNAppendDataBuffer
BNAppendDataBuffer.restype = None
BNAppendDataBuffer.argtypes = [
		ctypes.POINTER(BNDataBuffer),
		ctypes.POINTER(BNDataBuffer),
	]
BNAppendDataBufferContents = core.BNAppendDataBufferContents
BNAppendDataBufferContents.restype = None
BNAppendDataBufferContents.argtypes = [
		ctypes.POINTER(BNDataBuffer),
		ctypes.c_void_p,
		ctypes.c_ulonglong,
	]
BNApplyAutoDiscoveredFunctionType = core.BNApplyAutoDiscoveredFunctionType
BNApplyAutoDiscoveredFunctionType.restype = None
BNApplyAutoDiscoveredFunctionType.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNType),
	]
BNApplyImportedTypes = core.BNApplyImportedTypes
BNApplyImportedTypes.restype = None
BNApplyImportedTypes.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNSymbol),
	]
BNArchitectureAlwaysBranch = core.BNArchitectureAlwaysBranch
BNArchitectureAlwaysBranch.restype = ctypes.c_bool
BNArchitectureAlwaysBranch.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ubyte),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNArchitectureConvertToNop = core.BNArchitectureConvertToNop
BNArchitectureConvertToNop.restype = ctypes.c_bool
BNArchitectureConvertToNop.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ubyte),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNArchitectureInvertBranch = core.BNArchitectureInvertBranch
BNArchitectureInvertBranch.restype = ctypes.c_bool
BNArchitectureInvertBranch.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ubyte),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNArchitectureSkipAndReturnValue = core.BNArchitectureSkipAndReturnValue
BNArchitectureSkipAndReturnValue.restype = ctypes.c_bool
BNArchitectureSkipAndReturnValue.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ubyte),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNAreArgumentRegistersSharedIndex = core.BNAreArgumentRegistersSharedIndex
BNAreArgumentRegistersSharedIndex.restype = ctypes.c_bool
BNAreArgumentRegistersSharedIndex.argtypes = [
		ctypes.POINTER(BNCallingConvention),
	]
BNAreAutoUpdatesEnabled = core.BNAreAutoUpdatesEnabled
BNAreAutoUpdatesEnabled.restype = ctypes.c_bool
BNAreAutoUpdatesEnabled.argtypes = [
	]
BNAreUpdatesAvailable = core.BNAreUpdatesAvailable
BNAreUpdatesAvailable.restype = ctypes.c_bool
BNAreUpdatesAvailable.argtypes = [
		ctypes.c_char_p,
		ctypes.POINTER(ctypes.c_char_p),
	]
BNAssemble = core.BNAssemble
BNAssemble.restype = ctypes.c_bool
BNAssemble.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_char_p,
		ctypes.c_ulonglong,
		ctypes.POINTER(BNDataBuffer),
		ctypes.POINTER(ctypes.c_char_p),
	]
BNAssignDataBuffer = core.BNAssignDataBuffer
BNAssignDataBuffer.restype = None
BNAssignDataBuffer.argtypes = [
		ctypes.POINTER(BNDataBuffer),
		ctypes.POINTER(BNDataBuffer),
	]
BNBasicBlockCanExit = core.BNBasicBlockCanExit
BNBasicBlockCanExit.restype = ctypes.c_bool
BNBasicBlockCanExit.argtypes = [
		ctypes.POINTER(BNBasicBlock),
	]
BNBasicBlockHasUndeterminedOutgoingEdges = core.BNBasicBlockHasUndeterminedOutgoingEdges
BNBasicBlockHasUndeterminedOutgoingEdges.restype = ctypes.c_bool
BNBasicBlockHasUndeterminedOutgoingEdges.argtypes = [
		ctypes.POINTER(BNBasicBlock),
	]
_BNBeginBackgroundTask = core.BNBeginBackgroundTask
_BNBeginBackgroundTask.restype = ctypes.POINTER(BNBackgroundTask)
_BNBeginBackgroundTask.argtypes = [
		ctypes.c_char_p,
		ctypes.c_bool,
	]
def BNBeginBackgroundTask(*args):
	result = _BNBeginBackgroundTask(*args)
	if not result:
		return None
	return result
BNBeginUndoActions = core.BNBeginUndoActions
BNBeginUndoActions.restype = None
BNBeginUndoActions.argtypes = [
		ctypes.POINTER(BNFileMetadata),
	]
_BNBinaryViewQueryMetadata = core.BNBinaryViewQueryMetadata
_BNBinaryViewQueryMetadata.restype = ctypes.POINTER(BNMetadata)
_BNBinaryViewQueryMetadata.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
	]
def BNBinaryViewQueryMetadata(*args):
	result = _BNBinaryViewQueryMetadata(*args)
	if not result:
		return None
	return result
BNBinaryViewRemoveMetadata = core.BNBinaryViewRemoveMetadata
BNBinaryViewRemoveMetadata.restype = None
BNBinaryViewRemoveMetadata.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
	]
BNBinaryViewStoreMetadata = core.BNBinaryViewStoreMetadata
BNBinaryViewStoreMetadata.restype = None
BNBinaryViewStoreMetadata.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
		ctypes.POINTER(BNMetadata),
	]
BNCanCancelBackgroundTask = core.BNCanCancelBackgroundTask
BNCanCancelBackgroundTask.restype = ctypes.c_bool
BNCanCancelBackgroundTask.argtypes = [
		ctypes.POINTER(BNBackgroundTask),
	]
BNCanFunctionReturn = core.BNCanFunctionReturn
BNCanFunctionReturn.restype = BNBoolWithConfidence
BNCanFunctionReturn.argtypes = [
		ctypes.POINTER(BNFunction),
	]
BNCancelAnalysisCompletionEvent = core.BNCancelAnalysisCompletionEvent
BNCancelAnalysisCompletionEvent.restype = None
BNCancelAnalysisCompletionEvent.argtypes = [
		ctypes.POINTER(BNAnalysisCompletionEvent),
	]
BNCancelBackgroundTask = core.BNCancelBackgroundTask
BNCancelBackgroundTask.restype = None
BNCancelBackgroundTask.argtypes = [
		ctypes.POINTER(BNBackgroundTask),
	]
BNClearDataBuffer = core.BNClearDataBuffer
BNClearDataBuffer.restype = None
BNClearDataBuffer.argtypes = [
		ctypes.POINTER(BNDataBuffer),
	]
BNCloseFile = core.BNCloseFile
BNCloseFile.restype = None
BNCloseFile.argtypes = [
		ctypes.POINTER(BNFileMetadata),
	]
BNCloseLogs = core.BNCloseLogs
BNCloseLogs.restype = None
BNCloseLogs.argtypes = [
	]
BNCommitUndoActions = core.BNCommitUndoActions
BNCommitUndoActions.restype = None
BNCommitUndoActions.argtypes = [
		ctypes.POINTER(BNFileMetadata),
	]
BNConvertToNop = core.BNConvertToNop
BNConvertToNop.restype = ctypes.c_bool
BNConvertToNop.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
_BNCreateArrayType = core.BNCreateArrayType
_BNCreateArrayType.restype = ctypes.POINTER(BNType)
_BNCreateArrayType.argtypes = [
		ctypes.POINTER(BNTypeWithConfidence),
		ctypes.c_ulonglong,
	]
def BNCreateArrayType(*args):
	result = _BNCreateArrayType(*args)
	if not result:
		return None
	return result
BNCreateAutoStackVariable = core.BNCreateAutoStackVariable
BNCreateAutoStackVariable.restype = None
BNCreateAutoStackVariable.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.c_longlong,
		ctypes.POINTER(BNTypeWithConfidence),
		ctypes.c_char_p,
	]
BNCreateAutoVariable = core.BNCreateAutoVariable
BNCreateAutoVariable.restype = None
BNCreateAutoVariable.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNVariable),
		ctypes.POINTER(BNTypeWithConfidence),
		ctypes.c_char_p,
		ctypes.c_bool,
	]
_BNCreateBinaryDataView = core.BNCreateBinaryDataView
_BNCreateBinaryDataView.restype = ctypes.POINTER(BNBinaryView)
_BNCreateBinaryDataView.argtypes = [
		ctypes.POINTER(BNFileMetadata),
	]
def BNCreateBinaryDataView(*args):
	result = _BNCreateBinaryDataView(*args)
	if not result:
		return None
	return result
_BNCreateBinaryDataViewFromBuffer = core.BNCreateBinaryDataViewFromBuffer
_BNCreateBinaryDataViewFromBuffer.restype = ctypes.POINTER(BNBinaryView)
_BNCreateBinaryDataViewFromBuffer.argtypes = [
		ctypes.POINTER(BNFileMetadata),
		ctypes.POINTER(BNDataBuffer),
	]
def BNCreateBinaryDataViewFromBuffer(*args):
	result = _BNCreateBinaryDataViewFromBuffer(*args)
	if not result:
		return None
	return result
_BNCreateBinaryDataViewFromData = core.BNCreateBinaryDataViewFromData
_BNCreateBinaryDataViewFromData.restype = ctypes.POINTER(BNBinaryView)
_BNCreateBinaryDataViewFromData.argtypes = [
		ctypes.POINTER(BNFileMetadata),
		ctypes.c_void_p,
		ctypes.c_ulonglong,
	]
def BNCreateBinaryDataViewFromData(*args):
	result = _BNCreateBinaryDataViewFromData(*args)
	if not result:
		return None
	return result
_BNCreateBinaryDataViewFromFile = core.BNCreateBinaryDataViewFromFile
_BNCreateBinaryDataViewFromFile.restype = ctypes.POINTER(BNBinaryView)
_BNCreateBinaryDataViewFromFile.argtypes = [
		ctypes.POINTER(BNFileMetadata),
		ctypes.POINTER(BNFileAccessor),
	]
def BNCreateBinaryDataViewFromFile(*args):
	result = _BNCreateBinaryDataViewFromFile(*args)
	if not result:
		return None
	return result
_BNCreateBinaryDataViewFromFilename = core.BNCreateBinaryDataViewFromFilename
_BNCreateBinaryDataViewFromFilename.restype = ctypes.POINTER(BNBinaryView)
_BNCreateBinaryDataViewFromFilename.argtypes = [
		ctypes.POINTER(BNFileMetadata),
		ctypes.c_char_p,
	]
def BNCreateBinaryDataViewFromFilename(*args):
	result = _BNCreateBinaryDataViewFromFilename(*args)
	if not result:
		return None
	return result
_BNCreateBinaryReader = core.BNCreateBinaryReader
_BNCreateBinaryReader.restype = ctypes.POINTER(BNBinaryReader)
_BNCreateBinaryReader.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
def BNCreateBinaryReader(*args):
	result = _BNCreateBinaryReader(*args)
	if not result:
		return None
	return result
_BNCreateBinaryViewOfType = core.BNCreateBinaryViewOfType
_BNCreateBinaryViewOfType.restype = ctypes.POINTER(BNBinaryView)
_BNCreateBinaryViewOfType.argtypes = [
		ctypes.POINTER(BNBinaryViewType),
		ctypes.POINTER(BNBinaryView),
	]
def BNCreateBinaryViewOfType(*args):
	result = _BNCreateBinaryViewOfType(*args)
	if not result:
		return None
	return result
_BNCreateBinaryWriter = core.BNCreateBinaryWriter
_BNCreateBinaryWriter.restype = ctypes.POINTER(BNBinaryWriter)
_BNCreateBinaryWriter.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
def BNCreateBinaryWriter(*args):
	result = _BNCreateBinaryWriter(*args)
	if not result:
		return None
	return result
_BNCreateBoolType = core.BNCreateBoolType
_BNCreateBoolType.restype = ctypes.POINTER(BNType)
_BNCreateBoolType.argtypes = [
	]
def BNCreateBoolType(*args):
	result = _BNCreateBoolType(*args)
	if not result:
		return None
	return result
_BNCreateCallingConvention = core.BNCreateCallingConvention
_BNCreateCallingConvention.restype = ctypes.POINTER(BNCallingConvention)
_BNCreateCallingConvention.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_char_p,
		ctypes.POINTER(BNCustomCallingConvention),
	]
def BNCreateCallingConvention(*args):
	result = _BNCreateCallingConvention(*args)
	if not result:
		return None
	return result
_BNCreateCustomBinaryView = core.BNCreateCustomBinaryView
_BNCreateCustomBinaryView.restype = ctypes.POINTER(BNBinaryView)
_BNCreateCustomBinaryView.argtypes = [
		ctypes.c_char_p,
		ctypes.POINTER(BNFileMetadata),
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNCustomBinaryView),
	]
def BNCreateCustomBinaryView(*args):
	result = _BNCreateCustomBinaryView(*args)
	if not result:
		return None
	return result
_BNCreateDataBuffer = core.BNCreateDataBuffer
_BNCreateDataBuffer.restype = ctypes.POINTER(BNDataBuffer)
_BNCreateDataBuffer.argtypes = [
		ctypes.c_void_p,
		ctypes.c_ulonglong,
	]
def BNCreateDataBuffer(*args):
	result = _BNCreateDataBuffer(*args)
	if not result:
		return None
	return result
BNCreateDatabase = core.BNCreateDatabase
BNCreateDatabase.restype = ctypes.c_bool
BNCreateDatabase.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
	]
BNCreateDatabaseWithProgress = core.BNCreateDatabaseWithProgress
BNCreateDatabaseWithProgress.restype = ctypes.c_bool
BNCreateDatabaseWithProgress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
		ctypes.c_void_p,
		ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_ulonglong),
	]
BNCreateDirectory = core.BNCreateDirectory
BNCreateDirectory.restype = ctypes.c_bool
BNCreateDirectory.argtypes = [
		ctypes.c_char_p,
		ctypes.c_bool,
	]
_BNCreateDisassemblySettings = core.BNCreateDisassemblySettings
_BNCreateDisassemblySettings.restype = ctypes.POINTER(BNDisassemblySettings)
_BNCreateDisassemblySettings.argtypes = [
	]
def BNCreateDisassemblySettings(*args):
	result = _BNCreateDisassemblySettings(*args)
	if not result:
		return None
	return result
_BNCreateEnumeration = core.BNCreateEnumeration
_BNCreateEnumeration.restype = ctypes.POINTER(BNEnumeration)
_BNCreateEnumeration.argtypes = [
	]
def BNCreateEnumeration(*args):
	result = _BNCreateEnumeration(*args)
	if not result:
		return None
	return result
_BNCreateEnumerationType = core.BNCreateEnumerationType
_BNCreateEnumerationType.restype = ctypes.POINTER(BNType)
_BNCreateEnumerationType.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(BNEnumeration),
		ctypes.c_ulonglong,
		ctypes.c_bool,
	]
def BNCreateEnumerationType(*args):
	result = _BNCreateEnumerationType(*args)
	if not result:
		return None
	return result
_BNCreateFileMetadata = core.BNCreateFileMetadata
_BNCreateFileMetadata.restype = ctypes.POINTER(BNFileMetadata)
_BNCreateFileMetadata.argtypes = [
	]
def BNCreateFileMetadata(*args):
	result = _BNCreateFileMetadata(*args)
	if not result:
		return None
	return result
_BNCreateFloatType = core.BNCreateFloatType
_BNCreateFloatType.restype = ctypes.POINTER(BNType)
_BNCreateFloatType.argtypes = [
		ctypes.c_ulonglong,
		ctypes.c_char_p,
	]
def BNCreateFloatType(*args):
	result = _BNCreateFloatType(*args)
	if not result:
		return None
	return result
_BNCreateFunctionGraph = core.BNCreateFunctionGraph
_BNCreateFunctionGraph.restype = ctypes.POINTER(BNFunctionGraph)
_BNCreateFunctionGraph.argtypes = [
		ctypes.POINTER(BNFunction),
	]
def BNCreateFunctionGraph(*args):
	result = _BNCreateFunctionGraph(*args)
	if not result:
		return None
	return result
_BNCreateFunctionType = core.BNCreateFunctionType
_BNCreateFunctionType.restype = ctypes.POINTER(BNType)
_BNCreateFunctionType.argtypes = [
		ctypes.POINTER(BNTypeWithConfidence),
		ctypes.POINTER(BNCallingConventionWithConfidence),
		ctypes.POINTER(BNFunctionParameter),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNBoolWithConfidence),
		ctypes.POINTER(BNSizeWithConfidence),
	]
def BNCreateFunctionType(*args):
	result = _BNCreateFunctionType(*args)
	if not result:
		return None
	return result
_BNCreateIntegerType = core.BNCreateIntegerType
_BNCreateIntegerType.restype = ctypes.POINTER(BNType)
_BNCreateIntegerType.argtypes = [
		ctypes.c_ulonglong,
		ctypes.POINTER(BNBoolWithConfidence),
		ctypes.c_char_p,
	]
def BNCreateIntegerType(*args):
	result = _BNCreateIntegerType(*args)
	if not result:
		return None
	return result
_BNCreateLowLevelILFunction = core.BNCreateLowLevelILFunction
_BNCreateLowLevelILFunction.restype = ctypes.POINTER(BNLowLevelILFunction)
_BNCreateLowLevelILFunction.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(BNFunction),
	]
def BNCreateLowLevelILFunction(*args):
	result = _BNCreateLowLevelILFunction(*args)
	if not result:
		return None
	return result
_BNCreateMediumLevelILFunction = core.BNCreateMediumLevelILFunction
_BNCreateMediumLevelILFunction.restype = ctypes.POINTER(BNMediumLevelILFunction)
_BNCreateMediumLevelILFunction.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(BNFunction),
	]
def BNCreateMediumLevelILFunction(*args):
	result = _BNCreateMediumLevelILFunction(*args)
	if not result:
		return None
	return result
_BNCreateMetadataArray = core.BNCreateMetadataArray
_BNCreateMetadataArray.restype = ctypes.POINTER(BNMetadata)
_BNCreateMetadataArray.argtypes = [
		ctypes.POINTER(ctypes.POINTER(BNMetadata)),
		ctypes.c_ulonglong,
	]
def BNCreateMetadataArray(*args):
	result = _BNCreateMetadataArray(*args)
	if not result:
		return None
	return result
_BNCreateMetadataBooleanData = core.BNCreateMetadataBooleanData
_BNCreateMetadataBooleanData.restype = ctypes.POINTER(BNMetadata)
_BNCreateMetadataBooleanData.argtypes = [
		ctypes.c_bool,
	]
def BNCreateMetadataBooleanData(*args):
	result = _BNCreateMetadataBooleanData(*args)
	if not result:
		return None
	return result
_BNCreateMetadataDoubleData = core.BNCreateMetadataDoubleData
_BNCreateMetadataDoubleData.restype = ctypes.POINTER(BNMetadata)
_BNCreateMetadataDoubleData.argtypes = [
		ctypes.c_double,
	]
def BNCreateMetadataDoubleData(*args):
	result = _BNCreateMetadataDoubleData(*args)
	if not result:
		return None
	return result
_BNCreateMetadataOfType = core.BNCreateMetadataOfType
_BNCreateMetadataOfType.restype = ctypes.POINTER(BNMetadata)
_BNCreateMetadataOfType.argtypes = [
		MetadataTypeEnum,
	]
def BNCreateMetadataOfType(*args):
	result = _BNCreateMetadataOfType(*args)
	if not result:
		return None
	return result
_BNCreateMetadataRawData = core.BNCreateMetadataRawData
_BNCreateMetadataRawData.restype = ctypes.POINTER(BNMetadata)
_BNCreateMetadataRawData.argtypes = [
		ctypes.POINTER(ctypes.c_ubyte),
		ctypes.c_ulonglong,
	]
def BNCreateMetadataRawData(*args):
	result = _BNCreateMetadataRawData(*args)
	if not result:
		return None
	return result
_BNCreateMetadataSignedIntegerData = core.BNCreateMetadataSignedIntegerData
_BNCreateMetadataSignedIntegerData.restype = ctypes.POINTER(BNMetadata)
_BNCreateMetadataSignedIntegerData.argtypes = [
		ctypes.c_longlong,
	]
def BNCreateMetadataSignedIntegerData(*args):
	result = _BNCreateMetadataSignedIntegerData(*args)
	if not result:
		return None
	return result
_BNCreateMetadataStringData = core.BNCreateMetadataStringData
_BNCreateMetadataStringData.restype = ctypes.POINTER(BNMetadata)
_BNCreateMetadataStringData.argtypes = [
		ctypes.c_char_p,
	]
def BNCreateMetadataStringData(*args):
	result = _BNCreateMetadataStringData(*args)
	if not result:
		return None
	return result
_BNCreateMetadataUnsignedIntegerData = core.BNCreateMetadataUnsignedIntegerData
_BNCreateMetadataUnsignedIntegerData.restype = ctypes.POINTER(BNMetadata)
_BNCreateMetadataUnsignedIntegerData.argtypes = [
		ctypes.c_ulonglong,
	]
def BNCreateMetadataUnsignedIntegerData(*args):
	result = _BNCreateMetadataUnsignedIntegerData(*args)
	if not result:
		return None
	return result
_BNCreateMetadataValueStore = core.BNCreateMetadataValueStore
_BNCreateMetadataValueStore.restype = ctypes.POINTER(BNMetadata)
_BNCreateMetadataValueStore.argtypes = [
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.POINTER(ctypes.POINTER(BNMetadata)),
		ctypes.c_ulonglong,
	]
def BNCreateMetadataValueStore(*args):
	result = _BNCreateMetadataValueStore(*args)
	if not result:
		return None
	return result
_BNCreateNamedType = core.BNCreateNamedType
_BNCreateNamedType.restype = ctypes.POINTER(BNNamedTypeReference)
_BNCreateNamedType.argtypes = [
	]
def BNCreateNamedType(*args):
	result = _BNCreateNamedType(*args)
	if not result:
		return None
	return result
_BNCreateNamedTypeReference = core.BNCreateNamedTypeReference
_BNCreateNamedTypeReference.restype = ctypes.POINTER(BNType)
_BNCreateNamedTypeReference.argtypes = [
		ctypes.POINTER(BNNamedTypeReference),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
def BNCreateNamedTypeReference(*args):
	result = _BNCreateNamedTypeReference(*args)
	if not result:
		return None
	return result
_BNCreateNamedTypeReferenceFromType = core.BNCreateNamedTypeReferenceFromType
_BNCreateNamedTypeReferenceFromType.restype = ctypes.POINTER(BNType)
_BNCreateNamedTypeReferenceFromType.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNQualifiedName),
	]
def BNCreateNamedTypeReferenceFromType(*args):
	result = _BNCreateNamedTypeReferenceFromType(*args)
	if not result:
		return None
	return result
_BNCreateNamedTypeReferenceFromTypeAndId = core.BNCreateNamedTypeReferenceFromTypeAndId
_BNCreateNamedTypeReferenceFromTypeAndId.restype = ctypes.POINTER(BNType)
_BNCreateNamedTypeReferenceFromTypeAndId.argtypes = [
		ctypes.c_char_p,
		ctypes.POINTER(BNQualifiedName),
		ctypes.POINTER(BNType),
	]
def BNCreateNamedTypeReferenceFromTypeAndId(*args):
	result = _BNCreateNamedTypeReferenceFromTypeAndId(*args)
	if not result:
		return None
	return result
_BNCreatePlatform = core.BNCreatePlatform
_BNCreatePlatform.restype = ctypes.POINTER(BNPlatform)
_BNCreatePlatform.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_char_p,
	]
def BNCreatePlatform(*args):
	result = _BNCreatePlatform(*args)
	if not result:
		return None
	return result
_BNCreatePointerType = core.BNCreatePointerType
_BNCreatePointerType.restype = ctypes.POINTER(BNType)
_BNCreatePointerType.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(BNTypeWithConfidence),
		ctypes.POINTER(BNBoolWithConfidence),
		ctypes.POINTER(BNBoolWithConfidence),
		ReferenceTypeEnum,
	]
def BNCreatePointerType(*args):
	result = _BNCreatePointerType(*args)
	if not result:
		return None
	return result
_BNCreatePointerTypeOfWidth = core.BNCreatePointerTypeOfWidth
_BNCreatePointerTypeOfWidth.restype = ctypes.POINTER(BNType)
_BNCreatePointerTypeOfWidth.argtypes = [
		ctypes.c_ulonglong,
		ctypes.POINTER(BNTypeWithConfidence),
		ctypes.POINTER(BNBoolWithConfidence),
		ctypes.POINTER(BNBoolWithConfidence),
		ReferenceTypeEnum,
	]
def BNCreatePointerTypeOfWidth(*args):
	result = _BNCreatePointerTypeOfWidth(*args)
	if not result:
		return None
	return result
_BNCreateRepositoryManager = core.BNCreateRepositoryManager
_BNCreateRepositoryManager.restype = ctypes.POINTER(BNRepositoryManager)
_BNCreateRepositoryManager.argtypes = [
		ctypes.c_char_p,
	]
def BNCreateRepositoryManager(*args):
	result = _BNCreateRepositoryManager(*args)
	if not result:
		return None
	return result
_BNCreateScriptingProviderInstance = core.BNCreateScriptingProviderInstance
_BNCreateScriptingProviderInstance.restype = ctypes.POINTER(BNScriptingInstance)
_BNCreateScriptingProviderInstance.argtypes = [
		ctypes.POINTER(BNScriptingProvider),
	]
def BNCreateScriptingProviderInstance(*args):
	result = _BNCreateScriptingProviderInstance(*args)
	if not result:
		return None
	return result
_BNCreateStructure = core.BNCreateStructure
_BNCreateStructure.restype = ctypes.POINTER(BNStructure)
_BNCreateStructure.argtypes = [
	]
def BNCreateStructure(*args):
	result = _BNCreateStructure(*args)
	if not result:
		return None
	return result
_BNCreateStructureType = core.BNCreateStructureType
_BNCreateStructureType.restype = ctypes.POINTER(BNType)
_BNCreateStructureType.argtypes = [
		ctypes.POINTER(BNStructure),
	]
def BNCreateStructureType(*args):
	result = _BNCreateStructureType(*args)
	if not result:
		return None
	return result
_BNCreateStructureWithOptions = core.BNCreateStructureWithOptions
_BNCreateStructureWithOptions.restype = ctypes.POINTER(BNStructure)
_BNCreateStructureWithOptions.argtypes = [
		StructureTypeEnum,
		ctypes.c_bool,
	]
def BNCreateStructureWithOptions(*args):
	result = _BNCreateStructureWithOptions(*args)
	if not result:
		return None
	return result
_BNCreateSymbol = core.BNCreateSymbol
_BNCreateSymbol.restype = ctypes.POINTER(BNSymbol)
_BNCreateSymbol.argtypes = [
		SymbolTypeEnum,
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_ulonglong,
	]
def BNCreateSymbol(*args):
	result = _BNCreateSymbol(*args)
	if not result:
		return None
	return result
_BNCreateTemporaryFile = core.BNCreateTemporaryFile
_BNCreateTemporaryFile.restype = ctypes.POINTER(BNTemporaryFile)
_BNCreateTemporaryFile.argtypes = [
	]
def BNCreateTemporaryFile(*args):
	result = _BNCreateTemporaryFile(*args)
	if not result:
		return None
	return result
_BNCreateTemporaryFileWithContents = core.BNCreateTemporaryFileWithContents
_BNCreateTemporaryFileWithContents.restype = ctypes.POINTER(BNTemporaryFile)
_BNCreateTemporaryFileWithContents.argtypes = [
		ctypes.POINTER(BNDataBuffer),
	]
def BNCreateTemporaryFileWithContents(*args):
	result = _BNCreateTemporaryFileWithContents(*args)
	if not result:
		return None
	return result
BNCreateUserFunction = core.BNCreateUserFunction
BNCreateUserFunction.restype = None
BNCreateUserFunction.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNPlatform),
		ctypes.c_ulonglong,
	]
BNCreateUserStackVariable = core.BNCreateUserStackVariable
BNCreateUserStackVariable.restype = None
BNCreateUserStackVariable.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.c_longlong,
		ctypes.POINTER(BNTypeWithConfidence),
		ctypes.c_char_p,
	]
BNCreateUserVariable = core.BNCreateUserVariable
BNCreateUserVariable.restype = None
BNCreateUserVariable.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNVariable),
		ctypes.POINTER(BNTypeWithConfidence),
		ctypes.c_char_p,
		ctypes.c_bool,
	]
_BNCreateVoidType = core.BNCreateVoidType
_BNCreateVoidType.restype = ctypes.POINTER(BNType)
_BNCreateVoidType.argtypes = [
	]
def BNCreateVoidType(*args):
	result = _BNCreateVoidType(*args)
	if not result:
		return None
	return result
_BNDataBufferToBase64 = core.BNDataBufferToBase64
_BNDataBufferToBase64.restype = ctypes.POINTER(ctypes.c_byte)
_BNDataBufferToBase64.argtypes = [
		ctypes.POINTER(BNDataBuffer),
	]
def BNDataBufferToBase64(*args):
	result = _BNDataBufferToBase64(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNDataBufferToEscapedString = core.BNDataBufferToEscapedString
_BNDataBufferToEscapedString.restype = ctypes.POINTER(ctypes.c_byte)
_BNDataBufferToEscapedString.argtypes = [
		ctypes.POINTER(BNDataBuffer),
	]
def BNDataBufferToEscapedString(*args):
	result = _BNDataBufferToEscapedString(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNDecode = core.BNDecode
BNDecode.restype = ctypes.c_bool
BNDecode.argtypes = [
		ctypes.POINTER(BNTransform),
		ctypes.POINTER(BNDataBuffer),
		ctypes.POINTER(BNDataBuffer),
		ctypes.POINTER(BNTransformParameter),
		ctypes.c_ulonglong,
	]
_BNDecodeBase64 = core.BNDecodeBase64
_BNDecodeBase64.restype = ctypes.POINTER(BNDataBuffer)
_BNDecodeBase64.argtypes = [
		ctypes.c_char_p,
	]
def BNDecodeBase64(*args):
	result = _BNDecodeBase64(*args)
	if not result:
		return None
	return result
_BNDecodeEscapedString = core.BNDecodeEscapedString
_BNDecodeEscapedString.restype = ctypes.POINTER(BNDataBuffer)
_BNDecodeEscapedString.argtypes = [
		ctypes.c_char_p,
	]
def BNDecodeEscapedString(*args):
	result = _BNDecodeEscapedString(*args)
	if not result:
		return None
	return result
BNDefineAnalysisType = core.BNDefineAnalysisType
BNDefineAnalysisType.restype = BNQualifiedName
BNDefineAnalysisType.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
		ctypes.POINTER(BNQualifiedName),
		ctypes.POINTER(BNType),
	]
BNDefineAutoSymbol = core.BNDefineAutoSymbol
BNDefineAutoSymbol.restype = None
BNDefineAutoSymbol.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNSymbol),
	]
BNDefineAutoSymbolAndVariableOrFunction = core.BNDefineAutoSymbolAndVariableOrFunction
BNDefineAutoSymbolAndVariableOrFunction.restype = None
BNDefineAutoSymbolAndVariableOrFunction.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(BNSymbol),
		ctypes.POINTER(BNType),
	]
BNDefineDataVariable = core.BNDefineDataVariable
BNDefineDataVariable.restype = None
BNDefineDataVariable.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNTypeWithConfidence),
	]
BNDefineImportedFunction = core.BNDefineImportedFunction
BNDefineImportedFunction.restype = None
BNDefineImportedFunction.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNSymbol),
		ctypes.POINTER(BNFunction),
	]
BNDefineUserAnalysisType = core.BNDefineUserAnalysisType
BNDefineUserAnalysisType.restype = None
BNDefineUserAnalysisType.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNQualifiedName),
		ctypes.POINTER(BNType),
	]
BNDefineUserDataVariable = core.BNDefineUserDataVariable
BNDefineUserDataVariable.restype = None
BNDefineUserDataVariable.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNTypeWithConfidence),
	]
BNDefineUserSymbol = core.BNDefineUserSymbol
BNDefineUserSymbol.restype = None
BNDefineUserSymbol.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNSymbol),
	]
BNDeleteAutoStackVariable = core.BNDeleteAutoStackVariable
BNDeleteAutoStackVariable.restype = None
BNDeleteAutoStackVariable.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.c_longlong,
	]
BNDeleteAutoVariable = core.BNDeleteAutoVariable
BNDeleteAutoVariable.restype = None
BNDeleteAutoVariable.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNVariable),
	]
BNDeleteDirectory = core.BNDeleteDirectory
BNDeleteDirectory.restype = ctypes.c_int
BNDeleteDirectory.argtypes = [
		ctypes.c_char_p,
		ctypes.c_int,
	]
BNDeleteFile = core.BNDeleteFile
BNDeleteFile.restype = ctypes.c_int
BNDeleteFile.argtypes = [
		ctypes.c_char_p,
	]
BNDeleteUserStackVariable = core.BNDeleteUserStackVariable
BNDeleteUserStackVariable.restype = None
BNDeleteUserStackVariable.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.c_longlong,
	]
BNDeleteUserVariable = core.BNDeleteUserVariable
BNDeleteUserVariable.restype = None
BNDeleteUserVariable.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNVariable),
	]
BNDemangleGNU3 = core.BNDemangleGNU3
BNDemangleGNU3.restype = ctypes.c_bool
BNDemangleGNU3.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_char_p,
		ctypes.POINTER(ctypes.POINTER(BNType)),
		ctypes.POINTER(ctypes.POINTER(ctypes.c_char_p)),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
BNDemangleMS = core.BNDemangleMS
BNDemangleMS.restype = ctypes.c_bool
BNDemangleMS.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_char_p,
		ctypes.POINTER(ctypes.POINTER(BNType)),
		ctypes.POINTER(ctypes.POINTER(ctypes.c_char_p)),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
_BNDuplicateDataBuffer = core.BNDuplicateDataBuffer
_BNDuplicateDataBuffer.restype = ctypes.POINTER(BNDataBuffer)
_BNDuplicateDataBuffer.argtypes = [
		ctypes.POINTER(BNDataBuffer),
	]
def BNDuplicateDataBuffer(*args):
	result = _BNDuplicateDataBuffer(*args)
	if not result:
		return None
	return result
_BNDuplicateType = core.BNDuplicateType
_BNDuplicateType.restype = ctypes.POINTER(BNType)
_BNDuplicateType.argtypes = [
		ctypes.POINTER(BNType),
	]
def BNDuplicateType(*args):
	result = _BNDuplicateType(*args)
	if not result:
		return None
	return result
BNEncode = core.BNEncode
BNEncode.restype = ctypes.c_bool
BNEncode.argtypes = [
		ctypes.POINTER(BNTransform),
		ctypes.POINTER(BNDataBuffer),
		ctypes.POINTER(BNDataBuffer),
		ctypes.POINTER(BNTransformParameter),
		ctypes.c_ulonglong,
	]
BNExecuteMainThreadAction = core.BNExecuteMainThreadAction
BNExecuteMainThreadAction.restype = None
BNExecuteMainThreadAction.argtypes = [
		ctypes.POINTER(BNMainThreadAction),
	]
_BNExecuteOnMainThread = core.BNExecuteOnMainThread
_BNExecuteOnMainThread.restype = ctypes.POINTER(BNMainThreadAction)
_BNExecuteOnMainThread.argtypes = [
		ctypes.c_void_p,
		ctypes.CFUNCTYPE(None, ctypes.c_void_p),
	]
def BNExecuteOnMainThread(*args):
	result = _BNExecuteOnMainThread(*args)
	if not result:
		return None
	return result
BNExecuteOnMainThreadAndWait = core.BNExecuteOnMainThreadAndWait
BNExecuteOnMainThreadAndWait.restype = None
BNExecuteOnMainThreadAndWait.argtypes = [
		ctypes.c_void_p,
		ctypes.CFUNCTYPE(None, ctypes.c_void_p),
	]
BNExecuteScriptInput = core.BNExecuteScriptInput
BNExecuteScriptInput.restype = ScriptingProviderExecuteResultEnum
BNExecuteScriptInput.argtypes = [
		ctypes.POINTER(BNScriptingInstance),
		ctypes.c_char_p,
	]
BNExecuteWorkerProcess = core.BNExecuteWorkerProcess
BNExecuteWorkerProcess.restype = ctypes.c_bool
BNExecuteWorkerProcess.argtypes = [
		ctypes.c_char_p,
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.POINTER(BNDataBuffer),
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.c_bool,
		ctypes.c_bool,
	]
BNFinalizeLowLevelILFunction = core.BNFinalizeLowLevelILFunction
BNFinalizeLowLevelILFunction.restype = None
BNFinalizeLowLevelILFunction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
	]
BNFinalizeMediumLevelILFunction = core.BNFinalizeMediumLevelILFunction
BNFinalizeMediumLevelILFunction.restype = None
BNFinalizeMediumLevelILFunction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
	]
BNFindNextData = core.BNFindNextData
BNFindNextData.restype = ctypes.c_bool
BNFindNextData.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNDataBuffer),
		ctypes.POINTER(ctypes.c_ulonglong),
		FindFlagEnum,
	]
BNFinishBackgroundTask = core.BNFinishBackgroundTask
BNFinishBackgroundTask.restype = None
BNFinishBackgroundTask.argtypes = [
		ctypes.POINTER(BNBackgroundTask),
	]
BNFreeAddressList = core.BNFreeAddressList
BNFreeAddressList.restype = None
BNFreeAddressList.argtypes = [
		ctypes.POINTER(ctypes.c_ulonglong),
	]
BNFreeAddressRanges = core.BNFreeAddressRanges
BNFreeAddressRanges.restype = None
BNFreeAddressRanges.argtypes = [
		ctypes.POINTER(BNAddressRange),
	]
BNFreeAnalysisCompletionEvent = core.BNFreeAnalysisCompletionEvent
BNFreeAnalysisCompletionEvent.restype = None
BNFreeAnalysisCompletionEvent.argtypes = [
		ctypes.POINTER(BNAnalysisCompletionEvent),
	]
BNFreeAnalysisPerformanceInfo = core.BNFreeAnalysisPerformanceInfo
BNFreeAnalysisPerformanceInfo.restype = None
BNFreeAnalysisPerformanceInfo.argtypes = [
		ctypes.POINTER(BNPerformanceInfo),
		ctypes.c_ulonglong,
	]
BNFreeArchitectureList = core.BNFreeArchitectureList
BNFreeArchitectureList.restype = None
BNFreeArchitectureList.argtypes = [
		ctypes.POINTER(ctypes.POINTER(BNArchitecture)),
	]
BNFreeBackgroundTask = core.BNFreeBackgroundTask
BNFreeBackgroundTask.restype = None
BNFreeBackgroundTask.argtypes = [
		ctypes.POINTER(BNBackgroundTask),
	]
BNFreeBackgroundTaskList = core.BNFreeBackgroundTaskList
BNFreeBackgroundTaskList.restype = None
BNFreeBackgroundTaskList.argtypes = [
		ctypes.POINTER(ctypes.POINTER(BNBackgroundTask)),
		ctypes.c_ulonglong,
	]
BNFreeBasicBlock = core.BNFreeBasicBlock
BNFreeBasicBlock.restype = None
BNFreeBasicBlock.argtypes = [
		ctypes.POINTER(BNBasicBlock),
	]
BNFreeBasicBlockEdgeList = core.BNFreeBasicBlockEdgeList
BNFreeBasicBlockEdgeList.restype = None
BNFreeBasicBlockEdgeList.argtypes = [
		ctypes.POINTER(BNBasicBlockEdge),
		ctypes.c_ulonglong,
	]
BNFreeBasicBlockList = core.BNFreeBasicBlockList
BNFreeBasicBlockList.restype = None
BNFreeBasicBlockList.argtypes = [
		ctypes.POINTER(ctypes.POINTER(BNBasicBlock)),
		ctypes.c_ulonglong,
	]
BNFreeBinaryReader = core.BNFreeBinaryReader
BNFreeBinaryReader.restype = None
BNFreeBinaryReader.argtypes = [
		ctypes.POINTER(BNBinaryReader),
	]
BNFreeBinaryView = core.BNFreeBinaryView
BNFreeBinaryView.restype = None
BNFreeBinaryView.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
BNFreeBinaryViewTypeList = core.BNFreeBinaryViewTypeList
BNFreeBinaryViewTypeList.restype = None
BNFreeBinaryViewTypeList.argtypes = [
		ctypes.POINTER(ctypes.POINTER(BNBinaryViewType)),
	]
BNFreeBinaryWriter = core.BNFreeBinaryWriter
BNFreeBinaryWriter.restype = None
BNFreeBinaryWriter.argtypes = [
		ctypes.POINTER(BNBinaryWriter),
	]
BNFreeCallingConvention = core.BNFreeCallingConvention
BNFreeCallingConvention.restype = None
BNFreeCallingConvention.argtypes = [
		ctypes.POINTER(BNCallingConvention),
	]
BNFreeCallingConventionList = core.BNFreeCallingConventionList
BNFreeCallingConventionList.restype = None
BNFreeCallingConventionList.argtypes = [
		ctypes.POINTER(ctypes.POINTER(BNCallingConvention)),
		ctypes.c_ulonglong,
	]
BNFreeClobberedRegisters = core.BNFreeClobberedRegisters
BNFreeClobberedRegisters.restype = None
BNFreeClobberedRegisters.argtypes = [
		ctypes.POINTER(BNRegisterSetWithConfidence),
	]
BNFreeCodeReferences = core.BNFreeCodeReferences
BNFreeCodeReferences.restype = None
BNFreeCodeReferences.argtypes = [
		ctypes.POINTER(BNReferenceSource),
		ctypes.c_ulonglong,
	]
BNFreeConstantReferenceList = core.BNFreeConstantReferenceList
BNFreeConstantReferenceList.restype = None
BNFreeConstantReferenceList.argtypes = [
		ctypes.POINTER(BNConstantReference),
	]
BNFreeDataBuffer = core.BNFreeDataBuffer
BNFreeDataBuffer.restype = None
BNFreeDataBuffer.argtypes = [
		ctypes.POINTER(BNDataBuffer),
	]
BNFreeDataVariables = core.BNFreeDataVariables
BNFreeDataVariables.restype = None
BNFreeDataVariables.argtypes = [
		ctypes.POINTER(BNDataVariable),
		ctypes.c_ulonglong,
	]
BNFreeDemangledName = core.BNFreeDemangledName
BNFreeDemangledName.restype = None
BNFreeDemangledName.argtypes = [
		ctypes.POINTER(ctypes.POINTER(ctypes.c_char_p)),
		ctypes.c_ulonglong,
	]
BNFreeDisassemblySettings = core.BNFreeDisassemblySettings
BNFreeDisassemblySettings.restype = None
BNFreeDisassemblySettings.argtypes = [
		ctypes.POINTER(BNDisassemblySettings),
	]
BNFreeDisassemblyTextLines = core.BNFreeDisassemblyTextLines
BNFreeDisassemblyTextLines.restype = None
BNFreeDisassemblyTextLines.argtypes = [
		ctypes.POINTER(BNDisassemblyTextLine),
		ctypes.c_ulonglong,
	]
BNFreeEnumeration = core.BNFreeEnumeration
BNFreeEnumeration.restype = None
BNFreeEnumeration.argtypes = [
		ctypes.POINTER(BNEnumeration),
	]
BNFreeEnumerationMemberList = core.BNFreeEnumerationMemberList
BNFreeEnumerationMemberList.restype = None
BNFreeEnumerationMemberList.argtypes = [
		ctypes.POINTER(BNEnumerationMember),
		ctypes.c_ulonglong,
	]
BNFreeFileMetadata = core.BNFreeFileMetadata
BNFreeFileMetadata.restype = None
BNFreeFileMetadata.argtypes = [
		ctypes.POINTER(BNFileMetadata),
	]
BNFreeFormInputResults = core.BNFreeFormInputResults
BNFreeFormInputResults.restype = None
BNFreeFormInputResults.argtypes = [
		ctypes.POINTER(BNFormInputField),
		ctypes.c_ulonglong,
	]
BNFreeFunction = core.BNFreeFunction
BNFreeFunction.restype = None
BNFreeFunction.argtypes = [
		ctypes.POINTER(BNFunction),
	]
BNFreeFunctionGraph = core.BNFreeFunctionGraph
BNFreeFunctionGraph.restype = None
BNFreeFunctionGraph.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
	]
BNFreeFunctionGraphBlock = core.BNFreeFunctionGraphBlock
BNFreeFunctionGraphBlock.restype = None
BNFreeFunctionGraphBlock.argtypes = [
		ctypes.POINTER(BNFunctionGraphBlock),
	]
BNFreeFunctionGraphBlockList = core.BNFreeFunctionGraphBlockList
BNFreeFunctionGraphBlockList.restype = None
BNFreeFunctionGraphBlockList.argtypes = [
		ctypes.POINTER(ctypes.POINTER(BNFunctionGraphBlock)),
		ctypes.c_ulonglong,
	]
BNFreeFunctionGraphBlockOutgoingEdgeList = core.BNFreeFunctionGraphBlockOutgoingEdgeList
BNFreeFunctionGraphBlockOutgoingEdgeList.restype = None
BNFreeFunctionGraphBlockOutgoingEdgeList.argtypes = [
		ctypes.POINTER(BNFunctionGraphEdge),
		ctypes.c_ulonglong,
	]
BNFreeFunctionList = core.BNFreeFunctionList
BNFreeFunctionList.restype = None
BNFreeFunctionList.argtypes = [
		ctypes.POINTER(ctypes.POINTER(BNFunction)),
		ctypes.c_ulonglong,
	]
BNFreeILBranchDependenceList = core.BNFreeILBranchDependenceList
BNFreeILBranchDependenceList.restype = None
BNFreeILBranchDependenceList.argtypes = [
		ctypes.POINTER(BNILBranchInstructionAndDependence),
	]
BNFreeILInstructionList = core.BNFreeILInstructionList
BNFreeILInstructionList.restype = None
BNFreeILInstructionList.argtypes = [
		ctypes.POINTER(ctypes.c_ulonglong),
	]
BNFreeIndirectBranchList = core.BNFreeIndirectBranchList
BNFreeIndirectBranchList.restype = None
BNFreeIndirectBranchList.argtypes = [
		ctypes.POINTER(BNIndirectBranchInfo),
	]
BNFreeInstructionText = core.BNFreeInstructionText
BNFreeInstructionText.restype = None
BNFreeInstructionText.argtypes = [
		ctypes.POINTER(BNInstructionTextToken),
		ctypes.c_ulonglong,
	]
BNFreeInstructionTextLines = core.BNFreeInstructionTextLines
BNFreeInstructionTextLines.restype = None
BNFreeInstructionTextLines.argtypes = [
		ctypes.POINTER(BNInstructionTextLine),
		ctypes.c_ulonglong,
	]
BNFreeLinearDisassemblyLines = core.BNFreeLinearDisassemblyLines
BNFreeLinearDisassemblyLines.restype = None
BNFreeLinearDisassemblyLines.argtypes = [
		ctypes.POINTER(BNLinearDisassemblyLine),
		ctypes.c_ulonglong,
	]
BNFreeLinearDisassemblyPosition = core.BNFreeLinearDisassemblyPosition
BNFreeLinearDisassemblyPosition.restype = None
BNFreeLinearDisassemblyPosition.argtypes = [
		ctypes.POINTER(BNLinearDisassemblyPosition),
	]
BNFreeLowLevelILFunction = core.BNFreeLowLevelILFunction
BNFreeLowLevelILFunction.restype = None
BNFreeLowLevelILFunction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
	]
BNFreeMainThreadAction = core.BNFreeMainThreadAction
BNFreeMainThreadAction.restype = None
BNFreeMainThreadAction.argtypes = [
		ctypes.POINTER(BNMainThreadAction),
	]
BNFreeMediumLevelILFunction = core.BNFreeMediumLevelILFunction
BNFreeMediumLevelILFunction.restype = None
BNFreeMediumLevelILFunction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
	]
BNFreeMetadata = core.BNFreeMetadata
BNFreeMetadata.restype = None
BNFreeMetadata.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
BNFreeMetadataArray = core.BNFreeMetadataArray
BNFreeMetadataArray.restype = None
BNFreeMetadataArray.argtypes = [
		ctypes.POINTER(ctypes.POINTER(BNMetadata)),
	]
BNFreeMetadataRaw = core.BNFreeMetadataRaw
BNFreeMetadataRaw.restype = None
BNFreeMetadataRaw.argtypes = [
		ctypes.POINTER(ctypes.c_ubyte),
	]
BNFreeMetadataValueStore = core.BNFreeMetadataValueStore
BNFreeMetadataValueStore.restype = None
BNFreeMetadataValueStore.argtypes = [
		ctypes.POINTER(BNMetadataValueStore),
	]
BNFreeNamedTypeReference = core.BNFreeNamedTypeReference
BNFreeNamedTypeReference.restype = None
BNFreeNamedTypeReference.argtypes = [
		ctypes.POINTER(BNNamedTypeReference),
	]
BNFreeParameterVariables = core.BNFreeParameterVariables
BNFreeParameterVariables.restype = None
BNFreeParameterVariables.argtypes = [
		ctypes.POINTER(BNParameterVariablesWithConfidence),
	]
BNFreePlatform = core.BNFreePlatform
BNFreePlatform.restype = None
BNFreePlatform.argtypes = [
		ctypes.POINTER(BNPlatform),
	]
BNFreePlatformList = core.BNFreePlatformList
BNFreePlatformList.restype = None
BNFreePlatformList.argtypes = [
		ctypes.POINTER(ctypes.POINTER(BNPlatform)),
		ctypes.c_ulonglong,
	]
BNFreePlatformOSList = core.BNFreePlatformOSList
BNFreePlatformOSList.restype = None
BNFreePlatformOSList.argtypes = [
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.c_ulonglong,
	]
BNFreePlugin = core.BNFreePlugin
BNFreePlugin.restype = None
BNFreePlugin.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
BNFreePluginCommandList = core.BNFreePluginCommandList
BNFreePluginCommandList.restype = None
BNFreePluginCommandList.argtypes = [
		ctypes.POINTER(BNPluginCommand),
	]
BNFreePluginTypes = core.BNFreePluginTypes
BNFreePluginTypes.restype = None
BNFreePluginTypes.argtypes = [
		ctypes.POINTER(PluginTypeEnum),
	]
BNFreePossibleValueSet = core.BNFreePossibleValueSet
BNFreePossibleValueSet.restype = None
BNFreePossibleValueSet.argtypes = [
		ctypes.POINTER(BNPossibleValueSet),
	]
BNFreeQualifiedName = core.BNFreeQualifiedName
BNFreeQualifiedName.restype = None
BNFreeQualifiedName.argtypes = [
		ctypes.POINTER(BNQualifiedName),
	]
BNFreeQualifiedNameAndType = core.BNFreeQualifiedNameAndType
BNFreeQualifiedNameAndType.restype = None
BNFreeQualifiedNameAndType.argtypes = [
		ctypes.POINTER(BNQualifiedNameAndType),
	]
BNFreeRegisterList = core.BNFreeRegisterList
BNFreeRegisterList.restype = None
BNFreeRegisterList.argtypes = [
		ctypes.POINTER(ctypes.c_uint),
	]
BNFreeRepository = core.BNFreeRepository
BNFreeRepository.restype = None
BNFreeRepository.argtypes = [
		ctypes.POINTER(BNRepository),
	]
BNFreeRepositoryManager = core.BNFreeRepositoryManager
BNFreeRepositoryManager.restype = None
BNFreeRepositoryManager.argtypes = [
		ctypes.POINTER(BNRepositoryManager),
	]
BNFreeRepositoryManagerRepositoriesList = core.BNFreeRepositoryManagerRepositoriesList
BNFreeRepositoryManagerRepositoriesList.restype = None
BNFreeRepositoryManagerRepositoriesList.argtypes = [
		ctypes.POINTER(ctypes.POINTER(BNRepository)),
	]
BNFreeRepositoryPluginList = core.BNFreeRepositoryPluginList
BNFreeRepositoryPluginList.restype = None
BNFreeRepositoryPluginList.argtypes = [
		ctypes.POINTER(ctypes.POINTER(BNRepoPlugin)),
	]
BNFreeScriptingInstance = core.BNFreeScriptingInstance
BNFreeScriptingInstance.restype = None
BNFreeScriptingInstance.argtypes = [
		ctypes.POINTER(BNScriptingInstance),
	]
BNFreeScriptingProviderList = core.BNFreeScriptingProviderList
BNFreeScriptingProviderList.restype = None
BNFreeScriptingProviderList.argtypes = [
		ctypes.POINTER(ctypes.POINTER(BNScriptingProvider)),
	]
BNFreeSection = core.BNFreeSection
BNFreeSection.restype = None
BNFreeSection.argtypes = [
		ctypes.POINTER(BNSection),
	]
BNFreeSectionList = core.BNFreeSectionList
BNFreeSectionList.restype = None
BNFreeSectionList.argtypes = [
		ctypes.POINTER(BNSection),
		ctypes.c_ulonglong,
	]
BNFreeSegmentList = core.BNFreeSegmentList
BNFreeSegmentList.restype = None
BNFreeSegmentList.argtypes = [
		ctypes.POINTER(BNSegment),
	]
BNFreeSettingIntegerList = core.BNFreeSettingIntegerList
BNFreeSettingIntegerList.restype = None
BNFreeSettingIntegerList.argtypes = [
		ctypes.POINTER(ctypes.c_longlong),
	]
BNFreeStackVariableReferenceList = core.BNFreeStackVariableReferenceList
BNFreeStackVariableReferenceList.restype = None
BNFreeStackVariableReferenceList.argtypes = [
		ctypes.POINTER(BNStackVariableReference),
		ctypes.c_ulonglong,
	]
BNFreeString = core.BNFreeString
BNFreeString.restype = None
BNFreeString.argtypes = [
		ctypes.POINTER(ctypes.c_byte),
	]
BNFreeStringList = core.BNFreeStringList
BNFreeStringList.restype = None
BNFreeStringList.argtypes = [
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.c_ulonglong,
	]
BNFreeStringReferenceList = core.BNFreeStringReferenceList
BNFreeStringReferenceList.restype = None
BNFreeStringReferenceList.argtypes = [
		ctypes.POINTER(BNStringReference),
	]
BNFreeStructure = core.BNFreeStructure
BNFreeStructure.restype = None
BNFreeStructure.argtypes = [
		ctypes.POINTER(BNStructure),
	]
BNFreeStructureMemberList = core.BNFreeStructureMemberList
BNFreeStructureMemberList.restype = None
BNFreeStructureMemberList.argtypes = [
		ctypes.POINTER(BNStructureMember),
		ctypes.c_ulonglong,
	]
BNFreeSymbol = core.BNFreeSymbol
BNFreeSymbol.restype = None
BNFreeSymbol.argtypes = [
		ctypes.POINTER(BNSymbol),
	]
BNFreeSymbolList = core.BNFreeSymbolList
BNFreeSymbolList.restype = None
BNFreeSymbolList.argtypes = [
		ctypes.POINTER(ctypes.POINTER(BNSymbol)),
		ctypes.c_ulonglong,
	]
BNFreeSystemCallList = core.BNFreeSystemCallList
BNFreeSystemCallList.restype = None
BNFreeSystemCallList.argtypes = [
		ctypes.POINTER(BNSystemCallInfo),
		ctypes.c_ulonglong,
	]
BNFreeTemporaryFile = core.BNFreeTemporaryFile
BNFreeTemporaryFile.restype = None
BNFreeTemporaryFile.argtypes = [
		ctypes.POINTER(BNTemporaryFile),
	]
BNFreeTokenList = core.BNFreeTokenList
BNFreeTokenList.restype = None
BNFreeTokenList.argtypes = [
		ctypes.POINTER(BNInstructionTextToken),
		ctypes.c_ulonglong,
	]
BNFreeTransformParameterList = core.BNFreeTransformParameterList
BNFreeTransformParameterList.restype = None
BNFreeTransformParameterList.argtypes = [
		ctypes.POINTER(BNTransformParameterInfo),
		ctypes.c_ulonglong,
	]
BNFreeTransformTypeList = core.BNFreeTransformTypeList
BNFreeTransformTypeList.restype = None
BNFreeTransformTypeList.argtypes = [
		ctypes.POINTER(ctypes.POINTER(BNTransform)),
	]
BNFreeType = core.BNFreeType
BNFreeType.restype = None
BNFreeType.argtypes = [
		ctypes.POINTER(BNType),
	]
BNFreeTypeList = core.BNFreeTypeList
BNFreeTypeList.restype = None
BNFreeTypeList.argtypes = [
		ctypes.POINTER(BNQualifiedNameAndType),
		ctypes.c_ulonglong,
	]
BNFreeTypeParameterList = core.BNFreeTypeParameterList
BNFreeTypeParameterList.restype = None
BNFreeTypeParameterList.argtypes = [
		ctypes.POINTER(BNFunctionParameter),
		ctypes.c_ulonglong,
	]
BNFreeTypeParserResult = core.BNFreeTypeParserResult
BNFreeTypeParserResult.restype = None
BNFreeTypeParserResult.argtypes = [
		ctypes.POINTER(BNTypeParserResult),
	]
BNFreeUpdateChannelList = core.BNFreeUpdateChannelList
BNFreeUpdateChannelList.restype = None
BNFreeUpdateChannelList.argtypes = [
		ctypes.POINTER(BNUpdateChannel),
		ctypes.c_ulonglong,
	]
BNFreeUpdateChannelVersionList = core.BNFreeUpdateChannelVersionList
BNFreeUpdateChannelVersionList.restype = None
BNFreeUpdateChannelVersionList.argtypes = [
		ctypes.POINTER(BNUpdateVersion),
		ctypes.c_ulonglong,
	]
BNFreeVariableList = core.BNFreeVariableList
BNFreeVariableList.restype = None
BNFreeVariableList.argtypes = [
		ctypes.POINTER(BNVariableNameAndType),
		ctypes.c_ulonglong,
	]
BNFreeVariableNameAndType = core.BNFreeVariableNameAndType
BNFreeVariableNameAndType.restype = None
BNFreeVariableNameAndType.argtypes = [
		ctypes.POINTER(BNVariableNameAndType),
	]
BNFromVariableIdentifier = core.BNFromVariableIdentifier
BNFromVariableIdentifier.restype = BNVariable
BNFromVariableIdentifier.argtypes = [
		ctypes.c_ulonglong,
	]
BNFunctionHasExplicitlyDefinedType = core.BNFunctionHasExplicitlyDefinedType
BNFunctionHasExplicitlyDefinedType.restype = ctypes.c_bool
BNFunctionHasExplicitlyDefinedType.argtypes = [
		ctypes.POINTER(BNFunction),
	]
BNFunctionHasVariableArguments = core.BNFunctionHasVariableArguments
BNFunctionHasVariableArguments.restype = BNBoolWithConfidence
BNFunctionHasVariableArguments.argtypes = [
		ctypes.POINTER(BNFunction),
	]
BNFunctionTypeCanReturn = core.BNFunctionTypeCanReturn
BNFunctionTypeCanReturn.restype = BNBoolWithConfidence
BNFunctionTypeCanReturn.argtypes = [
		ctypes.POINTER(BNType),
	]
_BNGenerateAutoDebugTypeId = core.BNGenerateAutoDebugTypeId
_BNGenerateAutoDebugTypeId.restype = ctypes.POINTER(ctypes.c_byte)
_BNGenerateAutoDebugTypeId.argtypes = [
		ctypes.POINTER(BNQualifiedName),
	]
def BNGenerateAutoDebugTypeId(*args):
	result = _BNGenerateAutoDebugTypeId(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGenerateAutoDemangledTypeId = core.BNGenerateAutoDemangledTypeId
_BNGenerateAutoDemangledTypeId.restype = ctypes.POINTER(ctypes.c_byte)
_BNGenerateAutoDemangledTypeId.argtypes = [
		ctypes.POINTER(BNQualifiedName),
	]
def BNGenerateAutoDemangledTypeId(*args):
	result = _BNGenerateAutoDemangledTypeId(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGenerateAutoPlatformTypeId = core.BNGenerateAutoPlatformTypeId
_BNGenerateAutoPlatformTypeId.restype = ctypes.POINTER(ctypes.c_byte)
_BNGenerateAutoPlatformTypeId.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(BNQualifiedName),
	]
def BNGenerateAutoPlatformTypeId(*args):
	result = _BNGenerateAutoPlatformTypeId(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGenerateAutoTypeId = core.BNGenerateAutoTypeId
_BNGenerateAutoTypeId.restype = ctypes.POINTER(ctypes.c_byte)
_BNGenerateAutoTypeId.argtypes = [
		ctypes.c_char_p,
		ctypes.POINTER(BNQualifiedName),
	]
def BNGenerateAutoTypeId(*args):
	result = _BNGenerateAutoTypeId(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGenerateMediumLevelILSSAForm = core.BNGenerateMediumLevelILSSAForm
BNGenerateMediumLevelILSSAForm.restype = None
BNGenerateMediumLevelILSSAForm.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_bool,
		ctypes.c_bool,
		ctypes.POINTER(BNVariable),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNVariable),
		ctypes.c_ulonglong,
	]
_BNGetActiveUpdateChannel = core.BNGetActiveUpdateChannel
_BNGetActiveUpdateChannel.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetActiveUpdateChannel.argtypes = [
	]
def BNGetActiveUpdateChannel(*args):
	result = _BNGetActiveUpdateChannel(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGetAddressForDataOffset = core.BNGetAddressForDataOffset
BNGetAddressForDataOffset.restype = ctypes.c_bool
BNGetAddressForDataOffset.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
BNGetAddressInput = core.BNGetAddressInput
BNGetAddressInput.restype = ctypes.c_bool
BNGetAddressInput.argtypes = [
		ctypes.POINTER(ctypes.c_ulonglong),
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
_BNGetAllArchitectureFlagWriteTypes = core.BNGetAllArchitectureFlagWriteTypes
_BNGetAllArchitectureFlagWriteTypes.restype = ctypes.POINTER(ctypes.c_uint)
_BNGetAllArchitectureFlagWriteTypes.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetAllArchitectureFlagWriteTypes(*args):
	result = _BNGetAllArchitectureFlagWriteTypes(*args)
	if not result:
		return None
	return result
_BNGetAllArchitectureFlags = core.BNGetAllArchitectureFlags
_BNGetAllArchitectureFlags.restype = ctypes.POINTER(ctypes.c_uint)
_BNGetAllArchitectureFlags.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetAllArchitectureFlags(*args):
	result = _BNGetAllArchitectureFlags(*args)
	if not result:
		return None
	return result
_BNGetAllArchitectureRegisters = core.BNGetAllArchitectureRegisters
_BNGetAllArchitectureRegisters.restype = ctypes.POINTER(ctypes.c_uint)
_BNGetAllArchitectureRegisters.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetAllArchitectureRegisters(*args):
	result = _BNGetAllArchitectureRegisters(*args)
	if not result:
		return None
	return result
_BNGetAllMediumLevelILBranchDependence = core.BNGetAllMediumLevelILBranchDependence
_BNGetAllMediumLevelILBranchDependence.restype = ctypes.POINTER(BNILBranchInstructionAndDependence)
_BNGetAllMediumLevelILBranchDependence.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetAllMediumLevelILBranchDependence(*args):
	result = _BNGetAllMediumLevelILBranchDependence(*args)
	if not result:
		return None
	return result
_BNGetAllPluginCommands = core.BNGetAllPluginCommands
_BNGetAllPluginCommands.restype = ctypes.POINTER(BNPluginCommand)
_BNGetAllPluginCommands.argtypes = [
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetAllPluginCommands(*args):
	result = _BNGetAllPluginCommands(*args)
	if not result:
		return None
	return result
_BNGetAllocatedRanges = core.BNGetAllocatedRanges
_BNGetAllocatedRanges.restype = ctypes.POINTER(BNAddressRange)
_BNGetAllocatedRanges.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetAllocatedRanges(*args):
	result = _BNGetAllocatedRanges(*args)
	if not result:
		return None
	return result
_BNGetAnalysisEntryPoint = core.BNGetAnalysisEntryPoint
_BNGetAnalysisEntryPoint.restype = ctypes.POINTER(BNFunction)
_BNGetAnalysisEntryPoint.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
def BNGetAnalysisEntryPoint(*args):
	result = _BNGetAnalysisEntryPoint(*args)
	if not result:
		return None
	return result
_BNGetAnalysisFunction = core.BNGetAnalysisFunction
_BNGetAnalysisFunction.restype = ctypes.POINTER(BNFunction)
_BNGetAnalysisFunction.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNPlatform),
		ctypes.c_ulonglong,
	]
def BNGetAnalysisFunction(*args):
	result = _BNGetAnalysisFunction(*args)
	if not result:
		return None
	return result
_BNGetAnalysisFunctionList = core.BNGetAnalysisFunctionList
_BNGetAnalysisFunctionList.restype = ctypes.POINTER(ctypes.POINTER(BNFunction))
_BNGetAnalysisFunctionList.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetAnalysisFunctionList(*args):
	result = _BNGetAnalysisFunctionList(*args)
	if not result:
		return None
	return result
_BNGetAnalysisFunctionsForAddress = core.BNGetAnalysisFunctionsForAddress
_BNGetAnalysisFunctionsForAddress.restype = ctypes.POINTER(ctypes.POINTER(BNFunction))
_BNGetAnalysisFunctionsForAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetAnalysisFunctionsForAddress(*args):
	result = _BNGetAnalysisFunctionsForAddress(*args)
	if not result:
		return None
	return result
BNGetAnalysisProgress = core.BNGetAnalysisProgress
BNGetAnalysisProgress.restype = BNAnalysisProgress
BNGetAnalysisProgress.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
_BNGetAnalysisTypeById = core.BNGetAnalysisTypeById
_BNGetAnalysisTypeById.restype = ctypes.POINTER(BNType)
_BNGetAnalysisTypeById.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
	]
def BNGetAnalysisTypeById(*args):
	result = _BNGetAnalysisTypeById(*args)
	if not result:
		return None
	return result
_BNGetAnalysisTypeByName = core.BNGetAnalysisTypeByName
_BNGetAnalysisTypeByName.restype = ctypes.POINTER(BNType)
_BNGetAnalysisTypeByName.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNQualifiedName),
	]
def BNGetAnalysisTypeByName(*args):
	result = _BNGetAnalysisTypeByName(*args)
	if not result:
		return None
	return result
_BNGetAnalysisTypeId = core.BNGetAnalysisTypeId
_BNGetAnalysisTypeId.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetAnalysisTypeId.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNQualifiedName),
	]
def BNGetAnalysisTypeId(*args):
	result = _BNGetAnalysisTypeId(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetAnalysisTypeList = core.BNGetAnalysisTypeList
_BNGetAnalysisTypeList.restype = ctypes.POINTER(BNQualifiedNameAndType)
_BNGetAnalysisTypeList.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetAnalysisTypeList(*args):
	result = _BNGetAnalysisTypeList(*args)
	if not result:
		return None
	return result
BNGetAnalysisTypeNameById = core.BNGetAnalysisTypeNameById
BNGetAnalysisTypeNameById.restype = BNQualifiedName
BNGetAnalysisTypeNameById.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
	]
BNGetArchitectureAddressSize = core.BNGetArchitectureAddressSize
BNGetArchitectureAddressSize.restype = ctypes.c_ulonglong
BNGetArchitectureAddressSize.argtypes = [
		ctypes.POINTER(BNArchitecture),
	]
_BNGetArchitectureByName = core.BNGetArchitectureByName
_BNGetArchitectureByName.restype = ctypes.POINTER(BNArchitecture)
_BNGetArchitectureByName.argtypes = [
		ctypes.c_char_p,
	]
def BNGetArchitectureByName(*args):
	result = _BNGetArchitectureByName(*args)
	if not result:
		return None
	return result
_BNGetArchitectureCallingConventionByName = core.BNGetArchitectureCallingConventionByName
_BNGetArchitectureCallingConventionByName.restype = ctypes.POINTER(BNCallingConvention)
_BNGetArchitectureCallingConventionByName.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_char_p,
	]
def BNGetArchitectureCallingConventionByName(*args):
	result = _BNGetArchitectureCallingConventionByName(*args)
	if not result:
		return None
	return result
_BNGetArchitectureCallingConventions = core.BNGetArchitectureCallingConventions
_BNGetArchitectureCallingConventions.restype = ctypes.POINTER(ctypes.POINTER(BNCallingConvention))
_BNGetArchitectureCallingConventions.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetArchitectureCallingConventions(*args):
	result = _BNGetArchitectureCallingConventions(*args)
	if not result:
		return None
	return result
_BNGetArchitectureCdeclCallingConvention = core.BNGetArchitectureCdeclCallingConvention
_BNGetArchitectureCdeclCallingConvention.restype = ctypes.POINTER(BNCallingConvention)
_BNGetArchitectureCdeclCallingConvention.argtypes = [
		ctypes.POINTER(BNArchitecture),
	]
def BNGetArchitectureCdeclCallingConvention(*args):
	result = _BNGetArchitectureCdeclCallingConvention(*args)
	if not result:
		return None
	return result
_BNGetArchitectureDefaultCallingConvention = core.BNGetArchitectureDefaultCallingConvention
_BNGetArchitectureDefaultCallingConvention.restype = ctypes.POINTER(BNCallingConvention)
_BNGetArchitectureDefaultCallingConvention.argtypes = [
		ctypes.POINTER(BNArchitecture),
	]
def BNGetArchitectureDefaultCallingConvention(*args):
	result = _BNGetArchitectureDefaultCallingConvention(*args)
	if not result:
		return None
	return result
BNGetArchitectureDefaultIntegerSize = core.BNGetArchitectureDefaultIntegerSize
BNGetArchitectureDefaultIntegerSize.restype = ctypes.c_ulonglong
BNGetArchitectureDefaultIntegerSize.argtypes = [
		ctypes.POINTER(BNArchitecture),
	]
BNGetArchitectureEndianness = core.BNGetArchitectureEndianness
BNGetArchitectureEndianness.restype = EndiannessEnum
BNGetArchitectureEndianness.argtypes = [
		ctypes.POINTER(BNArchitecture),
	]
_BNGetArchitectureFastcallCallingConvention = core.BNGetArchitectureFastcallCallingConvention
_BNGetArchitectureFastcallCallingConvention.restype = ctypes.POINTER(BNCallingConvention)
_BNGetArchitectureFastcallCallingConvention.argtypes = [
		ctypes.POINTER(BNArchitecture),
	]
def BNGetArchitectureFastcallCallingConvention(*args):
	result = _BNGetArchitectureFastcallCallingConvention(*args)
	if not result:
		return None
	return result
BNGetArchitectureFlagConditionLowLevelIL = core.BNGetArchitectureFlagConditionLowLevelIL
BNGetArchitectureFlagConditionLowLevelIL.restype = ctypes.c_ulonglong
BNGetArchitectureFlagConditionLowLevelIL.argtypes = [
		ctypes.POINTER(BNArchitecture),
		LowLevelILFlagConditionEnum,
		ctypes.POINTER(BNLowLevelILFunction),
	]
_BNGetArchitectureFlagName = core.BNGetArchitectureFlagName
_BNGetArchitectureFlagName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetArchitectureFlagName.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_uint,
	]
def BNGetArchitectureFlagName(*args):
	result = _BNGetArchitectureFlagName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGetArchitectureFlagRole = core.BNGetArchitectureFlagRole
BNGetArchitectureFlagRole.restype = FlagRoleEnum
BNGetArchitectureFlagRole.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_uint,
	]
BNGetArchitectureFlagWriteLowLevelIL = core.BNGetArchitectureFlagWriteLowLevelIL
BNGetArchitectureFlagWriteLowLevelIL.restype = ctypes.c_ulonglong
BNGetArchitectureFlagWriteLowLevelIL.argtypes = [
		ctypes.POINTER(BNArchitecture),
		LowLevelILOperationEnum,
		ctypes.c_ulonglong,
		ctypes.c_uint,
		ctypes.c_uint,
		ctypes.POINTER(BNRegisterOrConstant),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNLowLevelILFunction),
	]
_BNGetArchitectureFlagWriteTypeName = core.BNGetArchitectureFlagWriteTypeName
_BNGetArchitectureFlagWriteTypeName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetArchitectureFlagWriteTypeName.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_uint,
	]
def BNGetArchitectureFlagWriteTypeName(*args):
	result = _BNGetArchitectureFlagWriteTypeName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetArchitectureFlagsRequiredForFlagCondition = core.BNGetArchitectureFlagsRequiredForFlagCondition
_BNGetArchitectureFlagsRequiredForFlagCondition.restype = ctypes.POINTER(ctypes.c_uint)
_BNGetArchitectureFlagsRequiredForFlagCondition.argtypes = [
		ctypes.POINTER(BNArchitecture),
		LowLevelILFlagConditionEnum,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetArchitectureFlagsRequiredForFlagCondition(*args):
	result = _BNGetArchitectureFlagsRequiredForFlagCondition(*args)
	if not result:
		return None
	return result
_BNGetArchitectureFlagsWrittenByFlagWriteType = core.BNGetArchitectureFlagsWrittenByFlagWriteType
_BNGetArchitectureFlagsWrittenByFlagWriteType.restype = ctypes.POINTER(ctypes.c_uint)
_BNGetArchitectureFlagsWrittenByFlagWriteType.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_uint,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetArchitectureFlagsWrittenByFlagWriteType(*args):
	result = _BNGetArchitectureFlagsWrittenByFlagWriteType(*args)
	if not result:
		return None
	return result
_BNGetArchitectureForViewType = core.BNGetArchitectureForViewType
_BNGetArchitectureForViewType.restype = ctypes.POINTER(BNArchitecture)
_BNGetArchitectureForViewType.argtypes = [
		ctypes.POINTER(BNBinaryViewType),
		ctypes.c_uint,
		EndiannessEnum,
	]
def BNGetArchitectureForViewType(*args):
	result = _BNGetArchitectureForViewType(*args)
	if not result:
		return None
	return result
_BNGetArchitectureGlobalRegisters = core.BNGetArchitectureGlobalRegisters
_BNGetArchitectureGlobalRegisters.restype = ctypes.POINTER(ctypes.c_uint)
_BNGetArchitectureGlobalRegisters.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetArchitectureGlobalRegisters(*args):
	result = _BNGetArchitectureGlobalRegisters(*args)
	if not result:
		return None
	return result
BNGetArchitectureLinkRegister = core.BNGetArchitectureLinkRegister
BNGetArchitectureLinkRegister.restype = ctypes.c_uint
BNGetArchitectureLinkRegister.argtypes = [
		ctypes.POINTER(BNArchitecture),
	]
_BNGetArchitectureList = core.BNGetArchitectureList
_BNGetArchitectureList.restype = ctypes.POINTER(ctypes.POINTER(BNArchitecture))
_BNGetArchitectureList.argtypes = [
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetArchitectureList(*args):
	result = _BNGetArchitectureList(*args)
	if not result:
		return None
	return result
BNGetArchitectureMaxInstructionLength = core.BNGetArchitectureMaxInstructionLength
BNGetArchitectureMaxInstructionLength.restype = ctypes.c_ulonglong
BNGetArchitectureMaxInstructionLength.argtypes = [
		ctypes.POINTER(BNArchitecture),
	]
_BNGetArchitectureName = core.BNGetArchitectureName
_BNGetArchitectureName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetArchitectureName.argtypes = [
		ctypes.POINTER(BNArchitecture),
	]
def BNGetArchitectureName(*args):
	result = _BNGetArchitectureName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGetArchitectureOpcodeDisplayLength = core.BNGetArchitectureOpcodeDisplayLength
BNGetArchitectureOpcodeDisplayLength.restype = ctypes.c_ulonglong
BNGetArchitectureOpcodeDisplayLength.argtypes = [
		ctypes.POINTER(BNArchitecture),
	]
BNGetArchitectureRegisterByName = core.BNGetArchitectureRegisterByName
BNGetArchitectureRegisterByName.restype = ctypes.c_uint
BNGetArchitectureRegisterByName.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_char_p,
	]
BNGetArchitectureRegisterInfo = core.BNGetArchitectureRegisterInfo
BNGetArchitectureRegisterInfo.restype = BNRegisterInfo
BNGetArchitectureRegisterInfo.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_uint,
	]
_BNGetArchitectureRegisterName = core.BNGetArchitectureRegisterName
_BNGetArchitectureRegisterName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetArchitectureRegisterName.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_uint,
	]
def BNGetArchitectureRegisterName(*args):
	result = _BNGetArchitectureRegisterName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGetArchitectureStackPointerRegister = core.BNGetArchitectureStackPointerRegister
BNGetArchitectureStackPointerRegister.restype = ctypes.c_uint
BNGetArchitectureStackPointerRegister.argtypes = [
		ctypes.POINTER(BNArchitecture),
	]
_BNGetArchitectureStandalonePlatform = core.BNGetArchitectureStandalonePlatform
_BNGetArchitectureStandalonePlatform.restype = ctypes.POINTER(BNPlatform)
_BNGetArchitectureStandalonePlatform.argtypes = [
		ctypes.POINTER(BNArchitecture),
	]
def BNGetArchitectureStandalonePlatform(*args):
	result = _BNGetArchitectureStandalonePlatform(*args)
	if not result:
		return None
	return result
_BNGetArchitectureStdcallCallingConvention = core.BNGetArchitectureStdcallCallingConvention
_BNGetArchitectureStdcallCallingConvention.restype = ctypes.POINTER(BNCallingConvention)
_BNGetArchitectureStdcallCallingConvention.argtypes = [
		ctypes.POINTER(BNArchitecture),
	]
def BNGetArchitectureStdcallCallingConvention(*args):
	result = _BNGetArchitectureStdcallCallingConvention(*args)
	if not result:
		return None
	return result
_BNGetAssociatedArchitectureByAddress = core.BNGetAssociatedArchitectureByAddress
_BNGetAssociatedArchitectureByAddress.restype = ctypes.POINTER(BNArchitecture)
_BNGetAssociatedArchitectureByAddress.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetAssociatedArchitectureByAddress(*args):
	result = _BNGetAssociatedArchitectureByAddress(*args)
	if not result:
		return None
	return result
_BNGetAssociatedPlatformByAddress = core.BNGetAssociatedPlatformByAddress
_BNGetAssociatedPlatformByAddress.restype = ctypes.POINTER(BNPlatform)
_BNGetAssociatedPlatformByAddress.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetAssociatedPlatformByAddress(*args):
	result = _BNGetAssociatedPlatformByAddress(*args)
	if not result:
		return None
	return result
_BNGetAutoDebugTypeIdSource = core.BNGetAutoDebugTypeIdSource
_BNGetAutoDebugTypeIdSource.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetAutoDebugTypeIdSource.argtypes = [
	]
def BNGetAutoDebugTypeIdSource(*args):
	result = _BNGetAutoDebugTypeIdSource(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetAutoDemangledTypeIdSource = core.BNGetAutoDemangledTypeIdSource
_BNGetAutoDemangledTypeIdSource.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetAutoDemangledTypeIdSource.argtypes = [
	]
def BNGetAutoDemangledTypeIdSource(*args):
	result = _BNGetAutoDemangledTypeIdSource(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetAutoPlatformTypeIdSource = core.BNGetAutoPlatformTypeIdSource
_BNGetAutoPlatformTypeIdSource.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetAutoPlatformTypeIdSource.argtypes = [
		ctypes.POINTER(BNPlatform),
	]
def BNGetAutoPlatformTypeIdSource(*args):
	result = _BNGetAutoPlatformTypeIdSource(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetBackgroundTaskProgressText = core.BNGetBackgroundTaskProgressText
_BNGetBackgroundTaskProgressText.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetBackgroundTaskProgressText.argtypes = [
		ctypes.POINTER(BNBackgroundTask),
	]
def BNGetBackgroundTaskProgressText(*args):
	result = _BNGetBackgroundTaskProgressText(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetBasicBlockArchitecture = core.BNGetBasicBlockArchitecture
_BNGetBasicBlockArchitecture.restype = ctypes.POINTER(BNArchitecture)
_BNGetBasicBlockArchitecture.argtypes = [
		ctypes.POINTER(BNBasicBlock),
	]
def BNGetBasicBlockArchitecture(*args):
	result = _BNGetBasicBlockArchitecture(*args)
	if not result:
		return None
	return result
_BNGetBasicBlockDisassemblyText = core.BNGetBasicBlockDisassemblyText
_BNGetBasicBlockDisassemblyText.restype = ctypes.POINTER(BNDisassemblyTextLine)
_BNGetBasicBlockDisassemblyText.argtypes = [
		ctypes.POINTER(BNBasicBlock),
		ctypes.POINTER(BNDisassemblySettings),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetBasicBlockDisassemblyText(*args):
	result = _BNGetBasicBlockDisassemblyText(*args)
	if not result:
		return None
	return result
_BNGetBasicBlockDominanceFrontier = core.BNGetBasicBlockDominanceFrontier
_BNGetBasicBlockDominanceFrontier.restype = ctypes.POINTER(ctypes.POINTER(BNBasicBlock))
_BNGetBasicBlockDominanceFrontier.argtypes = [
		ctypes.POINTER(BNBasicBlock),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetBasicBlockDominanceFrontier(*args):
	result = _BNGetBasicBlockDominanceFrontier(*args)
	if not result:
		return None
	return result
_BNGetBasicBlockDominatorTreeChildren = core.BNGetBasicBlockDominatorTreeChildren
_BNGetBasicBlockDominatorTreeChildren.restype = ctypes.POINTER(ctypes.POINTER(BNBasicBlock))
_BNGetBasicBlockDominatorTreeChildren.argtypes = [
		ctypes.POINTER(BNBasicBlock),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetBasicBlockDominatorTreeChildren(*args):
	result = _BNGetBasicBlockDominatorTreeChildren(*args)
	if not result:
		return None
	return result
_BNGetBasicBlockDominators = core.BNGetBasicBlockDominators
_BNGetBasicBlockDominators.restype = ctypes.POINTER(ctypes.POINTER(BNBasicBlock))
_BNGetBasicBlockDominators.argtypes = [
		ctypes.POINTER(BNBasicBlock),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetBasicBlockDominators(*args):
	result = _BNGetBasicBlockDominators(*args)
	if not result:
		return None
	return result
BNGetBasicBlockEnd = core.BNGetBasicBlockEnd
BNGetBasicBlockEnd.restype = ctypes.c_ulonglong
BNGetBasicBlockEnd.argtypes = [
		ctypes.POINTER(BNBasicBlock),
	]
_BNGetBasicBlockFunction = core.BNGetBasicBlockFunction
_BNGetBasicBlockFunction.restype = ctypes.POINTER(BNFunction)
_BNGetBasicBlockFunction.argtypes = [
		ctypes.POINTER(BNBasicBlock),
	]
def BNGetBasicBlockFunction(*args):
	result = _BNGetBasicBlockFunction(*args)
	if not result:
		return None
	return result
BNGetBasicBlockHighlight = core.BNGetBasicBlockHighlight
BNGetBasicBlockHighlight.restype = BNHighlightColor
BNGetBasicBlockHighlight.argtypes = [
		ctypes.POINTER(BNBasicBlock),
	]
_BNGetBasicBlockImmediateDominator = core.BNGetBasicBlockImmediateDominator
_BNGetBasicBlockImmediateDominator.restype = ctypes.POINTER(BNBasicBlock)
_BNGetBasicBlockImmediateDominator.argtypes = [
		ctypes.POINTER(BNBasicBlock),
	]
def BNGetBasicBlockImmediateDominator(*args):
	result = _BNGetBasicBlockImmediateDominator(*args)
	if not result:
		return None
	return result
_BNGetBasicBlockIncomingEdges = core.BNGetBasicBlockIncomingEdges
_BNGetBasicBlockIncomingEdges.restype = ctypes.POINTER(BNBasicBlockEdge)
_BNGetBasicBlockIncomingEdges.argtypes = [
		ctypes.POINTER(BNBasicBlock),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetBasicBlockIncomingEdges(*args):
	result = _BNGetBasicBlockIncomingEdges(*args)
	if not result:
		return None
	return result
BNGetBasicBlockIndex = core.BNGetBasicBlockIndex
BNGetBasicBlockIndex.restype = ctypes.c_ulonglong
BNGetBasicBlockIndex.argtypes = [
		ctypes.POINTER(BNBasicBlock),
	]
_BNGetBasicBlockIteratedDominanceFrontier = core.BNGetBasicBlockIteratedDominanceFrontier
_BNGetBasicBlockIteratedDominanceFrontier.restype = ctypes.POINTER(ctypes.POINTER(BNBasicBlock))
_BNGetBasicBlockIteratedDominanceFrontier.argtypes = [
		ctypes.POINTER(ctypes.POINTER(BNBasicBlock)),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetBasicBlockIteratedDominanceFrontier(*args):
	result = _BNGetBasicBlockIteratedDominanceFrontier(*args)
	if not result:
		return None
	return result
BNGetBasicBlockLength = core.BNGetBasicBlockLength
BNGetBasicBlockLength.restype = ctypes.c_ulonglong
BNGetBasicBlockLength.argtypes = [
		ctypes.POINTER(BNBasicBlock),
	]
_BNGetBasicBlockOutgoingEdges = core.BNGetBasicBlockOutgoingEdges
_BNGetBasicBlockOutgoingEdges.restype = ctypes.POINTER(BNBasicBlockEdge)
_BNGetBasicBlockOutgoingEdges.argtypes = [
		ctypes.POINTER(BNBasicBlock),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetBasicBlockOutgoingEdges(*args):
	result = _BNGetBasicBlockOutgoingEdges(*args)
	if not result:
		return None
	return result
BNGetBasicBlockStart = core.BNGetBasicBlockStart
BNGetBasicBlockStart.restype = ctypes.c_ulonglong
BNGetBasicBlockStart.argtypes = [
		ctypes.POINTER(BNBasicBlock),
	]
_BNGetBasicBlockStrictDominators = core.BNGetBasicBlockStrictDominators
_BNGetBasicBlockStrictDominators.restype = ctypes.POINTER(ctypes.POINTER(BNBasicBlock))
_BNGetBasicBlockStrictDominators.argtypes = [
		ctypes.POINTER(BNBasicBlock),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetBasicBlockStrictDominators(*args):
	result = _BNGetBasicBlockStrictDominators(*args)
	if not result:
		return None
	return result
_BNGetBasicBlocksForAddress = core.BNGetBasicBlocksForAddress
_BNGetBasicBlocksForAddress.restype = ctypes.POINTER(ctypes.POINTER(BNBasicBlock))
_BNGetBasicBlocksForAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetBasicBlocksForAddress(*args):
	result = _BNGetBasicBlocksForAddress(*args)
	if not result:
		return None
	return result
_BNGetBasicBlocksStartingAtAddress = core.BNGetBasicBlocksStartingAtAddress
_BNGetBasicBlocksStartingAtAddress.restype = ctypes.POINTER(ctypes.POINTER(BNBasicBlock))
_BNGetBasicBlocksStartingAtAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetBasicBlocksStartingAtAddress(*args):
	result = _BNGetBasicBlocksStartingAtAddress(*args)
	if not result:
		return None
	return result
BNGetBinaryReaderEndianness = core.BNGetBinaryReaderEndianness
BNGetBinaryReaderEndianness.restype = EndiannessEnum
BNGetBinaryReaderEndianness.argtypes = [
		ctypes.POINTER(BNBinaryReader),
	]
BNGetBinaryViewTypeArchitectureConstant = core.BNGetBinaryViewTypeArchitectureConstant
BNGetBinaryViewTypeArchitectureConstant.restype = ctypes.c_ulonglong
BNGetBinaryViewTypeArchitectureConstant.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_ulonglong,
	]
_BNGetBinaryViewTypeByName = core.BNGetBinaryViewTypeByName
_BNGetBinaryViewTypeByName.restype = ctypes.POINTER(BNBinaryViewType)
_BNGetBinaryViewTypeByName.argtypes = [
		ctypes.c_char_p,
	]
def BNGetBinaryViewTypeByName(*args):
	result = _BNGetBinaryViewTypeByName(*args)
	if not result:
		return None
	return result
_BNGetBinaryViewTypeLongName = core.BNGetBinaryViewTypeLongName
_BNGetBinaryViewTypeLongName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetBinaryViewTypeLongName.argtypes = [
		ctypes.POINTER(BNBinaryViewType),
	]
def BNGetBinaryViewTypeLongName(*args):
	result = _BNGetBinaryViewTypeLongName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetBinaryViewTypeName = core.BNGetBinaryViewTypeName
_BNGetBinaryViewTypeName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetBinaryViewTypeName.argtypes = [
		ctypes.POINTER(BNBinaryViewType),
	]
def BNGetBinaryViewTypeName(*args):
	result = _BNGetBinaryViewTypeName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetBinaryViewTypes = core.BNGetBinaryViewTypes
_BNGetBinaryViewTypes.restype = ctypes.POINTER(ctypes.POINTER(BNBinaryViewType))
_BNGetBinaryViewTypes.argtypes = [
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetBinaryViewTypes(*args):
	result = _BNGetBinaryViewTypes(*args)
	if not result:
		return None
	return result
_BNGetBinaryViewTypesForData = core.BNGetBinaryViewTypesForData
_BNGetBinaryViewTypesForData.restype = ctypes.POINTER(ctypes.POINTER(BNBinaryViewType))
_BNGetBinaryViewTypesForData.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetBinaryViewTypesForData(*args):
	result = _BNGetBinaryViewTypesForData(*args)
	if not result:
		return None
	return result
BNGetBinaryWriterEndianness = core.BNGetBinaryWriterEndianness
BNGetBinaryWriterEndianness.restype = EndiannessEnum
BNGetBinaryWriterEndianness.argtypes = [
		ctypes.POINTER(BNBinaryWriter),
	]
BNGetBuildId = core.BNGetBuildId
BNGetBuildId.restype = ctypes.c_uint
BNGetBuildId.argtypes = [
	]
_BNGetBundledPluginDirectory = core.BNGetBundledPluginDirectory
_BNGetBundledPluginDirectory.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetBundledPluginDirectory.argtypes = [
	]
def BNGetBundledPluginDirectory(*args):
	result = _BNGetBundledPluginDirectory(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetCallerSavedRegisters = core.BNGetCallerSavedRegisters
_BNGetCallerSavedRegisters.restype = ctypes.POINTER(ctypes.c_uint)
_BNGetCallerSavedRegisters.argtypes = [
		ctypes.POINTER(BNCallingConvention),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetCallerSavedRegisters(*args):
	result = _BNGetCallerSavedRegisters(*args)
	if not result:
		return None
	return result
_BNGetCallingConventionArchitecture = core.BNGetCallingConventionArchitecture
_BNGetCallingConventionArchitecture.restype = ctypes.POINTER(BNArchitecture)
_BNGetCallingConventionArchitecture.argtypes = [
		ctypes.POINTER(BNCallingConvention),
	]
def BNGetCallingConventionArchitecture(*args):
	result = _BNGetCallingConventionArchitecture(*args)
	if not result:
		return None
	return result
_BNGetCallingConventionName = core.BNGetCallingConventionName
_BNGetCallingConventionName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetCallingConventionName.argtypes = [
		ctypes.POINTER(BNCallingConvention),
	]
def BNGetCallingConventionName(*args):
	result = _BNGetCallingConventionName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGetChildType = core.BNGetChildType
BNGetChildType.restype = BNTypeWithConfidence
BNGetChildType.argtypes = [
		ctypes.POINTER(BNType),
	]
BNGetChoiceInput = core.BNGetChoiceInput
BNGetChoiceInput.restype = ctypes.c_bool
BNGetChoiceInput.argtypes = [
		ctypes.POINTER(ctypes.c_ulonglong),
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.c_ulonglong,
	]
_BNGetCodeReferences = core.BNGetCodeReferences
_BNGetCodeReferences.restype = ctypes.POINTER(BNReferenceSource)
_BNGetCodeReferences.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetCodeReferences(*args):
	result = _BNGetCodeReferences(*args)
	if not result:
		return None
	return result
_BNGetCodeReferencesInRange = core.BNGetCodeReferencesInRange
_BNGetCodeReferencesInRange.restype = ctypes.POINTER(BNReferenceSource)
_BNGetCodeReferencesInRange.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetCodeReferencesInRange(*args):
	result = _BNGetCodeReferencesInRange(*args)
	if not result:
		return None
	return result
_BNGetCommentForAddress = core.BNGetCommentForAddress
_BNGetCommentForAddress.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetCommentForAddress.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.c_ulonglong,
	]
def BNGetCommentForAddress(*args):
	result = _BNGetCommentForAddress(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetCommentedAddresses = core.BNGetCommentedAddresses
_BNGetCommentedAddresses.restype = ctypes.POINTER(ctypes.c_ulonglong)
_BNGetCommentedAddresses.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetCommentedAddresses(*args):
	result = _BNGetCommentedAddresses(*args)
	if not result:
		return None
	return result
_BNGetConstantsReferencedByInstruction = core.BNGetConstantsReferencedByInstruction
_BNGetConstantsReferencedByInstruction.restype = ctypes.POINTER(BNConstantReference)
_BNGetConstantsReferencedByInstruction.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetConstantsReferencedByInstruction(*args):
	result = _BNGetConstantsReferencedByInstruction(*args)
	if not result:
		return None
	return result
BNGetCurrentOffset = core.BNGetCurrentOffset
BNGetCurrentOffset.restype = ctypes.c_ulonglong
BNGetCurrentOffset.argtypes = [
		ctypes.POINTER(BNFileMetadata),
	]
_BNGetCurrentView = core.BNGetCurrentView
_BNGetCurrentView.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetCurrentView.argtypes = [
		ctypes.POINTER(BNFileMetadata),
	]
def BNGetCurrentView(*args):
	result = _BNGetCurrentView(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGetDataBufferByte = core.BNGetDataBufferByte
BNGetDataBufferByte.restype = ctypes.c_ubyte
BNGetDataBufferByte.argtypes = [
		ctypes.POINTER(BNDataBuffer),
		ctypes.c_ulonglong,
	]
_BNGetDataBufferContents = core.BNGetDataBufferContents
_BNGetDataBufferContents.restype = ctypes.c_void_p
_BNGetDataBufferContents.argtypes = [
		ctypes.POINTER(BNDataBuffer),
	]
def BNGetDataBufferContents(*args):
	result = _BNGetDataBufferContents(*args)
	if not result:
		return None
	return result
_BNGetDataBufferContentsAt = core.BNGetDataBufferContentsAt
_BNGetDataBufferContentsAt.restype = ctypes.c_void_p
_BNGetDataBufferContentsAt.argtypes = [
		ctypes.POINTER(BNDataBuffer),
		ctypes.c_ulonglong,
	]
def BNGetDataBufferContentsAt(*args):
	result = _BNGetDataBufferContentsAt(*args)
	if not result:
		return None
	return result
BNGetDataBufferLength = core.BNGetDataBufferLength
BNGetDataBufferLength.restype = ctypes.c_ulonglong
BNGetDataBufferLength.argtypes = [
		ctypes.POINTER(BNDataBuffer),
	]
_BNGetDataBufferSlice = core.BNGetDataBufferSlice
_BNGetDataBufferSlice.restype = ctypes.POINTER(BNDataBuffer)
_BNGetDataBufferSlice.argtypes = [
		ctypes.POINTER(BNDataBuffer),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
def BNGetDataBufferSlice(*args):
	result = _BNGetDataBufferSlice(*args)
	if not result:
		return None
	return result
BNGetDataVariableAtAddress = core.BNGetDataVariableAtAddress
BNGetDataVariableAtAddress.restype = ctypes.c_bool
BNGetDataVariableAtAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNDataVariable),
	]
_BNGetDataVariables = core.BNGetDataVariables
_BNGetDataVariables.restype = ctypes.POINTER(BNDataVariable)
_BNGetDataVariables.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetDataVariables(*args):
	result = _BNGetDataVariables(*args)
	if not result:
		return None
	return result
_BNGetDefaultArchitecture = core.BNGetDefaultArchitecture
_BNGetDefaultArchitecture.restype = ctypes.POINTER(BNArchitecture)
_BNGetDefaultArchitecture.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
def BNGetDefaultArchitecture(*args):
	result = _BNGetDefaultArchitecture(*args)
	if not result:
		return None
	return result
BNGetDefaultArchitectureFlagConditionLowLevelIL = core.BNGetDefaultArchitectureFlagConditionLowLevelIL
BNGetDefaultArchitectureFlagConditionLowLevelIL.restype = ctypes.c_ulonglong
BNGetDefaultArchitectureFlagConditionLowLevelIL.argtypes = [
		ctypes.POINTER(BNArchitecture),
		LowLevelILFlagConditionEnum,
		ctypes.POINTER(BNLowLevelILFunction),
	]
BNGetDefaultArchitectureFlagWriteLowLevelIL = core.BNGetDefaultArchitectureFlagWriteLowLevelIL
BNGetDefaultArchitectureFlagWriteLowLevelIL.restype = ctypes.c_ulonglong
BNGetDefaultArchitectureFlagWriteLowLevelIL.argtypes = [
		ctypes.POINTER(BNArchitecture),
		LowLevelILOperationEnum,
		ctypes.c_ulonglong,
		FlagRoleEnum,
		ctypes.POINTER(BNRegisterOrConstant),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNLowLevelILFunction),
	]
BNGetDefaultEndianness = core.BNGetDefaultEndianness
BNGetDefaultEndianness.restype = EndiannessEnum
BNGetDefaultEndianness.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
_BNGetDefaultPlatform = core.BNGetDefaultPlatform
_BNGetDefaultPlatform.restype = ctypes.POINTER(BNPlatform)
_BNGetDefaultPlatform.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
def BNGetDefaultPlatform(*args):
	result = _BNGetDefaultPlatform(*args)
	if not result:
		return None
	return result
BNGetDirectoryNameInput = core.BNGetDirectoryNameInput
BNGetDirectoryNameInput.restype = ctypes.c_bool
BNGetDirectoryNameInput.argtypes = [
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNGetDisassemblyMaximumSymbolWidth = core.BNGetDisassemblyMaximumSymbolWidth
BNGetDisassemblyMaximumSymbolWidth.restype = ctypes.c_ulonglong
BNGetDisassemblyMaximumSymbolWidth.argtypes = [
		ctypes.POINTER(BNDisassemblySettings),
	]
BNGetDisassemblyWidth = core.BNGetDisassemblyWidth
BNGetDisassemblyWidth.restype = ctypes.c_ulonglong
BNGetDisassemblyWidth.argtypes = [
		ctypes.POINTER(BNDisassemblySettings),
	]
BNGetEndOffset = core.BNGetEndOffset
BNGetEndOffset.restype = ctypes.c_ulonglong
BNGetEndOffset.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
BNGetEntryPoint = core.BNGetEntryPoint
BNGetEntryPoint.restype = ctypes.c_ulonglong
BNGetEntryPoint.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
_BNGetEnumerationMembers = core.BNGetEnumerationMembers
_BNGetEnumerationMembers.restype = ctypes.POINTER(BNEnumerationMember)
_BNGetEnumerationMembers.argtypes = [
		ctypes.POINTER(BNEnumeration),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetEnumerationMembers(*args):
	result = _BNGetEnumerationMembers(*args)
	if not result:
		return None
	return result
_BNGetFileForView = core.BNGetFileForView
_BNGetFileForView.restype = ctypes.POINTER(BNFileMetadata)
_BNGetFileForView.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
def BNGetFileForView(*args):
	result = _BNGetFileForView(*args)
	if not result:
		return None
	return result
_BNGetFileViewOfType = core.BNGetFileViewOfType
_BNGetFileViewOfType.restype = ctypes.POINTER(BNBinaryView)
_BNGetFileViewOfType.argtypes = [
		ctypes.POINTER(BNFileMetadata),
		ctypes.c_char_p,
	]
def BNGetFileViewOfType(*args):
	result = _BNGetFileViewOfType(*args)
	if not result:
		return None
	return result
_BNGetFilename = core.BNGetFilename
_BNGetFilename.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetFilename.argtypes = [
		ctypes.POINTER(BNFileMetadata),
	]
def BNGetFilename(*args):
	result = _BNGetFilename(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetFlagsReadByLiftedILInstruction = core.BNGetFlagsReadByLiftedILInstruction
_BNGetFlagsReadByLiftedILInstruction.restype = ctypes.POINTER(ctypes.c_uint)
_BNGetFlagsReadByLiftedILInstruction.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetFlagsReadByLiftedILInstruction(*args):
	result = _BNGetFlagsReadByLiftedILInstruction(*args)
	if not result:
		return None
	return result
_BNGetFlagsWrittenByLiftedILInstruction = core.BNGetFlagsWrittenByLiftedILInstruction
_BNGetFlagsWrittenByLiftedILInstruction.restype = ctypes.POINTER(ctypes.c_uint)
_BNGetFlagsWrittenByLiftedILInstruction.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetFlagsWrittenByLiftedILInstruction(*args):
	result = _BNGetFlagsWrittenByLiftedILInstruction(*args)
	if not result:
		return None
	return result
_BNGetFloatArgumentRegisters = core.BNGetFloatArgumentRegisters
_BNGetFloatArgumentRegisters.restype = ctypes.POINTER(ctypes.c_uint)
_BNGetFloatArgumentRegisters.argtypes = [
		ctypes.POINTER(BNCallingConvention),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetFloatArgumentRegisters(*args):
	result = _BNGetFloatArgumentRegisters(*args)
	if not result:
		return None
	return result
BNGetFloatReturnValueRegister = core.BNGetFloatReturnValueRegister
BNGetFloatReturnValueRegister.restype = ctypes.c_uint
BNGetFloatReturnValueRegister.argtypes = [
		ctypes.POINTER(BNCallingConvention),
	]
BNGetFormInput = core.BNGetFormInput
BNGetFormInput.restype = ctypes.c_bool
BNGetFormInput.argtypes = [
		ctypes.POINTER(BNFormInputField),
		ctypes.c_ulonglong,
		ctypes.c_char_p,
	]
_BNGetFullWidthArchitectureRegisters = core.BNGetFullWidthArchitectureRegisters
_BNGetFullWidthArchitectureRegisters.restype = ctypes.POINTER(ctypes.c_uint)
_BNGetFullWidthArchitectureRegisters.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetFullWidthArchitectureRegisters(*args):
	result = _BNGetFullWidthArchitectureRegisters(*args)
	if not result:
		return None
	return result
_BNGetFunctionAnalysisPerformanceInfo = core.BNGetFunctionAnalysisPerformanceInfo
_BNGetFunctionAnalysisPerformanceInfo.restype = ctypes.POINTER(BNPerformanceInfo)
_BNGetFunctionAnalysisPerformanceInfo.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetFunctionAnalysisPerformanceInfo(*args):
	result = _BNGetFunctionAnalysisPerformanceInfo(*args)
	if not result:
		return None
	return result
_BNGetFunctionArchitecture = core.BNGetFunctionArchitecture
_BNGetFunctionArchitecture.restype = ctypes.POINTER(BNArchitecture)
_BNGetFunctionArchitecture.argtypes = [
		ctypes.POINTER(BNFunction),
	]
def BNGetFunctionArchitecture(*args):
	result = _BNGetFunctionArchitecture(*args)
	if not result:
		return None
	return result
_BNGetFunctionBasicBlockAtAddress = core.BNGetFunctionBasicBlockAtAddress
_BNGetFunctionBasicBlockAtAddress.restype = ctypes.POINTER(BNBasicBlock)
_BNGetFunctionBasicBlockAtAddress.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
def BNGetFunctionBasicBlockAtAddress(*args):
	result = _BNGetFunctionBasicBlockAtAddress(*args)
	if not result:
		return None
	return result
_BNGetFunctionBasicBlockList = core.BNGetFunctionBasicBlockList
_BNGetFunctionBasicBlockList.restype = ctypes.POINTER(ctypes.POINTER(BNBasicBlock))
_BNGetFunctionBasicBlockList.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetFunctionBasicBlockList(*args):
	result = _BNGetFunctionBasicBlockList(*args)
	if not result:
		return None
	return result
_BNGetFunctionBlockAnnotations = core.BNGetFunctionBlockAnnotations
_BNGetFunctionBlockAnnotations.restype = ctypes.POINTER(BNInstructionTextLine)
_BNGetFunctionBlockAnnotations.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetFunctionBlockAnnotations(*args):
	result = _BNGetFunctionBlockAnnotations(*args)
	if not result:
		return None
	return result
BNGetFunctionCallingConvention = core.BNGetFunctionCallingConvention
BNGetFunctionCallingConvention.restype = BNCallingConventionWithConfidence
BNGetFunctionCallingConvention.argtypes = [
		ctypes.POINTER(BNFunction),
	]
BNGetFunctionClobberedRegisters = core.BNGetFunctionClobberedRegisters
BNGetFunctionClobberedRegisters.restype = BNRegisterSetWithConfidence
BNGetFunctionClobberedRegisters.argtypes = [
		ctypes.POINTER(BNFunction),
	]
_BNGetFunctionComment = core.BNGetFunctionComment
_BNGetFunctionComment.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetFunctionComment.argtypes = [
		ctypes.POINTER(BNFunction),
	]
def BNGetFunctionComment(*args):
	result = _BNGetFunctionComment(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetFunctionData = core.BNGetFunctionData
_BNGetFunctionData.restype = ctypes.POINTER(BNBinaryView)
_BNGetFunctionData.argtypes = [
		ctypes.POINTER(BNFunction),
	]
def BNGetFunctionData(*args):
	result = _BNGetFunctionData(*args)
	if not result:
		return None
	return result
_BNGetFunctionForFunctionGraph = core.BNGetFunctionForFunctionGraph
_BNGetFunctionForFunctionGraph.restype = ctypes.POINTER(BNFunction)
_BNGetFunctionForFunctionGraph.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
	]
def BNGetFunctionForFunctionGraph(*args):
	result = _BNGetFunctionForFunctionGraph(*args)
	if not result:
		return None
	return result
BNGetFunctionGlobalPointerValue = core.BNGetFunctionGlobalPointerValue
BNGetFunctionGlobalPointerValue.restype = BNRegisterValueWithConfidence
BNGetFunctionGlobalPointerValue.argtypes = [
		ctypes.POINTER(BNFunction),
	]
_BNGetFunctionGraphBasicBlock = core.BNGetFunctionGraphBasicBlock
_BNGetFunctionGraphBasicBlock.restype = ctypes.POINTER(BNBasicBlock)
_BNGetFunctionGraphBasicBlock.argtypes = [
		ctypes.POINTER(BNFunctionGraphBlock),
	]
def BNGetFunctionGraphBasicBlock(*args):
	result = _BNGetFunctionGraphBasicBlock(*args)
	if not result:
		return None
	return result
_BNGetFunctionGraphBlockArchitecture = core.BNGetFunctionGraphBlockArchitecture
_BNGetFunctionGraphBlockArchitecture.restype = ctypes.POINTER(BNArchitecture)
_BNGetFunctionGraphBlockArchitecture.argtypes = [
		ctypes.POINTER(BNFunctionGraphBlock),
	]
def BNGetFunctionGraphBlockArchitecture(*args):
	result = _BNGetFunctionGraphBlockArchitecture(*args)
	if not result:
		return None
	return result
BNGetFunctionGraphBlockEnd = core.BNGetFunctionGraphBlockEnd
BNGetFunctionGraphBlockEnd.restype = ctypes.c_ulonglong
BNGetFunctionGraphBlockEnd.argtypes = [
		ctypes.POINTER(BNFunctionGraphBlock),
	]
BNGetFunctionGraphBlockHeight = core.BNGetFunctionGraphBlockHeight
BNGetFunctionGraphBlockHeight.restype = ctypes.c_int
BNGetFunctionGraphBlockHeight.argtypes = [
		ctypes.POINTER(BNFunctionGraphBlock),
	]
_BNGetFunctionGraphBlockLines = core.BNGetFunctionGraphBlockLines
_BNGetFunctionGraphBlockLines.restype = ctypes.POINTER(BNDisassemblyTextLine)
_BNGetFunctionGraphBlockLines.argtypes = [
		ctypes.POINTER(BNFunctionGraphBlock),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetFunctionGraphBlockLines(*args):
	result = _BNGetFunctionGraphBlockLines(*args)
	if not result:
		return None
	return result
_BNGetFunctionGraphBlockOutgoingEdges = core.BNGetFunctionGraphBlockOutgoingEdges
_BNGetFunctionGraphBlockOutgoingEdges.restype = ctypes.POINTER(BNFunctionGraphEdge)
_BNGetFunctionGraphBlockOutgoingEdges.argtypes = [
		ctypes.POINTER(BNFunctionGraphBlock),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetFunctionGraphBlockOutgoingEdges(*args):
	result = _BNGetFunctionGraphBlockOutgoingEdges(*args)
	if not result:
		return None
	return result
BNGetFunctionGraphBlockStart = core.BNGetFunctionGraphBlockStart
BNGetFunctionGraphBlockStart.restype = ctypes.c_ulonglong
BNGetFunctionGraphBlockStart.argtypes = [
		ctypes.POINTER(BNFunctionGraphBlock),
	]
BNGetFunctionGraphBlockWidth = core.BNGetFunctionGraphBlockWidth
BNGetFunctionGraphBlockWidth.restype = ctypes.c_int
BNGetFunctionGraphBlockWidth.argtypes = [
		ctypes.POINTER(BNFunctionGraphBlock),
	]
BNGetFunctionGraphBlockX = core.BNGetFunctionGraphBlockX
BNGetFunctionGraphBlockX.restype = ctypes.c_int
BNGetFunctionGraphBlockX.argtypes = [
		ctypes.POINTER(BNFunctionGraphBlock),
	]
BNGetFunctionGraphBlockY = core.BNGetFunctionGraphBlockY
BNGetFunctionGraphBlockY.restype = ctypes.c_int
BNGetFunctionGraphBlockY.argtypes = [
		ctypes.POINTER(BNFunctionGraphBlock),
	]
_BNGetFunctionGraphBlocks = core.BNGetFunctionGraphBlocks
_BNGetFunctionGraphBlocks.restype = ctypes.POINTER(ctypes.POINTER(BNFunctionGraphBlock))
_BNGetFunctionGraphBlocks.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetFunctionGraphBlocks(*args):
	result = _BNGetFunctionGraphBlocks(*args)
	if not result:
		return None
	return result
_BNGetFunctionGraphBlocksInRegion = core.BNGetFunctionGraphBlocksInRegion
_BNGetFunctionGraphBlocksInRegion.restype = ctypes.POINTER(ctypes.POINTER(BNFunctionGraphBlock))
_BNGetFunctionGraphBlocksInRegion.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
		ctypes.c_int,
		ctypes.c_int,
		ctypes.c_int,
		ctypes.c_int,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetFunctionGraphBlocksInRegion(*args):
	result = _BNGetFunctionGraphBlocksInRegion(*args)
	if not result:
		return None
	return result
BNGetFunctionGraphHeight = core.BNGetFunctionGraphHeight
BNGetFunctionGraphHeight.restype = ctypes.c_int
BNGetFunctionGraphHeight.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
	]
_BNGetFunctionGraphSettings = core.BNGetFunctionGraphSettings
_BNGetFunctionGraphSettings.restype = ctypes.POINTER(BNDisassemblySettings)
_BNGetFunctionGraphSettings.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
	]
def BNGetFunctionGraphSettings(*args):
	result = _BNGetFunctionGraphSettings(*args)
	if not result:
		return None
	return result
BNGetFunctionGraphType = core.BNGetFunctionGraphType
BNGetFunctionGraphType.restype = FunctionGraphTypeEnum
BNGetFunctionGraphType.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
	]
BNGetFunctionGraphWidth = core.BNGetFunctionGraphWidth
BNGetFunctionGraphWidth.restype = ctypes.c_int
BNGetFunctionGraphWidth.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
	]
_BNGetFunctionLiftedIL = core.BNGetFunctionLiftedIL
_BNGetFunctionLiftedIL.restype = ctypes.POINTER(BNLowLevelILFunction)
_BNGetFunctionLiftedIL.argtypes = [
		ctypes.POINTER(BNFunction),
	]
def BNGetFunctionLiftedIL(*args):
	result = _BNGetFunctionLiftedIL(*args)
	if not result:
		return None
	return result
_BNGetFunctionLowLevelIL = core.BNGetFunctionLowLevelIL
_BNGetFunctionLowLevelIL.restype = ctypes.POINTER(BNLowLevelILFunction)
_BNGetFunctionLowLevelIL.argtypes = [
		ctypes.POINTER(BNFunction),
	]
def BNGetFunctionLowLevelIL(*args):
	result = _BNGetFunctionLowLevelIL(*args)
	if not result:
		return None
	return result
_BNGetFunctionMediumLevelIL = core.BNGetFunctionMediumLevelIL
_BNGetFunctionMediumLevelIL.restype = ctypes.POINTER(BNMediumLevelILFunction)
_BNGetFunctionMediumLevelIL.argtypes = [
		ctypes.POINTER(BNFunction),
	]
def BNGetFunctionMediumLevelIL(*args):
	result = _BNGetFunctionMediumLevelIL(*args)
	if not result:
		return None
	return result
BNGetFunctionParameterVariables = core.BNGetFunctionParameterVariables
BNGetFunctionParameterVariables.restype = BNParameterVariablesWithConfidence
BNGetFunctionParameterVariables.argtypes = [
		ctypes.POINTER(BNFunction),
	]
_BNGetFunctionPlatform = core.BNGetFunctionPlatform
_BNGetFunctionPlatform.restype = ctypes.POINTER(BNPlatform)
_BNGetFunctionPlatform.argtypes = [
		ctypes.POINTER(BNFunction),
	]
def BNGetFunctionPlatform(*args):
	result = _BNGetFunctionPlatform(*args)
	if not result:
		return None
	return result
BNGetFunctionRegisterValueAtExit = core.BNGetFunctionRegisterValueAtExit
BNGetFunctionRegisterValueAtExit.restype = BNRegisterValueWithConfidence
BNGetFunctionRegisterValueAtExit.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.c_uint,
	]
BNGetFunctionReturnType = core.BNGetFunctionReturnType
BNGetFunctionReturnType.restype = BNTypeWithConfidence
BNGetFunctionReturnType.argtypes = [
		ctypes.POINTER(BNFunction),
	]
BNGetFunctionStackAdjustment = core.BNGetFunctionStackAdjustment
BNGetFunctionStackAdjustment.restype = BNSizeWithConfidence
BNGetFunctionStackAdjustment.argtypes = [
		ctypes.POINTER(BNFunction),
	]
BNGetFunctionStart = core.BNGetFunctionStart
BNGetFunctionStart.restype = ctypes.c_ulonglong
BNGetFunctionStart.argtypes = [
		ctypes.POINTER(BNFunction),
	]
_BNGetFunctionSymbol = core.BNGetFunctionSymbol
_BNGetFunctionSymbol.restype = ctypes.POINTER(BNSymbol)
_BNGetFunctionSymbol.argtypes = [
		ctypes.POINTER(BNFunction),
	]
def BNGetFunctionSymbol(*args):
	result = _BNGetFunctionSymbol(*args)
	if not result:
		return None
	return result
_BNGetFunctionType = core.BNGetFunctionType
_BNGetFunctionType.restype = ctypes.POINTER(BNType)
_BNGetFunctionType.argtypes = [
		ctypes.POINTER(BNFunction),
	]
def BNGetFunctionType(*args):
	result = _BNGetFunctionType(*args)
	if not result:
		return None
	return result
_BNGetFunctionTypeTokens = core.BNGetFunctionTypeTokens
_BNGetFunctionTypeTokens.restype = ctypes.POINTER(BNDisassemblyTextLine)
_BNGetFunctionTypeTokens.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNDisassemblySettings),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetFunctionTypeTokens(*args):
	result = _BNGetFunctionTypeTokens(*args)
	if not result:
		return None
	return result
_BNGetFunctionVariables = core.BNGetFunctionVariables
_BNGetFunctionVariables.restype = ctypes.POINTER(BNVariableNameAndType)
_BNGetFunctionVariables.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetFunctionVariables(*args):
	result = _BNGetFunctionVariables(*args)
	if not result:
		return None
	return result
BNGetGlobalPointerRegister = core.BNGetGlobalPointerRegister
BNGetGlobalPointerRegister.restype = ctypes.c_uint
BNGetGlobalPointerRegister.argtypes = [
		ctypes.POINTER(BNCallingConvention),
	]
BNGetGlobalPointerValue = core.BNGetGlobalPointerValue
BNGetGlobalPointerValue.restype = BNRegisterValueWithConfidence
BNGetGlobalPointerValue.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
BNGetHighIntegerReturnValueRegister = core.BNGetHighIntegerReturnValueRegister
BNGetHighIntegerReturnValueRegister.restype = ctypes.c_uint
BNGetHighIntegerReturnValueRegister.argtypes = [
		ctypes.POINTER(BNCallingConvention),
	]
BNGetHorizontalFunctionGraphBlockMargin = core.BNGetHorizontalFunctionGraphBlockMargin
BNGetHorizontalFunctionGraphBlockMargin.restype = ctypes.c_int
BNGetHorizontalFunctionGraphBlockMargin.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
	]
_BNGetImplicitlyDefinedRegisters = core.BNGetImplicitlyDefinedRegisters
_BNGetImplicitlyDefinedRegisters.restype = ctypes.POINTER(ctypes.c_uint)
_BNGetImplicitlyDefinedRegisters.argtypes = [
		ctypes.POINTER(BNCallingConvention),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetImplicitlyDefinedRegisters(*args):
	result = _BNGetImplicitlyDefinedRegisters(*args)
	if not result:
		return None
	return result
BNGetIncomingFlagValue = core.BNGetIncomingFlagValue
BNGetIncomingFlagValue.restype = BNRegisterValue
BNGetIncomingFlagValue.argtypes = [
		ctypes.POINTER(BNCallingConvention),
		ctypes.c_uint,
		ctypes.POINTER(BNFunction),
	]
BNGetIncomingRegisterValue = core.BNGetIncomingRegisterValue
BNGetIncomingRegisterValue.restype = BNRegisterValue
BNGetIncomingRegisterValue.argtypes = [
		ctypes.POINTER(BNCallingConvention),
		ctypes.c_uint,
		ctypes.POINTER(BNFunction),
	]
_BNGetIndirectBranches = core.BNGetIndirectBranches
_BNGetIndirectBranches.restype = ctypes.POINTER(BNIndirectBranchInfo)
_BNGetIndirectBranches.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetIndirectBranches(*args):
	result = _BNGetIndirectBranches(*args)
	if not result:
		return None
	return result
_BNGetIndirectBranchesAt = core.BNGetIndirectBranchesAt
_BNGetIndirectBranchesAt.restype = ctypes.POINTER(BNIndirectBranchInfo)
_BNGetIndirectBranchesAt.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetIndirectBranchesAt(*args):
	result = _BNGetIndirectBranchesAt(*args)
	if not result:
		return None
	return result
_BNGetInstallDirectory = core.BNGetInstallDirectory
_BNGetInstallDirectory.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetInstallDirectory.argtypes = [
	]
def BNGetInstallDirectory(*args):
	result = _BNGetInstallDirectory(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGetInstructionHighlight = core.BNGetInstructionHighlight
BNGetInstructionHighlight.restype = BNHighlightColor
BNGetInstructionHighlight.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
BNGetInstructionInfo = core.BNGetInstructionInfo
BNGetInstructionInfo.restype = ctypes.c_bool
BNGetInstructionInfo.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ubyte),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.POINTER(BNInstructionInfo),
	]
BNGetInstructionLength = core.BNGetInstructionLength
BNGetInstructionLength.restype = ctypes.c_ulonglong
BNGetInstructionLength.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
BNGetInstructionLowLevelIL = core.BNGetInstructionLowLevelIL
BNGetInstructionLowLevelIL.restype = ctypes.c_bool
BNGetInstructionLowLevelIL.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ubyte),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
		ctypes.POINTER(BNLowLevelILFunction),
	]
BNGetInstructionText = core.BNGetInstructionText
BNGetInstructionText.restype = ctypes.c_bool
BNGetInstructionText.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ubyte),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
		ctypes.POINTER(ctypes.POINTER(BNInstructionTextToken)),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
_BNGetIntegerArgumentRegisters = core.BNGetIntegerArgumentRegisters
_BNGetIntegerArgumentRegisters.restype = ctypes.POINTER(ctypes.c_uint)
_BNGetIntegerArgumentRegisters.argtypes = [
		ctypes.POINTER(BNCallingConvention),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetIntegerArgumentRegisters(*args):
	result = _BNGetIntegerArgumentRegisters(*args)
	if not result:
		return None
	return result
BNGetIntegerConstantDisplayType = core.BNGetIntegerConstantDisplayType
BNGetIntegerConstantDisplayType.restype = IntegerDisplayTypeEnum
BNGetIntegerConstantDisplayType.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNGetIntegerInput = core.BNGetIntegerInput
BNGetIntegerInput.restype = ctypes.c_bool
BNGetIntegerInput.argtypes = [
		ctypes.POINTER(ctypes.c_longlong),
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNGetIntegerReturnValueRegister = core.BNGetIntegerReturnValueRegister
BNGetIntegerReturnValueRegister.restype = ctypes.c_uint
BNGetIntegerReturnValueRegister.argtypes = [
		ctypes.POINTER(BNCallingConvention),
	]
_BNGetLabelForLowLevelILSourceInstruction = core.BNGetLabelForLowLevelILSourceInstruction
_BNGetLabelForLowLevelILSourceInstruction.restype = ctypes.POINTER(BNLowLevelILLabel)
_BNGetLabelForLowLevelILSourceInstruction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
	]
def BNGetLabelForLowLevelILSourceInstruction(*args):
	result = _BNGetLabelForLowLevelILSourceInstruction(*args)
	if not result:
		return None
	return result
_BNGetLabelForMediumLevelILSourceInstruction = core.BNGetLabelForMediumLevelILSourceInstruction
_BNGetLabelForMediumLevelILSourceInstruction.restype = ctypes.POINTER(BNMediumLevelILLabel)
_BNGetLabelForMediumLevelILSourceInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
	]
def BNGetLabelForMediumLevelILSourceInstruction(*args):
	result = _BNGetLabelForMediumLevelILSourceInstruction(*args)
	if not result:
		return None
	return result
BNGetLicenseCount = core.BNGetLicenseCount
BNGetLicenseCount.restype = ctypes.c_int
BNGetLicenseCount.argtypes = [
	]
_BNGetLiftedILFlagDefinitionsForUse = core.BNGetLiftedILFlagDefinitionsForUse
_BNGetLiftedILFlagDefinitionsForUse.restype = ctypes.POINTER(ctypes.c_ulonglong)
_BNGetLiftedILFlagDefinitionsForUse.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.c_ulonglong,
		ctypes.c_uint,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetLiftedILFlagDefinitionsForUse(*args):
	result = _BNGetLiftedILFlagDefinitionsForUse(*args)
	if not result:
		return None
	return result
_BNGetLiftedILFlagUsesForDefinition = core.BNGetLiftedILFlagUsesForDefinition
_BNGetLiftedILFlagUsesForDefinition.restype = ctypes.POINTER(ctypes.c_ulonglong)
_BNGetLiftedILFlagUsesForDefinition.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.c_ulonglong,
		ctypes.c_uint,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetLiftedILFlagUsesForDefinition(*args):
	result = _BNGetLiftedILFlagUsesForDefinition(*args)
	if not result:
		return None
	return result
BNGetLiftedILForInstruction = core.BNGetLiftedILForInstruction
BNGetLiftedILForInstruction.restype = ctypes.c_ulonglong
BNGetLiftedILForInstruction.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
BNGetLinearDisassemblyPositionForAddress = core.BNGetLinearDisassemblyPositionForAddress
BNGetLinearDisassemblyPositionForAddress.restype = BNLinearDisassemblyPosition
BNGetLinearDisassemblyPositionForAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNDisassemblySettings),
	]
_BNGetLowLevelILBasicBlockList = core.BNGetLowLevelILBasicBlockList
_BNGetLowLevelILBasicBlockList.restype = ctypes.POINTER(ctypes.POINTER(BNBasicBlock))
_BNGetLowLevelILBasicBlockList.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetLowLevelILBasicBlockList(*args):
	result = _BNGetLowLevelILBasicBlockList(*args)
	if not result:
		return None
	return result
BNGetLowLevelILByIndex = core.BNGetLowLevelILByIndex
BNGetLowLevelILByIndex.restype = BNLowLevelILInstruction
BNGetLowLevelILByIndex.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
	]
_BNGetLowLevelILExitsForInstruction = core.BNGetLowLevelILExitsForInstruction
_BNGetLowLevelILExitsForInstruction.restype = ctypes.POINTER(ctypes.c_ulonglong)
_BNGetLowLevelILExitsForInstruction.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetLowLevelILExitsForInstruction(*args):
	result = _BNGetLowLevelILExitsForInstruction(*args)
	if not result:
		return None
	return result
BNGetLowLevelILExprCount = core.BNGetLowLevelILExprCount
BNGetLowLevelILExprCount.restype = ctypes.c_ulonglong
BNGetLowLevelILExprCount.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
	]
BNGetLowLevelILExprIndex = core.BNGetLowLevelILExprIndex
BNGetLowLevelILExprIndex.restype = ctypes.c_ulonglong
BNGetLowLevelILExprIndex.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetLowLevelILExprText = core.BNGetLowLevelILExprText
BNGetLowLevelILExprText.restype = ctypes.c_bool
BNGetLowLevelILExprText.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.POINTER(BNInstructionTextToken)),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
BNGetLowLevelILExprValue = core.BNGetLowLevelILExprValue
BNGetLowLevelILExprValue.restype = BNRegisterValue
BNGetLowLevelILExprValue.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetLowLevelILFlagValueAfterInstruction = core.BNGetLowLevelILFlagValueAfterInstruction
BNGetLowLevelILFlagValueAfterInstruction.restype = BNRegisterValue
BNGetLowLevelILFlagValueAfterInstruction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetLowLevelILFlagValueAtInstruction = core.BNGetLowLevelILFlagValueAtInstruction
BNGetLowLevelILFlagValueAtInstruction.restype = BNRegisterValue
BNGetLowLevelILFlagValueAtInstruction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetLowLevelILForInstruction = core.BNGetLowLevelILForInstruction
BNGetLowLevelILForInstruction.restype = ctypes.c_ulonglong
BNGetLowLevelILForInstruction.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
_BNGetLowLevelILForMediumLevelIL = core.BNGetLowLevelILForMediumLevelIL
_BNGetLowLevelILForMediumLevelIL.restype = ctypes.POINTER(BNLowLevelILFunction)
_BNGetLowLevelILForMediumLevelIL.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
	]
def BNGetLowLevelILForMediumLevelIL(*args):
	result = _BNGetLowLevelILForMediumLevelIL(*args)
	if not result:
		return None
	return result
BNGetLowLevelILIndexForInstruction = core.BNGetLowLevelILIndexForInstruction
BNGetLowLevelILIndexForInstruction.restype = ctypes.c_ulonglong
BNGetLowLevelILIndexForInstruction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetLowLevelILInstructionCount = core.BNGetLowLevelILInstructionCount
BNGetLowLevelILInstructionCount.restype = ctypes.c_ulonglong
BNGetLowLevelILInstructionCount.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
	]
BNGetLowLevelILInstructionForExpr = core.BNGetLowLevelILInstructionForExpr
BNGetLowLevelILInstructionForExpr.restype = ctypes.c_ulonglong
BNGetLowLevelILInstructionForExpr.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetLowLevelILInstructionIndex = core.BNGetLowLevelILInstructionIndex
BNGetLowLevelILInstructionIndex.restype = ctypes.c_ulonglong
BNGetLowLevelILInstructionIndex.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetLowLevelILInstructionText = core.BNGetLowLevelILInstructionText
BNGetLowLevelILInstructionText.restype = ctypes.c_bool
BNGetLowLevelILInstructionText.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.POINTER(BNInstructionTextToken)),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
_BNGetLowLevelILLabelForAddress = core.BNGetLowLevelILLabelForAddress
_BNGetLowLevelILLabelForAddress.restype = ctypes.POINTER(BNLowLevelILLabel)
_BNGetLowLevelILLabelForAddress.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
def BNGetLowLevelILLabelForAddress(*args):
	result = _BNGetLowLevelILLabelForAddress(*args)
	if not result:
		return None
	return result
BNGetLowLevelILNonSSAExprIndex = core.BNGetLowLevelILNonSSAExprIndex
BNGetLowLevelILNonSSAExprIndex.restype = ctypes.c_ulonglong
BNGetLowLevelILNonSSAExprIndex.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
	]
_BNGetLowLevelILNonSSAForm = core.BNGetLowLevelILNonSSAForm
_BNGetLowLevelILNonSSAForm.restype = ctypes.POINTER(BNLowLevelILFunction)
_BNGetLowLevelILNonSSAForm.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
	]
def BNGetLowLevelILNonSSAForm(*args):
	result = _BNGetLowLevelILNonSSAForm(*args)
	if not result:
		return None
	return result
BNGetLowLevelILNonSSAInstructionIndex = core.BNGetLowLevelILNonSSAInstructionIndex
BNGetLowLevelILNonSSAInstructionIndex.restype = ctypes.c_ulonglong
BNGetLowLevelILNonSSAInstructionIndex.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
	]
_BNGetLowLevelILOwnerFunction = core.BNGetLowLevelILOwnerFunction
_BNGetLowLevelILOwnerFunction.restype = ctypes.POINTER(BNFunction)
_BNGetLowLevelILOwnerFunction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
	]
def BNGetLowLevelILOwnerFunction(*args):
	result = _BNGetLowLevelILOwnerFunction(*args)
	if not result:
		return None
	return result
BNGetLowLevelILPossibleExprValues = core.BNGetLowLevelILPossibleExprValues
BNGetLowLevelILPossibleExprValues.restype = BNPossibleValueSet
BNGetLowLevelILPossibleExprValues.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetLowLevelILPossibleFlagValuesAfterInstruction = core.BNGetLowLevelILPossibleFlagValuesAfterInstruction
BNGetLowLevelILPossibleFlagValuesAfterInstruction.restype = BNPossibleValueSet
BNGetLowLevelILPossibleFlagValuesAfterInstruction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetLowLevelILPossibleFlagValuesAtInstruction = core.BNGetLowLevelILPossibleFlagValuesAtInstruction
BNGetLowLevelILPossibleFlagValuesAtInstruction.restype = BNPossibleValueSet
BNGetLowLevelILPossibleFlagValuesAtInstruction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetLowLevelILPossibleRegisterValuesAfterInstruction = core.BNGetLowLevelILPossibleRegisterValuesAfterInstruction
BNGetLowLevelILPossibleRegisterValuesAfterInstruction.restype = BNPossibleValueSet
BNGetLowLevelILPossibleRegisterValuesAfterInstruction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetLowLevelILPossibleRegisterValuesAtInstruction = core.BNGetLowLevelILPossibleRegisterValuesAtInstruction
BNGetLowLevelILPossibleRegisterValuesAtInstruction.restype = BNPossibleValueSet
BNGetLowLevelILPossibleRegisterValuesAtInstruction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetLowLevelILPossibleStackContentsAfterInstruction = core.BNGetLowLevelILPossibleStackContentsAfterInstruction
BNGetLowLevelILPossibleStackContentsAfterInstruction.restype = BNPossibleValueSet
BNGetLowLevelILPossibleStackContentsAfterInstruction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_longlong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNGetLowLevelILPossibleStackContentsAtInstruction = core.BNGetLowLevelILPossibleStackContentsAtInstruction
BNGetLowLevelILPossibleStackContentsAtInstruction.restype = BNPossibleValueSet
BNGetLowLevelILPossibleStackContentsAtInstruction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_longlong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNGetLowLevelILRegisterValueAfterInstruction = core.BNGetLowLevelILRegisterValueAfterInstruction
BNGetLowLevelILRegisterValueAfterInstruction.restype = BNRegisterValue
BNGetLowLevelILRegisterValueAfterInstruction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetLowLevelILRegisterValueAtInstruction = core.BNGetLowLevelILRegisterValueAtInstruction
BNGetLowLevelILRegisterValueAtInstruction.restype = BNRegisterValue
BNGetLowLevelILRegisterValueAtInstruction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetLowLevelILSSAExprIndex = core.BNGetLowLevelILSSAExprIndex
BNGetLowLevelILSSAExprIndex.restype = ctypes.c_ulonglong
BNGetLowLevelILSSAExprIndex.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetLowLevelILSSAFlagDefinition = core.BNGetLowLevelILSSAFlagDefinition
BNGetLowLevelILSSAFlagDefinition.restype = ctypes.c_ulonglong
BNGetLowLevelILSSAFlagDefinition.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
_BNGetLowLevelILSSAFlagUses = core.BNGetLowLevelILSSAFlagUses
_BNGetLowLevelILSSAFlagUses.restype = ctypes.POINTER(ctypes.c_ulonglong)
_BNGetLowLevelILSSAFlagUses.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetLowLevelILSSAFlagUses(*args):
	result = _BNGetLowLevelILSSAFlagUses(*args)
	if not result:
		return None
	return result
BNGetLowLevelILSSAFlagValue = core.BNGetLowLevelILSSAFlagValue
BNGetLowLevelILSSAFlagValue.restype = BNRegisterValue
BNGetLowLevelILSSAFlagValue.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
_BNGetLowLevelILSSAForm = core.BNGetLowLevelILSSAForm
_BNGetLowLevelILSSAForm.restype = ctypes.POINTER(BNLowLevelILFunction)
_BNGetLowLevelILSSAForm.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
	]
def BNGetLowLevelILSSAForm(*args):
	result = _BNGetLowLevelILSSAForm(*args)
	if not result:
		return None
	return result
BNGetLowLevelILSSAInstructionIndex = core.BNGetLowLevelILSSAInstructionIndex
BNGetLowLevelILSSAInstructionIndex.restype = ctypes.c_ulonglong
BNGetLowLevelILSSAInstructionIndex.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetLowLevelILSSAMemoryDefinition = core.BNGetLowLevelILSSAMemoryDefinition
BNGetLowLevelILSSAMemoryDefinition.restype = ctypes.c_ulonglong
BNGetLowLevelILSSAMemoryDefinition.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
	]
_BNGetLowLevelILSSAMemoryUses = core.BNGetLowLevelILSSAMemoryUses
_BNGetLowLevelILSSAMemoryUses.restype = ctypes.POINTER(ctypes.c_ulonglong)
_BNGetLowLevelILSSAMemoryUses.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetLowLevelILSSAMemoryUses(*args):
	result = _BNGetLowLevelILSSAMemoryUses(*args)
	if not result:
		return None
	return result
BNGetLowLevelILSSARegisterDefinition = core.BNGetLowLevelILSSARegisterDefinition
BNGetLowLevelILSSARegisterDefinition.restype = ctypes.c_ulonglong
BNGetLowLevelILSSARegisterDefinition.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
_BNGetLowLevelILSSARegisterUses = core.BNGetLowLevelILSSARegisterUses
_BNGetLowLevelILSSARegisterUses.restype = ctypes.POINTER(ctypes.c_ulonglong)
_BNGetLowLevelILSSARegisterUses.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetLowLevelILSSARegisterUses(*args):
	result = _BNGetLowLevelILSSARegisterUses(*args)
	if not result:
		return None
	return result
BNGetLowLevelILSSARegisterValue = core.BNGetLowLevelILSSARegisterValue
BNGetLowLevelILSSARegisterValue.restype = BNRegisterValue
BNGetLowLevelILSSARegisterValue.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetLowLevelILStackContentsAfterInstruction = core.BNGetLowLevelILStackContentsAfterInstruction
BNGetLowLevelILStackContentsAfterInstruction.restype = BNRegisterValue
BNGetLowLevelILStackContentsAfterInstruction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_longlong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNGetLowLevelILStackContentsAtInstruction = core.BNGetLowLevelILStackContentsAtInstruction
BNGetLowLevelILStackContentsAtInstruction.restype = BNRegisterValue
BNGetLowLevelILStackContentsAtInstruction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_longlong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNGetLowLevelILTemporaryFlagCount = core.BNGetLowLevelILTemporaryFlagCount
BNGetLowLevelILTemporaryFlagCount.restype = ctypes.c_uint
BNGetLowLevelILTemporaryFlagCount.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
	]
BNGetLowLevelILTemporaryRegisterCount = core.BNGetLowLevelILTemporaryRegisterCount
BNGetLowLevelILTemporaryRegisterCount.restype = ctypes.c_uint
BNGetLowLevelILTemporaryRegisterCount.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
	]
_BNGetMappedMediumLevelIL = core.BNGetMappedMediumLevelIL
_BNGetMappedMediumLevelIL.restype = ctypes.POINTER(BNMediumLevelILFunction)
_BNGetMappedMediumLevelIL.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
	]
def BNGetMappedMediumLevelIL(*args):
	result = _BNGetMappedMediumLevelIL(*args)
	if not result:
		return None
	return result
BNGetMappedMediumLevelILExprIndex = core.BNGetMappedMediumLevelILExprIndex
BNGetMappedMediumLevelILExprIndex.restype = ctypes.c_ulonglong
BNGetMappedMediumLevelILExprIndex.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetMappedMediumLevelILInstructionIndex = core.BNGetMappedMediumLevelILInstructionIndex
BNGetMappedMediumLevelILInstructionIndex.restype = ctypes.c_ulonglong
BNGetMappedMediumLevelILInstructionIndex.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
	]
_BNGetMediumLevelILBasicBlockList = core.BNGetMediumLevelILBasicBlockList
_BNGetMediumLevelILBasicBlockList.restype = ctypes.POINTER(ctypes.POINTER(BNBasicBlock))
_BNGetMediumLevelILBasicBlockList.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetMediumLevelILBasicBlockList(*args):
	result = _BNGetMediumLevelILBasicBlockList(*args)
	if not result:
		return None
	return result
BNGetMediumLevelILBranchDependence = core.BNGetMediumLevelILBranchDependence
BNGetMediumLevelILBranchDependence.restype = ILBranchDependenceEnum
BNGetMediumLevelILBranchDependence.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILByIndex = core.BNGetMediumLevelILByIndex
BNGetMediumLevelILByIndex.restype = BNMediumLevelILInstruction
BNGetMediumLevelILByIndex.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILExprCount = core.BNGetMediumLevelILExprCount
BNGetMediumLevelILExprCount.restype = ctypes.c_ulonglong
BNGetMediumLevelILExprCount.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
	]
BNGetMediumLevelILExprIndex = core.BNGetMediumLevelILExprIndex
BNGetMediumLevelILExprIndex.restype = ctypes.c_ulonglong
BNGetMediumLevelILExprIndex.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILExprText = core.BNGetMediumLevelILExprText
BNGetMediumLevelILExprText.restype = ctypes.c_bool
BNGetMediumLevelILExprText.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.POINTER(BNInstructionTextToken)),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
BNGetMediumLevelILExprType = core.BNGetMediumLevelILExprType
BNGetMediumLevelILExprType.restype = BNTypeWithConfidence
BNGetMediumLevelILExprType.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILExprValue = core.BNGetMediumLevelILExprValue
BNGetMediumLevelILExprValue.restype = BNRegisterValue
BNGetMediumLevelILExprValue.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILFlagValueAfterInstruction = core.BNGetMediumLevelILFlagValueAfterInstruction
BNGetMediumLevelILFlagValueAfterInstruction.restype = BNRegisterValue
BNGetMediumLevelILFlagValueAfterInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILFlagValueAtInstruction = core.BNGetMediumLevelILFlagValueAtInstruction
BNGetMediumLevelILFlagValueAtInstruction.restype = BNRegisterValue
BNGetMediumLevelILFlagValueAtInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
_BNGetMediumLevelILForLowLevelIL = core.BNGetMediumLevelILForLowLevelIL
_BNGetMediumLevelILForLowLevelIL.restype = ctypes.POINTER(BNMediumLevelILFunction)
_BNGetMediumLevelILForLowLevelIL.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
	]
def BNGetMediumLevelILForLowLevelIL(*args):
	result = _BNGetMediumLevelILForLowLevelIL(*args)
	if not result:
		return None
	return result
BNGetMediumLevelILIndexForInstruction = core.BNGetMediumLevelILIndexForInstruction
BNGetMediumLevelILIndexForInstruction.restype = ctypes.c_ulonglong
BNGetMediumLevelILIndexForInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILInstructionCount = core.BNGetMediumLevelILInstructionCount
BNGetMediumLevelILInstructionCount.restype = ctypes.c_ulonglong
BNGetMediumLevelILInstructionCount.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
	]
BNGetMediumLevelILInstructionForExpr = core.BNGetMediumLevelILInstructionForExpr
BNGetMediumLevelILInstructionForExpr.restype = ctypes.c_ulonglong
BNGetMediumLevelILInstructionForExpr.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILInstructionIndex = core.BNGetMediumLevelILInstructionIndex
BNGetMediumLevelILInstructionIndex.restype = ctypes.c_ulonglong
BNGetMediumLevelILInstructionIndex.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILInstructionText = core.BNGetMediumLevelILInstructionText
BNGetMediumLevelILInstructionText.restype = ctypes.c_bool
BNGetMediumLevelILInstructionText.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.POINTER(BNInstructionTextToken)),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
BNGetMediumLevelILNonSSAExprIndex = core.BNGetMediumLevelILNonSSAExprIndex
BNGetMediumLevelILNonSSAExprIndex.restype = ctypes.c_ulonglong
BNGetMediumLevelILNonSSAExprIndex.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
	]
_BNGetMediumLevelILNonSSAForm = core.BNGetMediumLevelILNonSSAForm
_BNGetMediumLevelILNonSSAForm.restype = ctypes.POINTER(BNMediumLevelILFunction)
_BNGetMediumLevelILNonSSAForm.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
	]
def BNGetMediumLevelILNonSSAForm(*args):
	result = _BNGetMediumLevelILNonSSAForm(*args)
	if not result:
		return None
	return result
BNGetMediumLevelILNonSSAInstructionIndex = core.BNGetMediumLevelILNonSSAInstructionIndex
BNGetMediumLevelILNonSSAInstructionIndex.restype = ctypes.c_ulonglong
BNGetMediumLevelILNonSSAInstructionIndex.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
	]
_BNGetMediumLevelILOwnerFunction = core.BNGetMediumLevelILOwnerFunction
_BNGetMediumLevelILOwnerFunction.restype = ctypes.POINTER(BNFunction)
_BNGetMediumLevelILOwnerFunction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
	]
def BNGetMediumLevelILOwnerFunction(*args):
	result = _BNGetMediumLevelILOwnerFunction(*args)
	if not result:
		return None
	return result
BNGetMediumLevelILPossibleExprValues = core.BNGetMediumLevelILPossibleExprValues
BNGetMediumLevelILPossibleExprValues.restype = BNPossibleValueSet
BNGetMediumLevelILPossibleExprValues.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILPossibleFlagValuesAfterInstruction = core.BNGetMediumLevelILPossibleFlagValuesAfterInstruction
BNGetMediumLevelILPossibleFlagValuesAfterInstruction.restype = BNPossibleValueSet
BNGetMediumLevelILPossibleFlagValuesAfterInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILPossibleFlagValuesAtInstruction = core.BNGetMediumLevelILPossibleFlagValuesAtInstruction
BNGetMediumLevelILPossibleFlagValuesAtInstruction.restype = BNPossibleValueSet
BNGetMediumLevelILPossibleFlagValuesAtInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILPossibleRegisterValuesAfterInstruction = core.BNGetMediumLevelILPossibleRegisterValuesAfterInstruction
BNGetMediumLevelILPossibleRegisterValuesAfterInstruction.restype = BNPossibleValueSet
BNGetMediumLevelILPossibleRegisterValuesAfterInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILPossibleRegisterValuesAtInstruction = core.BNGetMediumLevelILPossibleRegisterValuesAtInstruction
BNGetMediumLevelILPossibleRegisterValuesAtInstruction.restype = BNPossibleValueSet
BNGetMediumLevelILPossibleRegisterValuesAtInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILPossibleSSAVarValues = core.BNGetMediumLevelILPossibleSSAVarValues
BNGetMediumLevelILPossibleSSAVarValues.restype = BNPossibleValueSet
BNGetMediumLevelILPossibleSSAVarValues.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(BNVariable),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILPossibleStackContentsAfterInstruction = core.BNGetMediumLevelILPossibleStackContentsAfterInstruction
BNGetMediumLevelILPossibleStackContentsAfterInstruction.restype = BNPossibleValueSet
BNGetMediumLevelILPossibleStackContentsAfterInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_longlong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILPossibleStackContentsAtInstruction = core.BNGetMediumLevelILPossibleStackContentsAtInstruction
BNGetMediumLevelILPossibleStackContentsAtInstruction.restype = BNPossibleValueSet
BNGetMediumLevelILPossibleStackContentsAtInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_longlong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILRegisterValueAfterInstruction = core.BNGetMediumLevelILRegisterValueAfterInstruction
BNGetMediumLevelILRegisterValueAfterInstruction.restype = BNRegisterValue
BNGetMediumLevelILRegisterValueAfterInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILRegisterValueAtInstruction = core.BNGetMediumLevelILRegisterValueAtInstruction
BNGetMediumLevelILRegisterValueAtInstruction.restype = BNRegisterValue
BNGetMediumLevelILRegisterValueAtInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILSSAExprIndex = core.BNGetMediumLevelILSSAExprIndex
BNGetMediumLevelILSSAExprIndex.restype = ctypes.c_ulonglong
BNGetMediumLevelILSSAExprIndex.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
	]
_BNGetMediumLevelILSSAForm = core.BNGetMediumLevelILSSAForm
_BNGetMediumLevelILSSAForm.restype = ctypes.POINTER(BNMediumLevelILFunction)
_BNGetMediumLevelILSSAForm.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
	]
def BNGetMediumLevelILSSAForm(*args):
	result = _BNGetMediumLevelILSSAForm(*args)
	if not result:
		return None
	return result
BNGetMediumLevelILSSAInstructionIndex = core.BNGetMediumLevelILSSAInstructionIndex
BNGetMediumLevelILSSAInstructionIndex.restype = ctypes.c_ulonglong
BNGetMediumLevelILSSAInstructionIndex.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILSSAMemoryDefinition = core.BNGetMediumLevelILSSAMemoryDefinition
BNGetMediumLevelILSSAMemoryDefinition.restype = ctypes.c_ulonglong
BNGetMediumLevelILSSAMemoryDefinition.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
	]
_BNGetMediumLevelILSSAMemoryUses = core.BNGetMediumLevelILSSAMemoryUses
_BNGetMediumLevelILSSAMemoryUses.restype = ctypes.POINTER(ctypes.c_ulonglong)
_BNGetMediumLevelILSSAMemoryUses.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetMediumLevelILSSAMemoryUses(*args):
	result = _BNGetMediumLevelILSSAMemoryUses(*args)
	if not result:
		return None
	return result
BNGetMediumLevelILSSAMemoryVersionAtILInstruction = core.BNGetMediumLevelILSSAMemoryVersionAtILInstruction
BNGetMediumLevelILSSAMemoryVersionAtILInstruction.restype = ctypes.c_ulonglong
BNGetMediumLevelILSSAMemoryVersionAtILInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILSSAVarDefinition = core.BNGetMediumLevelILSSAVarDefinition
BNGetMediumLevelILSSAVarDefinition.restype = ctypes.c_ulonglong
BNGetMediumLevelILSSAVarDefinition.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(BNVariable),
		ctypes.c_ulonglong,
	]
_BNGetMediumLevelILSSAVarUses = core.BNGetMediumLevelILSSAVarUses
_BNGetMediumLevelILSSAVarUses.restype = ctypes.POINTER(ctypes.c_ulonglong)
_BNGetMediumLevelILSSAVarUses.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(BNVariable),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetMediumLevelILSSAVarUses(*args):
	result = _BNGetMediumLevelILSSAVarUses(*args)
	if not result:
		return None
	return result
BNGetMediumLevelILSSAVarValue = core.BNGetMediumLevelILSSAVarValue
BNGetMediumLevelILSSAVarValue.restype = BNRegisterValue
BNGetMediumLevelILSSAVarValue.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(BNVariable),
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILSSAVarVersionAtILInstruction = core.BNGetMediumLevelILSSAVarVersionAtILInstruction
BNGetMediumLevelILSSAVarVersionAtILInstruction.restype = ctypes.c_ulonglong
BNGetMediumLevelILSSAVarVersionAtILInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(BNVariable),
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILStackContentsAfterInstruction = core.BNGetMediumLevelILStackContentsAfterInstruction
BNGetMediumLevelILStackContentsAfterInstruction.restype = BNRegisterValue
BNGetMediumLevelILStackContentsAfterInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_longlong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILStackContentsAtInstruction = core.BNGetMediumLevelILStackContentsAtInstruction
BNGetMediumLevelILStackContentsAtInstruction.restype = BNRegisterValue
BNGetMediumLevelILStackContentsAtInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_longlong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
_BNGetMediumLevelILVariableDefinitions = core.BNGetMediumLevelILVariableDefinitions
_BNGetMediumLevelILVariableDefinitions.restype = ctypes.POINTER(ctypes.c_ulonglong)
_BNGetMediumLevelILVariableDefinitions.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(BNVariable),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetMediumLevelILVariableDefinitions(*args):
	result = _BNGetMediumLevelILVariableDefinitions(*args)
	if not result:
		return None
	return result
BNGetMediumLevelILVariableForFlagAtInstruction = core.BNGetMediumLevelILVariableForFlagAtInstruction
BNGetMediumLevelILVariableForFlagAtInstruction.restype = BNVariable
BNGetMediumLevelILVariableForFlagAtInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILVariableForRegisterAtInstruction = core.BNGetMediumLevelILVariableForRegisterAtInstruction
BNGetMediumLevelILVariableForRegisterAtInstruction.restype = BNVariable
BNGetMediumLevelILVariableForRegisterAtInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_uint,
		ctypes.c_ulonglong,
	]
BNGetMediumLevelILVariableForStackLocationAtInstruction = core.BNGetMediumLevelILVariableForStackLocationAtInstruction
BNGetMediumLevelILVariableForStackLocationAtInstruction.restype = BNVariable
BNGetMediumLevelILVariableForStackLocationAtInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_longlong,
		ctypes.c_ulonglong,
	]
_BNGetMediumLevelILVariableUses = core.BNGetMediumLevelILVariableUses
_BNGetMediumLevelILVariableUses.restype = ctypes.POINTER(ctypes.c_ulonglong)
_BNGetMediumLevelILVariableUses.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(BNVariable),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetMediumLevelILVariableUses(*args):
	result = _BNGetMediumLevelILVariableUses(*args)
	if not result:
		return None
	return result
BNGetModification = core.BNGetModification
BNGetModification.restype = ModificationStatusEnum
BNGetModification.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNGetModificationArray = core.BNGetModificationArray
BNGetModificationArray.restype = ctypes.c_ulonglong
BNGetModificationArray.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.POINTER(ModificationStatusEnum),
		ctypes.c_ulonglong,
	]
_BNGetModifiedArchitectureRegistersOnWrite = core.BNGetModifiedArchitectureRegistersOnWrite
_BNGetModifiedArchitectureRegistersOnWrite.restype = ctypes.POINTER(ctypes.c_uint)
_BNGetModifiedArchitectureRegistersOnWrite.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_uint,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetModifiedArchitectureRegistersOnWrite(*args):
	result = _BNGetModifiedArchitectureRegistersOnWrite(*args)
	if not result:
		return None
	return result
BNGetNextBasicBlockStartAfterAddress = core.BNGetNextBasicBlockStartAfterAddress
BNGetNextBasicBlockStartAfterAddress.restype = ctypes.c_ulonglong
BNGetNextBasicBlockStartAfterAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNGetNextDataAfterAddress = core.BNGetNextDataAfterAddress
BNGetNextDataAfterAddress.restype = ctypes.c_ulonglong
BNGetNextDataAfterAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNGetNextDataVariableAfterAddress = core.BNGetNextDataVariableAfterAddress
BNGetNextDataVariableAfterAddress.restype = ctypes.c_ulonglong
BNGetNextDataVariableAfterAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNGetNextFunctionStartAfterAddress = core.BNGetNextFunctionStartAfterAddress
BNGetNextFunctionStartAfterAddress.restype = ctypes.c_ulonglong
BNGetNextFunctionStartAfterAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
_BNGetNextLinearDisassemblyLines = core.BNGetNextLinearDisassemblyLines
_BNGetNextLinearDisassemblyLines.restype = ctypes.POINTER(BNLinearDisassemblyLine)
_BNGetNextLinearDisassemblyLines.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNLinearDisassemblyPosition),
		ctypes.POINTER(BNDisassemblySettings),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetNextLinearDisassemblyLines(*args):
	result = _BNGetNextLinearDisassemblyLines(*args)
	if not result:
		return None
	return result
BNGetNextValidOffset = core.BNGetNextValidOffset
BNGetNextValidOffset.restype = ctypes.c_ulonglong
BNGetNextValidOffset.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNGetOpenFileNameInput = core.BNGetOpenFileNameInput
BNGetOpenFileNameInput.restype = ctypes.c_bool
BNGetOpenFileNameInput.argtypes = [
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNGetParameterValueAtInstruction = core.BNGetParameterValueAtInstruction
BNGetParameterValueAtInstruction.restype = BNRegisterValue
BNGetParameterValueAtInstruction.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNType),
		ctypes.c_ulonglong,
	]
BNGetParameterValueAtLowLevelILInstruction = core.BNGetParameterValueAtLowLevelILInstruction
BNGetParameterValueAtLowLevelILInstruction.restype = BNRegisterValue
BNGetParameterValueAtLowLevelILInstruction.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNType),
		ctypes.c_ulonglong,
	]
_BNGetParentView = core.BNGetParentView
_BNGetParentView.restype = ctypes.POINTER(BNBinaryView)
_BNGetParentView.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
def BNGetParentView(*args):
	result = _BNGetParentView(*args)
	if not result:
		return None
	return result
_BNGetPathRelativeToBundledPluginDirectory = core.BNGetPathRelativeToBundledPluginDirectory
_BNGetPathRelativeToBundledPluginDirectory.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetPathRelativeToBundledPluginDirectory.argtypes = [
		ctypes.c_char_p,
	]
def BNGetPathRelativeToBundledPluginDirectory(*args):
	result = _BNGetPathRelativeToBundledPluginDirectory(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetPathRelativeToUserPluginDirectory = core.BNGetPathRelativeToUserPluginDirectory
_BNGetPathRelativeToUserPluginDirectory.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetPathRelativeToUserPluginDirectory.argtypes = [
		ctypes.c_char_p,
	]
def BNGetPathRelativeToUserPluginDirectory(*args):
	result = _BNGetPathRelativeToUserPluginDirectory(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetPlatformArchitecture = core.BNGetPlatformArchitecture
_BNGetPlatformArchitecture.restype = ctypes.POINTER(BNArchitecture)
_BNGetPlatformArchitecture.argtypes = [
		ctypes.POINTER(BNPlatform),
	]
def BNGetPlatformArchitecture(*args):
	result = _BNGetPlatformArchitecture(*args)
	if not result:
		return None
	return result
_BNGetPlatformByName = core.BNGetPlatformByName
_BNGetPlatformByName.restype = ctypes.POINTER(BNPlatform)
_BNGetPlatformByName.argtypes = [
		ctypes.c_char_p,
	]
def BNGetPlatformByName(*args):
	result = _BNGetPlatformByName(*args)
	if not result:
		return None
	return result
_BNGetPlatformCallingConventions = core.BNGetPlatformCallingConventions
_BNGetPlatformCallingConventions.restype = ctypes.POINTER(ctypes.POINTER(BNCallingConvention))
_BNGetPlatformCallingConventions.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetPlatformCallingConventions(*args):
	result = _BNGetPlatformCallingConventions(*args)
	if not result:
		return None
	return result
_BNGetPlatformCdeclCallingConvention = core.BNGetPlatformCdeclCallingConvention
_BNGetPlatformCdeclCallingConvention.restype = ctypes.POINTER(BNCallingConvention)
_BNGetPlatformCdeclCallingConvention.argtypes = [
		ctypes.POINTER(BNPlatform),
	]
def BNGetPlatformCdeclCallingConvention(*args):
	result = _BNGetPlatformCdeclCallingConvention(*args)
	if not result:
		return None
	return result
_BNGetPlatformDefaultCallingConvention = core.BNGetPlatformDefaultCallingConvention
_BNGetPlatformDefaultCallingConvention.restype = ctypes.POINTER(BNCallingConvention)
_BNGetPlatformDefaultCallingConvention.argtypes = [
		ctypes.POINTER(BNPlatform),
	]
def BNGetPlatformDefaultCallingConvention(*args):
	result = _BNGetPlatformDefaultCallingConvention(*args)
	if not result:
		return None
	return result
_BNGetPlatformFastcallCallingConvention = core.BNGetPlatformFastcallCallingConvention
_BNGetPlatformFastcallCallingConvention.restype = ctypes.POINTER(BNCallingConvention)
_BNGetPlatformFastcallCallingConvention.argtypes = [
		ctypes.POINTER(BNPlatform),
	]
def BNGetPlatformFastcallCallingConvention(*args):
	result = _BNGetPlatformFastcallCallingConvention(*args)
	if not result:
		return None
	return result
_BNGetPlatformForViewType = core.BNGetPlatformForViewType
_BNGetPlatformForViewType.restype = ctypes.POINTER(BNPlatform)
_BNGetPlatformForViewType.argtypes = [
		ctypes.POINTER(BNBinaryViewType),
		ctypes.c_uint,
		ctypes.POINTER(BNArchitecture),
	]
def BNGetPlatformForViewType(*args):
	result = _BNGetPlatformForViewType(*args)
	if not result:
		return None
	return result
_BNGetPlatformFunctionByName = core.BNGetPlatformFunctionByName
_BNGetPlatformFunctionByName.restype = ctypes.POINTER(BNType)
_BNGetPlatformFunctionByName.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(BNQualifiedName),
	]
def BNGetPlatformFunctionByName(*args):
	result = _BNGetPlatformFunctionByName(*args)
	if not result:
		return None
	return result
_BNGetPlatformFunctions = core.BNGetPlatformFunctions
_BNGetPlatformFunctions.restype = ctypes.POINTER(BNQualifiedNameAndType)
_BNGetPlatformFunctions.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetPlatformFunctions(*args):
	result = _BNGetPlatformFunctions(*args)
	if not result:
		return None
	return result
_BNGetPlatformList = core.BNGetPlatformList
_BNGetPlatformList.restype = ctypes.POINTER(ctypes.POINTER(BNPlatform))
_BNGetPlatformList.argtypes = [
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetPlatformList(*args):
	result = _BNGetPlatformList(*args)
	if not result:
		return None
	return result
_BNGetPlatformListByArchitecture = core.BNGetPlatformListByArchitecture
_BNGetPlatformListByArchitecture.restype = ctypes.POINTER(ctypes.POINTER(BNPlatform))
_BNGetPlatformListByArchitecture.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetPlatformListByArchitecture(*args):
	result = _BNGetPlatformListByArchitecture(*args)
	if not result:
		return None
	return result
_BNGetPlatformListByOS = core.BNGetPlatformListByOS
_BNGetPlatformListByOS.restype = ctypes.POINTER(ctypes.POINTER(BNPlatform))
_BNGetPlatformListByOS.argtypes = [
		ctypes.c_char_p,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetPlatformListByOS(*args):
	result = _BNGetPlatformListByOS(*args)
	if not result:
		return None
	return result
_BNGetPlatformListByOSAndArchitecture = core.BNGetPlatformListByOSAndArchitecture
_BNGetPlatformListByOSAndArchitecture.restype = ctypes.POINTER(ctypes.POINTER(BNPlatform))
_BNGetPlatformListByOSAndArchitecture.argtypes = [
		ctypes.c_char_p,
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetPlatformListByOSAndArchitecture(*args):
	result = _BNGetPlatformListByOSAndArchitecture(*args)
	if not result:
		return None
	return result
_BNGetPlatformName = core.BNGetPlatformName
_BNGetPlatformName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetPlatformName.argtypes = [
		ctypes.POINTER(BNPlatform),
	]
def BNGetPlatformName(*args):
	result = _BNGetPlatformName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetPlatformOSList = core.BNGetPlatformOSList
_BNGetPlatformOSList.restype = ctypes.POINTER(ctypes.c_char_p)
_BNGetPlatformOSList.argtypes = [
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetPlatformOSList(*args):
	result = _BNGetPlatformOSList(*args)
	if not result:
		return None
	return result
_BNGetPlatformStdcallCallingConvention = core.BNGetPlatformStdcallCallingConvention
_BNGetPlatformStdcallCallingConvention.restype = ctypes.POINTER(BNCallingConvention)
_BNGetPlatformStdcallCallingConvention.argtypes = [
		ctypes.POINTER(BNPlatform),
	]
def BNGetPlatformStdcallCallingConvention(*args):
	result = _BNGetPlatformStdcallCallingConvention(*args)
	if not result:
		return None
	return result
_BNGetPlatformSystemCallConvention = core.BNGetPlatformSystemCallConvention
_BNGetPlatformSystemCallConvention.restype = ctypes.POINTER(BNCallingConvention)
_BNGetPlatformSystemCallConvention.argtypes = [
		ctypes.POINTER(BNPlatform),
	]
def BNGetPlatformSystemCallConvention(*args):
	result = _BNGetPlatformSystemCallConvention(*args)
	if not result:
		return None
	return result
_BNGetPlatformSystemCallName = core.BNGetPlatformSystemCallName
_BNGetPlatformSystemCallName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetPlatformSystemCallName.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.c_uint,
	]
def BNGetPlatformSystemCallName(*args):
	result = _BNGetPlatformSystemCallName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetPlatformSystemCallType = core.BNGetPlatformSystemCallType
_BNGetPlatformSystemCallType.restype = ctypes.POINTER(BNType)
_BNGetPlatformSystemCallType.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.c_uint,
	]
def BNGetPlatformSystemCallType(*args):
	result = _BNGetPlatformSystemCallType(*args)
	if not result:
		return None
	return result
_BNGetPlatformSystemCalls = core.BNGetPlatformSystemCalls
_BNGetPlatformSystemCalls.restype = ctypes.POINTER(BNSystemCallInfo)
_BNGetPlatformSystemCalls.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetPlatformSystemCalls(*args):
	result = _BNGetPlatformSystemCalls(*args)
	if not result:
		return None
	return result
_BNGetPlatformTypeByName = core.BNGetPlatformTypeByName
_BNGetPlatformTypeByName.restype = ctypes.POINTER(BNType)
_BNGetPlatformTypeByName.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(BNQualifiedName),
	]
def BNGetPlatformTypeByName(*args):
	result = _BNGetPlatformTypeByName(*args)
	if not result:
		return None
	return result
_BNGetPlatformTypes = core.BNGetPlatformTypes
_BNGetPlatformTypes.restype = ctypes.POINTER(BNQualifiedNameAndType)
_BNGetPlatformTypes.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetPlatformTypes(*args):
	result = _BNGetPlatformTypes(*args)
	if not result:
		return None
	return result
_BNGetPlatformVariableByName = core.BNGetPlatformVariableByName
_BNGetPlatformVariableByName.restype = ctypes.POINTER(BNType)
_BNGetPlatformVariableByName.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(BNQualifiedName),
	]
def BNGetPlatformVariableByName(*args):
	result = _BNGetPlatformVariableByName(*args)
	if not result:
		return None
	return result
_BNGetPlatformVariables = core.BNGetPlatformVariables
_BNGetPlatformVariables.restype = ctypes.POINTER(BNQualifiedNameAndType)
_BNGetPlatformVariables.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetPlatformVariables(*args):
	result = _BNGetPlatformVariables(*args)
	if not result:
		return None
	return result
BNGetPreviousBasicBlockEndBeforeAddress = core.BNGetPreviousBasicBlockEndBeforeAddress
BNGetPreviousBasicBlockEndBeforeAddress.restype = ctypes.c_ulonglong
BNGetPreviousBasicBlockEndBeforeAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNGetPreviousBasicBlockStartBeforeAddress = core.BNGetPreviousBasicBlockStartBeforeAddress
BNGetPreviousBasicBlockStartBeforeAddress.restype = ctypes.c_ulonglong
BNGetPreviousBasicBlockStartBeforeAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNGetPreviousDataBeforeAddress = core.BNGetPreviousDataBeforeAddress
BNGetPreviousDataBeforeAddress.restype = ctypes.c_ulonglong
BNGetPreviousDataBeforeAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNGetPreviousDataVariableBeforeAddress = core.BNGetPreviousDataVariableBeforeAddress
BNGetPreviousDataVariableBeforeAddress.restype = ctypes.c_ulonglong
BNGetPreviousDataVariableBeforeAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNGetPreviousFunctionStartBeforeAddress = core.BNGetPreviousFunctionStartBeforeAddress
BNGetPreviousFunctionStartBeforeAddress.restype = ctypes.c_ulonglong
BNGetPreviousFunctionStartBeforeAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
_BNGetPreviousLinearDisassemblyLines = core.BNGetPreviousLinearDisassemblyLines
_BNGetPreviousLinearDisassemblyLines.restype = ctypes.POINTER(BNLinearDisassemblyLine)
_BNGetPreviousLinearDisassemblyLines.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNLinearDisassemblyPosition),
		ctypes.POINTER(BNDisassemblySettings),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetPreviousLinearDisassemblyLines(*args):
	result = _BNGetPreviousLinearDisassemblyLines(*args)
	if not result:
		return None
	return result
_BNGetProduct = core.BNGetProduct
_BNGetProduct.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetProduct.argtypes = [
	]
def BNGetProduct(*args):
	result = _BNGetProduct(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetProductType = core.BNGetProductType
_BNGetProductType.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetProductType.argtypes = [
	]
def BNGetProductType(*args):
	result = _BNGetProductType(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGetReaderPosition = core.BNGetReaderPosition
BNGetReaderPosition.restype = ctypes.c_ulonglong
BNGetReaderPosition.argtypes = [
		ctypes.POINTER(BNBinaryReader),
	]
_BNGetRecentAnalysisFunctionForAddress = core.BNGetRecentAnalysisFunctionForAddress
_BNGetRecentAnalysisFunctionForAddress.restype = ctypes.POINTER(BNFunction)
_BNGetRecentAnalysisFunctionForAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
def BNGetRecentAnalysisFunctionForAddress(*args):
	result = _BNGetRecentAnalysisFunctionForAddress(*args)
	if not result:
		return None
	return result
_BNGetRecentBasicBlockForAddress = core.BNGetRecentBasicBlockForAddress
_BNGetRecentBasicBlockForAddress.restype = ctypes.POINTER(BNBasicBlock)
_BNGetRecentBasicBlockForAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
def BNGetRecentBasicBlockForAddress(*args):
	result = _BNGetRecentBasicBlockForAddress(*args)
	if not result:
		return None
	return result
BNGetRegisterValueAfterInstruction = core.BNGetRegisterValueAfterInstruction
BNGetRegisterValueAfterInstruction.restype = BNRegisterValue
BNGetRegisterValueAfterInstruction.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.c_uint,
	]
BNGetRegisterValueAtInstruction = core.BNGetRegisterValueAtInstruction
BNGetRegisterValueAtInstruction.restype = BNRegisterValue
BNGetRegisterValueAtInstruction.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.c_uint,
	]
_BNGetRegistersReadByInstruction = core.BNGetRegistersReadByInstruction
_BNGetRegistersReadByInstruction.restype = ctypes.POINTER(ctypes.c_uint)
_BNGetRegistersReadByInstruction.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetRegistersReadByInstruction(*args):
	result = _BNGetRegistersReadByInstruction(*args)
	if not result:
		return None
	return result
_BNGetRegistersWrittenByInstruction = core.BNGetRegistersWrittenByInstruction
_BNGetRegistersWrittenByInstruction.restype = ctypes.POINTER(ctypes.c_uint)
_BNGetRegistersWrittenByInstruction.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetRegistersWrittenByInstruction(*args):
	result = _BNGetRegistersWrittenByInstruction(*args)
	if not result:
		return None
	return result
_BNGetRelatedPlatform = core.BNGetRelatedPlatform
_BNGetRelatedPlatform.restype = ctypes.POINTER(BNPlatform)
_BNGetRelatedPlatform.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(BNArchitecture),
	]
def BNGetRelatedPlatform(*args):
	result = _BNGetRelatedPlatform(*args)
	if not result:
		return None
	return result
_BNGetRepositoriesDirectory = core.BNGetRepositoriesDirectory
_BNGetRepositoriesDirectory.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetRepositoriesDirectory.argtypes = [
	]
def BNGetRepositoriesDirectory(*args):
	result = _BNGetRepositoriesDirectory(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetRepositoryManager = core.BNGetRepositoryManager
_BNGetRepositoryManager.restype = ctypes.POINTER(BNRepositoryManager)
_BNGetRepositoryManager.argtypes = [
	]
def BNGetRepositoryManager(*args):
	result = _BNGetRepositoryManager(*args)
	if not result:
		return None
	return result
_BNGetRunningBackgroundTasks = core.BNGetRunningBackgroundTasks
_BNGetRunningBackgroundTasks.restype = ctypes.POINTER(ctypes.POINTER(BNBackgroundTask))
_BNGetRunningBackgroundTasks.argtypes = [
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetRunningBackgroundTasks(*args):
	result = _BNGetRunningBackgroundTasks(*args)
	if not result:
		return None
	return result
BNGetSaveFileNameInput = core.BNGetSaveFileNameInput
BNGetSaveFileNameInput.restype = ctypes.c_bool
BNGetSaveFileNameInput.argtypes = [
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNGetScriptingInstanceInputReadyState = core.BNGetScriptingInstanceInputReadyState
BNGetScriptingInstanceInputReadyState.restype = ScriptingProviderInputReadyStateEnum
BNGetScriptingInstanceInputReadyState.argtypes = [
		ctypes.POINTER(BNScriptingInstance),
	]
_BNGetScriptingProviderByName = core.BNGetScriptingProviderByName
_BNGetScriptingProviderByName.restype = ctypes.POINTER(BNScriptingProvider)
_BNGetScriptingProviderByName.argtypes = [
		ctypes.c_char_p,
	]
def BNGetScriptingProviderByName(*args):
	result = _BNGetScriptingProviderByName(*args)
	if not result:
		return None
	return result
_BNGetScriptingProviderList = core.BNGetScriptingProviderList
_BNGetScriptingProviderList.restype = ctypes.POINTER(ctypes.POINTER(BNScriptingProvider))
_BNGetScriptingProviderList.argtypes = [
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetScriptingProviderList(*args):
	result = _BNGetScriptingProviderList(*args)
	if not result:
		return None
	return result
_BNGetScriptingProviderName = core.BNGetScriptingProviderName
_BNGetScriptingProviderName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetScriptingProviderName.argtypes = [
		ctypes.POINTER(BNScriptingProvider),
	]
def BNGetScriptingProviderName(*args):
	result = _BNGetScriptingProviderName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGetSectionByName = core.BNGetSectionByName
BNGetSectionByName.restype = ctypes.c_bool
BNGetSectionByName.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
		ctypes.POINTER(BNSection),
	]
_BNGetSections = core.BNGetSections
_BNGetSections.restype = ctypes.POINTER(BNSection)
_BNGetSections.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetSections(*args):
	result = _BNGetSections(*args)
	if not result:
		return None
	return result
_BNGetSectionsAt = core.BNGetSectionsAt
_BNGetSectionsAt.restype = ctypes.POINTER(BNSection)
_BNGetSectionsAt.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetSectionsAt(*args):
	result = _BNGetSectionsAt(*args)
	if not result:
		return None
	return result
BNGetSegmentAt = core.BNGetSegmentAt
BNGetSegmentAt.restype = ctypes.c_bool
BNGetSegmentAt.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNSegment),
	]
_BNGetSegments = core.BNGetSegments
_BNGetSegments.restype = ctypes.POINTER(BNSegment)
_BNGetSegments.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetSegments(*args):
	result = _BNGetSegments(*args)
	if not result:
		return None
	return result
_BNGetSettingsFileName = core.BNGetSettingsFileName
_BNGetSettingsFileName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetSettingsFileName.argtypes = [
	]
def BNGetSettingsFileName(*args):
	result = _BNGetSettingsFileName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGetStackContentsAfterInstruction = core.BNGetStackContentsAfterInstruction
BNGetStackContentsAfterInstruction.restype = BNRegisterValue
BNGetStackContentsAfterInstruction.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.c_longlong,
		ctypes.c_ulonglong,
	]
BNGetStackContentsAtInstruction = core.BNGetStackContentsAtInstruction
BNGetStackContentsAtInstruction.restype = BNRegisterValue
BNGetStackContentsAtInstruction.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.c_longlong,
		ctypes.c_ulonglong,
	]
_BNGetStackLayout = core.BNGetStackLayout
_BNGetStackLayout.restype = ctypes.POINTER(BNVariableNameAndType)
_BNGetStackLayout.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetStackLayout(*args):
	result = _BNGetStackLayout(*args)
	if not result:
		return None
	return result
BNGetStackVariableAtFrameOffset = core.BNGetStackVariableAtFrameOffset
BNGetStackVariableAtFrameOffset.restype = ctypes.c_bool
BNGetStackVariableAtFrameOffset.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.c_longlong,
		ctypes.POINTER(BNVariableNameAndType),
	]
_BNGetStackVariablesReferencedByInstruction = core.BNGetStackVariablesReferencedByInstruction
_BNGetStackVariablesReferencedByInstruction.restype = ctypes.POINTER(BNStackVariableReference)
_BNGetStackVariablesReferencedByInstruction.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetStackVariablesReferencedByInstruction(*args):
	result = _BNGetStackVariablesReferencedByInstruction(*args)
	if not result:
		return None
	return result
BNGetStartOffset = core.BNGetStartOffset
BNGetStartOffset.restype = ctypes.c_ulonglong
BNGetStartOffset.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
_BNGetStrings = core.BNGetStrings
_BNGetStrings.restype = ctypes.POINTER(BNStringReference)
_BNGetStrings.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetStrings(*args):
	result = _BNGetStrings(*args)
	if not result:
		return None
	return result
_BNGetStringsInRange = core.BNGetStringsInRange
_BNGetStringsInRange.restype = ctypes.POINTER(BNStringReference)
_BNGetStringsInRange.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetStringsInRange(*args):
	result = _BNGetStringsInRange(*args)
	if not result:
		return None
	return result
BNGetStructureAlignment = core.BNGetStructureAlignment
BNGetStructureAlignment.restype = ctypes.c_ulonglong
BNGetStructureAlignment.argtypes = [
		ctypes.POINTER(BNStructure),
	]
_BNGetStructureMembers = core.BNGetStructureMembers
_BNGetStructureMembers.restype = ctypes.POINTER(BNStructureMember)
_BNGetStructureMembers.argtypes = [
		ctypes.POINTER(BNStructure),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetStructureMembers(*args):
	result = _BNGetStructureMembers(*args)
	if not result:
		return None
	return result
BNGetStructureType = core.BNGetStructureType
BNGetStructureType.restype = StructureTypeEnum
BNGetStructureType.argtypes = [
		ctypes.POINTER(BNStructure),
	]
BNGetStructureWidth = core.BNGetStructureWidth
BNGetStructureWidth.restype = ctypes.c_ulonglong
BNGetStructureWidth.argtypes = [
		ctypes.POINTER(BNStructure),
	]
BNGetSymbolAddress = core.BNGetSymbolAddress
BNGetSymbolAddress.restype = ctypes.c_ulonglong
BNGetSymbolAddress.argtypes = [
		ctypes.POINTER(BNSymbol),
	]
_BNGetSymbolByAddress = core.BNGetSymbolByAddress
_BNGetSymbolByAddress.restype = ctypes.POINTER(BNSymbol)
_BNGetSymbolByAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
def BNGetSymbolByAddress(*args):
	result = _BNGetSymbolByAddress(*args)
	if not result:
		return None
	return result
_BNGetSymbolByRawName = core.BNGetSymbolByRawName
_BNGetSymbolByRawName.restype = ctypes.POINTER(BNSymbol)
_BNGetSymbolByRawName.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
	]
def BNGetSymbolByRawName(*args):
	result = _BNGetSymbolByRawName(*args)
	if not result:
		return None
	return result
_BNGetSymbolFullName = core.BNGetSymbolFullName
_BNGetSymbolFullName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetSymbolFullName.argtypes = [
		ctypes.POINTER(BNSymbol),
	]
def BNGetSymbolFullName(*args):
	result = _BNGetSymbolFullName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetSymbolRawName = core.BNGetSymbolRawName
_BNGetSymbolRawName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetSymbolRawName.argtypes = [
		ctypes.POINTER(BNSymbol),
	]
def BNGetSymbolRawName(*args):
	result = _BNGetSymbolRawName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetSymbolShortName = core.BNGetSymbolShortName
_BNGetSymbolShortName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetSymbolShortName.argtypes = [
		ctypes.POINTER(BNSymbol),
	]
def BNGetSymbolShortName(*args):
	result = _BNGetSymbolShortName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGetSymbolType = core.BNGetSymbolType
BNGetSymbolType.restype = SymbolTypeEnum
BNGetSymbolType.argtypes = [
		ctypes.POINTER(BNSymbol),
	]
_BNGetSymbols = core.BNGetSymbols
_BNGetSymbols.restype = ctypes.POINTER(ctypes.POINTER(BNSymbol))
_BNGetSymbols.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetSymbols(*args):
	result = _BNGetSymbols(*args)
	if not result:
		return None
	return result
_BNGetSymbolsByName = core.BNGetSymbolsByName
_BNGetSymbolsByName.restype = ctypes.POINTER(ctypes.POINTER(BNSymbol))
_BNGetSymbolsByName.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetSymbolsByName(*args):
	result = _BNGetSymbolsByName(*args)
	if not result:
		return None
	return result
_BNGetSymbolsInRange = core.BNGetSymbolsInRange
_BNGetSymbolsInRange.restype = ctypes.POINTER(ctypes.POINTER(BNSymbol))
_BNGetSymbolsInRange.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetSymbolsInRange(*args):
	result = _BNGetSymbolsInRange(*args)
	if not result:
		return None
	return result
_BNGetSymbolsOfType = core.BNGetSymbolsOfType
_BNGetSymbolsOfType.restype = ctypes.POINTER(ctypes.POINTER(BNSymbol))
_BNGetSymbolsOfType.argtypes = [
		ctypes.POINTER(BNBinaryView),
		SymbolTypeEnum,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetSymbolsOfType(*args):
	result = _BNGetSymbolsOfType(*args)
	if not result:
		return None
	return result
_BNGetSymbolsOfTypeInRange = core.BNGetSymbolsOfTypeInRange
_BNGetSymbolsOfTypeInRange.restype = ctypes.POINTER(ctypes.POINTER(BNSymbol))
_BNGetSymbolsOfTypeInRange.argtypes = [
		ctypes.POINTER(BNBinaryView),
		SymbolTypeEnum,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetSymbolsOfTypeInRange(*args):
	result = _BNGetSymbolsOfTypeInRange(*args)
	if not result:
		return None
	return result
_BNGetTemporaryFileContents = core.BNGetTemporaryFileContents
_BNGetTemporaryFileContents.restype = ctypes.POINTER(BNDataBuffer)
_BNGetTemporaryFileContents.argtypes = [
		ctypes.POINTER(BNTemporaryFile),
	]
def BNGetTemporaryFileContents(*args):
	result = _BNGetTemporaryFileContents(*args)
	if not result:
		return None
	return result
_BNGetTemporaryFilePath = core.BNGetTemporaryFilePath
_BNGetTemporaryFilePath.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetTemporaryFilePath.argtypes = [
		ctypes.POINTER(BNTemporaryFile),
	]
def BNGetTemporaryFilePath(*args):
	result = _BNGetTemporaryFilePath(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGetTextLineInput = core.BNGetTextLineInput
BNGetTextLineInput.restype = ctypes.c_bool
BNGetTextLineInput.argtypes = [
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNGetTimeSinceLastUpdateCheck = core.BNGetTimeSinceLastUpdateCheck
BNGetTimeSinceLastUpdateCheck.restype = ctypes.c_ulonglong
BNGetTimeSinceLastUpdateCheck.argtypes = [
	]
_BNGetTransformByName = core.BNGetTransformByName
_BNGetTransformByName.restype = ctypes.POINTER(BNTransform)
_BNGetTransformByName.argtypes = [
		ctypes.c_char_p,
	]
def BNGetTransformByName(*args):
	result = _BNGetTransformByName(*args)
	if not result:
		return None
	return result
_BNGetTransformGroup = core.BNGetTransformGroup
_BNGetTransformGroup.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetTransformGroup.argtypes = [
		ctypes.POINTER(BNTransform),
	]
def BNGetTransformGroup(*args):
	result = _BNGetTransformGroup(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetTransformLongName = core.BNGetTransformLongName
_BNGetTransformLongName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetTransformLongName.argtypes = [
		ctypes.POINTER(BNTransform),
	]
def BNGetTransformLongName(*args):
	result = _BNGetTransformLongName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetTransformName = core.BNGetTransformName
_BNGetTransformName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetTransformName.argtypes = [
		ctypes.POINTER(BNTransform),
	]
def BNGetTransformName(*args):
	result = _BNGetTransformName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetTransformParameterList = core.BNGetTransformParameterList
_BNGetTransformParameterList.restype = ctypes.POINTER(BNTransformParameterInfo)
_BNGetTransformParameterList.argtypes = [
		ctypes.POINTER(BNTransform),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetTransformParameterList(*args):
	result = _BNGetTransformParameterList(*args)
	if not result:
		return None
	return result
BNGetTransformType = core.BNGetTransformType
BNGetTransformType.restype = TransformTypeEnum
BNGetTransformType.argtypes = [
		ctypes.POINTER(BNTransform),
	]
_BNGetTransformTypeList = core.BNGetTransformTypeList
_BNGetTransformTypeList.restype = ctypes.POINTER(ctypes.POINTER(BNTransform))
_BNGetTransformTypeList.argtypes = [
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetTransformTypeList(*args):
	result = _BNGetTransformTypeList(*args)
	if not result:
		return None
	return result
BNGetTypeAlignment = core.BNGetTypeAlignment
BNGetTypeAlignment.restype = ctypes.c_ulonglong
BNGetTypeAlignment.argtypes = [
		ctypes.POINTER(BNType),
	]
_BNGetTypeAndName = core.BNGetTypeAndName
_BNGetTypeAndName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetTypeAndName.argtypes = [
		ctypes.POINTER(BNType),
		ctypes.POINTER(BNQualifiedName),
	]
def BNGetTypeAndName(*args):
	result = _BNGetTypeAndName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGetTypeCallingConvention = core.BNGetTypeCallingConvention
BNGetTypeCallingConvention.restype = BNCallingConventionWithConfidence
BNGetTypeCallingConvention.argtypes = [
		ctypes.POINTER(BNType),
	]
BNGetTypeClass = core.BNGetTypeClass
BNGetTypeClass.restype = TypeClassEnum
BNGetTypeClass.argtypes = [
		ctypes.POINTER(BNType),
	]
BNGetTypeElementCount = core.BNGetTypeElementCount
BNGetTypeElementCount.restype = ctypes.c_ulonglong
BNGetTypeElementCount.argtypes = [
		ctypes.POINTER(BNType),
	]
_BNGetTypeEnumeration = core.BNGetTypeEnumeration
_BNGetTypeEnumeration.restype = ctypes.POINTER(BNEnumeration)
_BNGetTypeEnumeration.argtypes = [
		ctypes.POINTER(BNType),
	]
def BNGetTypeEnumeration(*args):
	result = _BNGetTypeEnumeration(*args)
	if not result:
		return None
	return result
_BNGetTypeNamedTypeReference = core.BNGetTypeNamedTypeReference
_BNGetTypeNamedTypeReference.restype = ctypes.POINTER(BNNamedTypeReference)
_BNGetTypeNamedTypeReference.argtypes = [
		ctypes.POINTER(BNType),
	]
def BNGetTypeNamedTypeReference(*args):
	result = _BNGetTypeNamedTypeReference(*args)
	if not result:
		return None
	return result
BNGetTypeOffset = core.BNGetTypeOffset
BNGetTypeOffset.restype = ctypes.c_ulonglong
BNGetTypeOffset.argtypes = [
		ctypes.POINTER(BNType),
	]
_BNGetTypeParameters = core.BNGetTypeParameters
_BNGetTypeParameters.restype = ctypes.POINTER(BNFunctionParameter)
_BNGetTypeParameters.argtypes = [
		ctypes.POINTER(BNType),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetTypeParameters(*args):
	result = _BNGetTypeParameters(*args)
	if not result:
		return None
	return result
BNGetTypeReferenceClass = core.BNGetTypeReferenceClass
BNGetTypeReferenceClass.restype = NamedTypeReferenceClassEnum
BNGetTypeReferenceClass.argtypes = [
		ctypes.POINTER(BNNamedTypeReference),
	]
_BNGetTypeReferenceId = core.BNGetTypeReferenceId
_BNGetTypeReferenceId.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetTypeReferenceId.argtypes = [
		ctypes.POINTER(BNNamedTypeReference),
	]
def BNGetTypeReferenceId(*args):
	result = _BNGetTypeReferenceId(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGetTypeReferenceName = core.BNGetTypeReferenceName
BNGetTypeReferenceName.restype = BNQualifiedName
BNGetTypeReferenceName.argtypes = [
		ctypes.POINTER(BNNamedTypeReference),
	]
BNGetTypeStackAdjustment = core.BNGetTypeStackAdjustment
BNGetTypeStackAdjustment.restype = BNSizeWithConfidence
BNGetTypeStackAdjustment.argtypes = [
		ctypes.POINTER(BNType),
	]
_BNGetTypeString = core.BNGetTypeString
_BNGetTypeString.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetTypeString.argtypes = [
		ctypes.POINTER(BNType),
		ctypes.POINTER(BNPlatform),
	]
def BNGetTypeString(*args):
	result = _BNGetTypeString(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetTypeStringAfterName = core.BNGetTypeStringAfterName
_BNGetTypeStringAfterName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetTypeStringAfterName.argtypes = [
		ctypes.POINTER(BNType),
		ctypes.POINTER(BNPlatform),
	]
def BNGetTypeStringAfterName(*args):
	result = _BNGetTypeStringAfterName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetTypeStringBeforeName = core.BNGetTypeStringBeforeName
_BNGetTypeStringBeforeName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetTypeStringBeforeName.argtypes = [
		ctypes.POINTER(BNType),
		ctypes.POINTER(BNPlatform),
	]
def BNGetTypeStringBeforeName(*args):
	result = _BNGetTypeStringBeforeName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetTypeStructure = core.BNGetTypeStructure
_BNGetTypeStructure.restype = ctypes.POINTER(BNStructure)
_BNGetTypeStructure.argtypes = [
		ctypes.POINTER(BNType),
	]
def BNGetTypeStructure(*args):
	result = _BNGetTypeStructure(*args)
	if not result:
		return None
	return result
_BNGetTypeTokens = core.BNGetTypeTokens
_BNGetTypeTokens.restype = ctypes.POINTER(BNInstructionTextToken)
_BNGetTypeTokens.argtypes = [
		ctypes.POINTER(BNType),
		ctypes.POINTER(BNPlatform),
		ctypes.c_ubyte,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetTypeTokens(*args):
	result = _BNGetTypeTokens(*args)
	if not result:
		return None
	return result
_BNGetTypeTokensAfterName = core.BNGetTypeTokensAfterName
_BNGetTypeTokensAfterName.restype = ctypes.POINTER(BNInstructionTextToken)
_BNGetTypeTokensAfterName.argtypes = [
		ctypes.POINTER(BNType),
		ctypes.POINTER(BNPlatform),
		ctypes.c_ubyte,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetTypeTokensAfterName(*args):
	result = _BNGetTypeTokensAfterName(*args)
	if not result:
		return None
	return result
_BNGetTypeTokensBeforeName = core.BNGetTypeTokensBeforeName
_BNGetTypeTokensBeforeName.restype = ctypes.POINTER(BNInstructionTextToken)
_BNGetTypeTokensBeforeName.argtypes = [
		ctypes.POINTER(BNType),
		ctypes.POINTER(BNPlatform),
		ctypes.c_ubyte,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetTypeTokensBeforeName(*args):
	result = _BNGetTypeTokensBeforeName(*args)
	if not result:
		return None
	return result
BNGetTypeWidth = core.BNGetTypeWidth
BNGetTypeWidth.restype = ctypes.c_ulonglong
BNGetTypeWidth.argtypes = [
		ctypes.POINTER(BNType),
	]
_BNGetUniqueIdentifierString = core.BNGetUniqueIdentifierString
_BNGetUniqueIdentifierString.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetUniqueIdentifierString.argtypes = [
	]
def BNGetUniqueIdentifierString(*args):
	result = _BNGetUniqueIdentifierString(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetUniqueSectionNames = core.BNGetUniqueSectionNames
_BNGetUniqueSectionNames.restype = ctypes.POINTER(ctypes.c_char_p)
_BNGetUniqueSectionNames.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.c_ulonglong,
	]
def BNGetUniqueSectionNames(*args):
	result = _BNGetUniqueSectionNames(*args)
	if not result:
		return None
	return result
_BNGetUpdateChannelVersions = core.BNGetUpdateChannelVersions
_BNGetUpdateChannelVersions.restype = ctypes.POINTER(BNUpdateVersion)
_BNGetUpdateChannelVersions.argtypes = [
		ctypes.c_char_p,
		ctypes.POINTER(ctypes.c_ulonglong),
		ctypes.POINTER(ctypes.c_char_p),
	]
def BNGetUpdateChannelVersions(*args):
	result = _BNGetUpdateChannelVersions(*args)
	if not result:
		return None
	return result
_BNGetUpdateChannels = core.BNGetUpdateChannels
_BNGetUpdateChannels.restype = ctypes.POINTER(BNUpdateChannel)
_BNGetUpdateChannels.argtypes = [
		ctypes.POINTER(ctypes.c_ulonglong),
		ctypes.POINTER(ctypes.c_char_p),
	]
def BNGetUpdateChannels(*args):
	result = _BNGetUpdateChannels(*args)
	if not result:
		return None
	return result
_BNGetUserDirectory = core.BNGetUserDirectory
_BNGetUserDirectory.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetUserDirectory.argtypes = [
	]
def BNGetUserDirectory(*args):
	result = _BNGetUserDirectory(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetUserPluginDirectory = core.BNGetUserPluginDirectory
_BNGetUserPluginDirectory.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetUserPluginDirectory.argtypes = [
	]
def BNGetUserPluginDirectory(*args):
	result = _BNGetUserPluginDirectory(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNGetValidPluginCommands = core.BNGetValidPluginCommands
_BNGetValidPluginCommands.restype = ctypes.POINTER(BNPluginCommand)
_BNGetValidPluginCommands.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetValidPluginCommands(*args):
	result = _BNGetValidPluginCommands(*args)
	if not result:
		return None
	return result
_BNGetValidPluginCommandsForAddress = core.BNGetValidPluginCommandsForAddress
_BNGetValidPluginCommandsForAddress.restype = ctypes.POINTER(BNPluginCommand)
_BNGetValidPluginCommandsForAddress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetValidPluginCommandsForAddress(*args):
	result = _BNGetValidPluginCommandsForAddress(*args)
	if not result:
		return None
	return result
_BNGetValidPluginCommandsForFunction = core.BNGetValidPluginCommandsForFunction
_BNGetValidPluginCommandsForFunction.restype = ctypes.POINTER(BNPluginCommand)
_BNGetValidPluginCommandsForFunction.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetValidPluginCommandsForFunction(*args):
	result = _BNGetValidPluginCommandsForFunction(*args)
	if not result:
		return None
	return result
_BNGetValidPluginCommandsForRange = core.BNGetValidPluginCommandsForRange
_BNGetValidPluginCommandsForRange.restype = ctypes.POINTER(BNPluginCommand)
_BNGetValidPluginCommandsForRange.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNGetValidPluginCommandsForRange(*args):
	result = _BNGetValidPluginCommandsForRange(*args)
	if not result:
		return None
	return result
_BNGetVariableName = core.BNGetVariableName
_BNGetVariableName.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetVariableName.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNVariable),
	]
def BNGetVariableName(*args):
	result = _BNGetVariableName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGetVariableType = core.BNGetVariableType
BNGetVariableType.restype = BNTypeWithConfidence
BNGetVariableType.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNVariable),
	]
_BNGetVersionString = core.BNGetVersionString
_BNGetVersionString.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetVersionString.argtypes = [
	]
def BNGetVersionString(*args):
	result = _BNGetVersionString(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGetVerticalFunctionGraphBlockMargin = core.BNGetVerticalFunctionGraphBlockMargin
BNGetVerticalFunctionGraphBlockMargin.restype = ctypes.c_int
BNGetVerticalFunctionGraphBlockMargin.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
	]
BNGetViewAddressSize = core.BNGetViewAddressSize
BNGetViewAddressSize.restype = ctypes.c_ulonglong
BNGetViewAddressSize.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
BNGetViewLength = core.BNGetViewLength
BNGetViewLength.restype = ctypes.c_ulonglong
BNGetViewLength.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
_BNGetViewType = core.BNGetViewType
_BNGetViewType.restype = ctypes.POINTER(ctypes.c_byte)
_BNGetViewType.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
def BNGetViewType(*args):
	result = _BNGetViewType(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNGetWorkerThreadCount = core.BNGetWorkerThreadCount
BNGetWorkerThreadCount.restype = ctypes.c_ulonglong
BNGetWorkerThreadCount.argtypes = [
	]
BNGetWriterPosition = core.BNGetWriterPosition
BNGetWriterPosition.restype = ctypes.c_ulonglong
BNGetWriterPosition.argtypes = [
		ctypes.POINTER(BNBinaryWriter),
	]
BNHasFunctions = core.BNHasFunctions
BNHasFunctions.restype = ctypes.c_bool
BNHasFunctions.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
_BNImportedFunctionFromImportAddressSymbol = core.BNImportedFunctionFromImportAddressSymbol
_BNImportedFunctionFromImportAddressSymbol.restype = ctypes.POINTER(BNSymbol)
_BNImportedFunctionFromImportAddressSymbol.argtypes = [
		ctypes.POINTER(BNSymbol),
		ctypes.c_ulonglong,
	]
def BNImportedFunctionFromImportAddressSymbol(*args):
	result = _BNImportedFunctionFromImportAddressSymbol(*args)
	if not result:
		return None
	return result
BNInitCorePlugins = core.BNInitCorePlugins
BNInitCorePlugins.restype = None
BNInitCorePlugins.argtypes = [
	]
BNInitRepoPlugins = core.BNInitRepoPlugins
BNInitRepoPlugins.restype = None
BNInitRepoPlugins.argtypes = [
	]
_BNInitScriptingInstance = core.BNInitScriptingInstance
_BNInitScriptingInstance.restype = ctypes.POINTER(BNScriptingInstance)
_BNInitScriptingInstance.argtypes = [
		ctypes.POINTER(BNScriptingProvider),
		ctypes.POINTER(BNScriptingInstanceCallbacks),
	]
def BNInitScriptingInstance(*args):
	result = _BNInitScriptingInstance(*args)
	if not result:
		return None
	return result
BNInitUserPlugins = core.BNInitUserPlugins
BNInitUserPlugins.restype = None
BNInitUserPlugins.argtypes = [
	]
BNInsertViewBuffer = core.BNInsertViewBuffer
BNInsertViewBuffer.restype = ctypes.c_ulonglong
BNInsertViewBuffer.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNDataBuffer),
	]
BNInsertViewData = core.BNInsertViewData
BNInsertViewData.restype = ctypes.c_ulonglong
BNInsertViewData.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.c_void_p,
		ctypes.c_ulonglong,
	]
BNInstallPendingUpdate = core.BNInstallPendingUpdate
BNInstallPendingUpdate.restype = None
BNInstallPendingUpdate.argtypes = [
		ctypes.POINTER(ctypes.c_char_p),
	]
BNInvertBranch = core.BNInvertBranch
BNInvertBranch.restype = ctypes.c_bool
BNInvertBranch.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
BNIsAlwaysBranchPatchAvailable = core.BNIsAlwaysBranchPatchAvailable
BNIsAlwaysBranchPatchAvailable.restype = ctypes.c_bool
BNIsAlwaysBranchPatchAvailable.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
BNIsAnalysisChanged = core.BNIsAnalysisChanged
BNIsAnalysisChanged.restype = ctypes.c_bool
BNIsAnalysisChanged.argtypes = [
		ctypes.POINTER(BNFileMetadata),
	]
BNIsAnalysisTypeAutoDefined = core.BNIsAnalysisTypeAutoDefined
BNIsAnalysisTypeAutoDefined.restype = ctypes.c_bool
BNIsAnalysisTypeAutoDefined.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNQualifiedName),
	]
BNIsArchitectureAlwaysBranchPatchAvailable = core.BNIsArchitectureAlwaysBranchPatchAvailable
BNIsArchitectureAlwaysBranchPatchAvailable.restype = ctypes.c_bool
BNIsArchitectureAlwaysBranchPatchAvailable.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ubyte),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNIsArchitectureGlobalRegister = core.BNIsArchitectureGlobalRegister
BNIsArchitectureGlobalRegister.restype = ctypes.c_bool
BNIsArchitectureGlobalRegister.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_uint,
	]
BNIsArchitectureInvertBranchPatchAvailable = core.BNIsArchitectureInvertBranchPatchAvailable
BNIsArchitectureInvertBranchPatchAvailable.restype = ctypes.c_bool
BNIsArchitectureInvertBranchPatchAvailable.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ubyte),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNIsArchitectureNeverBranchPatchAvailable = core.BNIsArchitectureNeverBranchPatchAvailable
BNIsArchitectureNeverBranchPatchAvailable.restype = ctypes.c_bool
BNIsArchitectureNeverBranchPatchAvailable.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ubyte),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNIsArchitectureSkipAndReturnValuePatchAvailable = core.BNIsArchitectureSkipAndReturnValuePatchAvailable
BNIsArchitectureSkipAndReturnValuePatchAvailable.restype = ctypes.c_bool
BNIsArchitectureSkipAndReturnValuePatchAvailable.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ubyte),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNIsArchitectureSkipAndReturnZeroPatchAvailable = core.BNIsArchitectureSkipAndReturnZeroPatchAvailable
BNIsArchitectureSkipAndReturnZeroPatchAvailable.restype = ctypes.c_bool
BNIsArchitectureSkipAndReturnZeroPatchAvailable.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(ctypes.c_ubyte),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNIsBackedByDatabase = core.BNIsBackedByDatabase
BNIsBackedByDatabase.restype = ctypes.c_bool
BNIsBackedByDatabase.argtypes = [
		ctypes.POINTER(BNFileMetadata),
	]
BNIsBackgroundTaskCancelled = core.BNIsBackgroundTaskCancelled
BNIsBackgroundTaskCancelled.restype = ctypes.c_bool
BNIsBackgroundTaskCancelled.argtypes = [
		ctypes.POINTER(BNBackgroundTask),
	]
BNIsBackgroundTaskFinished = core.BNIsBackgroundTaskFinished
BNIsBackgroundTaskFinished.restype = ctypes.c_bool
BNIsBackgroundTaskFinished.argtypes = [
		ctypes.POINTER(BNBackgroundTask),
	]
BNIsBinaryViewTypeArchitectureConstantDefined = core.BNIsBinaryViewTypeArchitectureConstantDefined
BNIsBinaryViewTypeArchitectureConstantDefined.restype = ctypes.c_bool
BNIsBinaryViewTypeArchitectureConstantDefined.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNIsBinaryViewTypeValidForData = core.BNIsBinaryViewTypeValidForData
BNIsBinaryViewTypeValidForData.restype = ctypes.c_bool
BNIsBinaryViewTypeValidForData.argtypes = [
		ctypes.POINTER(BNBinaryViewType),
		ctypes.POINTER(BNBinaryView),
	]
BNIsDisassemblySettingsOptionSet = core.BNIsDisassemblySettingsOptionSet
BNIsDisassemblySettingsOptionSet.restype = ctypes.c_bool
BNIsDisassemblySettingsOptionSet.argtypes = [
		ctypes.POINTER(BNDisassemblySettings),
		DisassemblyOptionEnum,
	]
BNIsEndOfFile = core.BNIsEndOfFile
BNIsEndOfFile.restype = ctypes.c_bool
BNIsEndOfFile.argtypes = [
		ctypes.POINTER(BNBinaryReader),
	]
BNIsExecutableView = core.BNIsExecutableView
BNIsExecutableView.restype = ctypes.c_bool
BNIsExecutableView.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
BNIsFileModified = core.BNIsFileModified
BNIsFileModified.restype = ctypes.c_bool
BNIsFileModified.argtypes = [
		ctypes.POINTER(BNFileMetadata),
	]
BNIsFunctionGraphLayoutComplete = core.BNIsFunctionGraphLayoutComplete
BNIsFunctionGraphLayoutComplete.restype = ctypes.c_bool
BNIsFunctionGraphLayoutComplete.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
	]
BNIsFunctionGraphOptionSet = core.BNIsFunctionGraphOptionSet
BNIsFunctionGraphOptionSet.restype = ctypes.c_bool
BNIsFunctionGraphOptionSet.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
		DisassemblyOptionEnum,
	]
BNIsFunctionUpdateNeeded = core.BNIsFunctionUpdateNeeded
BNIsFunctionUpdateNeeded.restype = ctypes.c_bool
BNIsFunctionUpdateNeeded.argtypes = [
		ctypes.POINTER(BNFunction),
	]
BNIsInvertBranchPatchAvailable = core.BNIsInvertBranchPatchAvailable
BNIsInvertBranchPatchAvailable.restype = ctypes.c_bool
BNIsInvertBranchPatchAvailable.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
BNIsLicenseValidated = core.BNIsLicenseValidated
BNIsLicenseValidated.restype = ctypes.c_bool
BNIsLicenseValidated.argtypes = [
	]
BNIsMainThreadActionDone = core.BNIsMainThreadActionDone
BNIsMainThreadActionDone.restype = ctypes.c_bool
BNIsMainThreadActionDone.argtypes = [
		ctypes.POINTER(BNMainThreadAction),
	]
BNIsNeverBranchPatchAvailable = core.BNIsNeverBranchPatchAvailable
BNIsNeverBranchPatchAvailable.restype = ctypes.c_bool
BNIsNeverBranchPatchAvailable.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
BNIsOffsetBackedByFile = core.BNIsOffsetBackedByFile
BNIsOffsetBackedByFile.restype = ctypes.c_bool
BNIsOffsetBackedByFile.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNIsOffsetCodeSemantics = core.BNIsOffsetCodeSemantics
BNIsOffsetCodeSemantics.restype = ctypes.c_bool
BNIsOffsetCodeSemantics.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNIsOffsetExecutable = core.BNIsOffsetExecutable
BNIsOffsetExecutable.restype = ctypes.c_bool
BNIsOffsetExecutable.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNIsOffsetReadable = core.BNIsOffsetReadable
BNIsOffsetReadable.restype = ctypes.c_bool
BNIsOffsetReadable.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNIsOffsetWritable = core.BNIsOffsetWritable
BNIsOffsetWritable.restype = ctypes.c_bool
BNIsOffsetWritable.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNIsOffsetWritableSemantics = core.BNIsOffsetWritableSemantics
BNIsOffsetWritableSemantics.restype = ctypes.c_bool
BNIsOffsetWritableSemantics.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNIsPathDirectory = core.BNIsPathDirectory
BNIsPathDirectory.restype = ctypes.c_bool
BNIsPathDirectory.argtypes = [
		ctypes.c_char_p,
	]
BNIsPathRegularFile = core.BNIsPathRegularFile
BNIsPathRegularFile.restype = ctypes.c_bool
BNIsPathRegularFile.argtypes = [
		ctypes.c_char_p,
	]
BNIsSkipAndReturnValuePatchAvailable = core.BNIsSkipAndReturnValuePatchAvailable
BNIsSkipAndReturnValuePatchAvailable.restype = ctypes.c_bool
BNIsSkipAndReturnValuePatchAvailable.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
BNIsSkipAndReturnZeroPatchAvailable = core.BNIsSkipAndReturnZeroPatchAvailable
BNIsSkipAndReturnZeroPatchAvailable.restype = ctypes.c_bool
BNIsSkipAndReturnZeroPatchAvailable.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
BNIsStackAdjustedOnReturn = core.BNIsStackAdjustedOnReturn
BNIsStackAdjustedOnReturn.restype = ctypes.c_bool
BNIsStackAdjustedOnReturn.argtypes = [
		ctypes.POINTER(BNCallingConvention),
	]
BNIsStackReservedForArgumentRegisters = core.BNIsStackReservedForArgumentRegisters
BNIsStackReservedForArgumentRegisters.restype = ctypes.c_bool
BNIsStackReservedForArgumentRegisters.argtypes = [
		ctypes.POINTER(BNCallingConvention),
	]
BNIsStructurePacked = core.BNIsStructurePacked
BNIsStructurePacked.restype = ctypes.c_bool
BNIsStructurePacked.argtypes = [
		ctypes.POINTER(BNStructure),
	]
BNIsStructureUnion = core.BNIsStructureUnion
BNIsStructureUnion.restype = ctypes.c_bool
BNIsStructureUnion.argtypes = [
		ctypes.POINTER(BNStructure),
	]
BNIsSymbolAutoDefined = core.BNIsSymbolAutoDefined
BNIsSymbolAutoDefined.restype = ctypes.c_bool
BNIsSymbolAutoDefined.argtypes = [
		ctypes.POINTER(BNSymbol),
	]
BNIsTypeConst = core.BNIsTypeConst
BNIsTypeConst.restype = BNBoolWithConfidence
BNIsTypeConst.argtypes = [
		ctypes.POINTER(BNType),
	]
BNIsTypeFloatingPoint = core.BNIsTypeFloatingPoint
BNIsTypeFloatingPoint.restype = ctypes.c_bool
BNIsTypeFloatingPoint.argtypes = [
		ctypes.POINTER(BNType),
	]
BNIsTypeSigned = core.BNIsTypeSigned
BNIsTypeSigned.restype = BNBoolWithConfidence
BNIsTypeSigned.argtypes = [
		ctypes.POINTER(BNType),
	]
BNIsTypeVolatile = core.BNIsTypeVolatile
BNIsTypeVolatile.restype = BNBoolWithConfidence
BNIsTypeVolatile.argtypes = [
		ctypes.POINTER(BNType),
	]
BNIsUIEnabled = core.BNIsUIEnabled
BNIsUIEnabled.restype = ctypes.c_bool
BNIsUIEnabled.argtypes = [
	]
BNIsUpdateInstallationPending = core.BNIsUpdateInstallationPending
BNIsUpdateInstallationPending.restype = ctypes.c_bool
BNIsUpdateInstallationPending.argtypes = [
	]
BNIsValidOffset = core.BNIsValidOffset
BNIsValidOffset.restype = ctypes.c_bool
BNIsValidOffset.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNIsViewModified = core.BNIsViewModified
BNIsViewModified.restype = ctypes.c_bool
BNIsViewModified.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
BNLlvmServicesAssemble = core.BNLlvmServicesAssemble
BNLlvmServicesAssemble.restype = ctypes.c_int
BNLlvmServicesAssemble.argtypes = [
		ctypes.c_char_p,
		ctypes.c_int,
		ctypes.c_char_p,
		ctypes.c_int,
		ctypes.c_int,
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.POINTER(ctypes.c_int),
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.POINTER(ctypes.c_int),
	]
BNLlvmServicesAssembleFree = core.BNLlvmServicesAssembleFree
BNLlvmServicesAssembleFree.restype = None
BNLlvmServicesAssembleFree.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNLlvmServicesInit = core.BNLlvmServicesInit
BNLlvmServicesInit.restype = None
BNLlvmServicesInit.argtypes = [
	]
BNLoadPluginForApi = core.BNLoadPluginForApi
BNLoadPluginForApi.restype = ctypes.c_bool
BNLoadPluginForApi.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNLog = core.BNLog
BNLog.restype = None
BNLogAlert = core.BNLogAlert
BNLogAlert.restype = None
BNLogDebug = core.BNLogDebug
BNLogDebug.restype = None
BNLogError = core.BNLogError
BNLogError.restype = None
BNLogInfo = core.BNLogInfo
BNLogInfo.restype = None
BNLogToFile = core.BNLogToFile
BNLogToFile.restype = ctypes.c_bool
BNLogToFile.argtypes = [
		LogLevelEnum,
		ctypes.c_char_p,
		ctypes.c_bool,
	]
BNLogToStderr = core.BNLogToStderr
BNLogToStderr.restype = None
BNLogToStderr.argtypes = [
		LogLevelEnum,
	]
BNLogToStdout = core.BNLogToStdout
BNLogToStdout.restype = None
BNLogToStdout.argtypes = [
		LogLevelEnum,
	]
BNLogWarn = core.BNLogWarn
BNLogWarn.restype = None
BNLowLevelILAddExpr = core.BNLowLevelILAddExpr
BNLowLevelILAddExpr.restype = ctypes.c_ulonglong
BNLowLevelILAddExpr.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		LowLevelILOperationEnum,
		ctypes.c_ulonglong,
		ctypes.c_uint,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNLowLevelILAddExprWithLocation = core.BNLowLevelILAddExprWithLocation
BNLowLevelILAddExprWithLocation.restype = ctypes.c_ulonglong
BNLowLevelILAddExprWithLocation.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
		ctypes.c_uint,
		LowLevelILOperationEnum,
		ctypes.c_ulonglong,
		ctypes.c_uint,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNLowLevelILAddInstruction = core.BNLowLevelILAddInstruction
BNLowLevelILAddInstruction.restype = ctypes.c_ulonglong
BNLowLevelILAddInstruction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
	]
BNLowLevelILAddLabelList = core.BNLowLevelILAddLabelList
BNLowLevelILAddLabelList.restype = ctypes.c_ulonglong
BNLowLevelILAddLabelList.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.POINTER(ctypes.POINTER(BNLowLevelILLabel)),
		ctypes.c_ulonglong,
	]
BNLowLevelILAddOperandList = core.BNLowLevelILAddOperandList
BNLowLevelILAddOperandList.restype = ctypes.c_ulonglong
BNLowLevelILAddOperandList.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.POINTER(ctypes.c_ulonglong),
		ctypes.c_ulonglong,
	]
BNLowLevelILClearIndirectBranches = core.BNLowLevelILClearIndirectBranches
BNLowLevelILClearIndirectBranches.restype = None
BNLowLevelILClearIndirectBranches.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
	]
BNLowLevelILFreeOperandList = core.BNLowLevelILFreeOperandList
BNLowLevelILFreeOperandList.restype = None
BNLowLevelILFreeOperandList.argtypes = [
		ctypes.POINTER(ctypes.c_ulonglong),
	]
BNLowLevelILGetCurrentAddress = core.BNLowLevelILGetCurrentAddress
BNLowLevelILGetCurrentAddress.restype = ctypes.c_ulonglong
BNLowLevelILGetCurrentAddress.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
	]
BNLowLevelILGetInstructionStart = core.BNLowLevelILGetInstructionStart
BNLowLevelILGetInstructionStart.restype = ctypes.c_ulonglong
BNLowLevelILGetInstructionStart.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
_BNLowLevelILGetOperandList = core.BNLowLevelILGetOperandList
_BNLowLevelILGetOperandList.restype = ctypes.POINTER(ctypes.c_ulonglong)
_BNLowLevelILGetOperandList.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNLowLevelILGetOperandList(*args):
	result = _BNLowLevelILGetOperandList(*args)
	if not result:
		return None
	return result
BNLowLevelILGoto = core.BNLowLevelILGoto
BNLowLevelILGoto.restype = ctypes.c_ulonglong
BNLowLevelILGoto.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.POINTER(BNLowLevelILLabel),
	]
BNLowLevelILGotoWithLocation = core.BNLowLevelILGotoWithLocation
BNLowLevelILGotoWithLocation.restype = ctypes.c_ulonglong
BNLowLevelILGotoWithLocation.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.POINTER(BNLowLevelILLabel),
		ctypes.c_ulonglong,
		ctypes.c_uint,
	]
BNLowLevelILIf = core.BNLowLevelILIf
BNLowLevelILIf.restype = ctypes.c_ulonglong
BNLowLevelILIf.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNLowLevelILLabel),
		ctypes.POINTER(BNLowLevelILLabel),
	]
BNLowLevelILIfWithLocation = core.BNLowLevelILIfWithLocation
BNLowLevelILIfWithLocation.restype = ctypes.c_ulonglong
BNLowLevelILIfWithLocation.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNLowLevelILLabel),
		ctypes.POINTER(BNLowLevelILLabel),
		ctypes.c_ulonglong,
		ctypes.c_uint,
	]
BNLowLevelILInitLabel = core.BNLowLevelILInitLabel
BNLowLevelILInitLabel.restype = None
BNLowLevelILInitLabel.argtypes = [
		ctypes.POINTER(BNLowLevelILLabel),
	]
BNLowLevelILMarkLabel = core.BNLowLevelILMarkLabel
BNLowLevelILMarkLabel.restype = None
BNLowLevelILMarkLabel.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.POINTER(BNLowLevelILLabel),
	]
BNLowLevelILSetCurrentAddress = core.BNLowLevelILSetCurrentAddress
BNLowLevelILSetCurrentAddress.restype = None
BNLowLevelILSetCurrentAddress.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
BNLowLevelILSetExprSourceOperand = core.BNLowLevelILSetExprSourceOperand
BNLowLevelILSetExprSourceOperand.restype = None
BNLowLevelILSetExprSourceOperand.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
		ctypes.c_uint,
	]
BNLowLevelILSetIndirectBranches = core.BNLowLevelILSetIndirectBranches
BNLowLevelILSetIndirectBranches.restype = None
BNLowLevelILSetIndirectBranches.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.POINTER(BNArchitectureAndAddress),
		ctypes.c_ulonglong,
	]
BNMarkBasicBlockAsRecentlyUsed = core.BNMarkBasicBlockAsRecentlyUsed
BNMarkBasicBlockAsRecentlyUsed.restype = None
BNMarkBasicBlockAsRecentlyUsed.argtypes = [
		ctypes.POINTER(BNBasicBlock),
	]
BNMarkFileModified = core.BNMarkFileModified
BNMarkFileModified.restype = None
BNMarkFileModified.argtypes = [
		ctypes.POINTER(BNFileMetadata),
	]
BNMarkFileSaved = core.BNMarkFileSaved
BNMarkFileSaved.restype = None
BNMarkFileSaved.argtypes = [
		ctypes.POINTER(BNFileMetadata),
	]
BNMarkFunctionAsRecentlyUsed = core.BNMarkFunctionAsRecentlyUsed
BNMarkFunctionAsRecentlyUsed.restype = None
BNMarkFunctionAsRecentlyUsed.argtypes = [
		ctypes.POINTER(BNFunction),
	]
BNMarkMediumLevelILInstructionForRemoval = core.BNMarkMediumLevelILInstructionForRemoval
BNMarkMediumLevelILInstructionForRemoval.restype = None
BNMarkMediumLevelILInstructionForRemoval.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
	]
_BNMarkdownToHTML = core.BNMarkdownToHTML
_BNMarkdownToHTML.restype = ctypes.POINTER(ctypes.c_byte)
_BNMarkdownToHTML.argtypes = [
		ctypes.c_char_p,
	]
def BNMarkdownToHTML(*args):
	result = _BNMarkdownToHTML(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNMediumLevelILAddExpr = core.BNMediumLevelILAddExpr
BNMediumLevelILAddExpr.restype = ctypes.c_ulonglong
BNMediumLevelILAddExpr.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		MediumLevelILOperationEnum,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNMediumLevelILAddExprWithLocation = core.BNMediumLevelILAddExprWithLocation
BNMediumLevelILAddExprWithLocation.restype = ctypes.c_ulonglong
BNMediumLevelILAddExprWithLocation.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		MediumLevelILOperationEnum,
		ctypes.c_ulonglong,
		ctypes.c_uint,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNMediumLevelILAddInstruction = core.BNMediumLevelILAddInstruction
BNMediumLevelILAddInstruction.restype = ctypes.c_ulonglong
BNMediumLevelILAddInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
	]
BNMediumLevelILAddLabelList = core.BNMediumLevelILAddLabelList
BNMediumLevelILAddLabelList.restype = ctypes.c_ulonglong
BNMediumLevelILAddLabelList.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(ctypes.POINTER(BNMediumLevelILLabel)),
		ctypes.c_ulonglong,
	]
BNMediumLevelILAddOperandList = core.BNMediumLevelILAddOperandList
BNMediumLevelILAddOperandList.restype = ctypes.c_ulonglong
BNMediumLevelILAddOperandList.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(ctypes.c_ulonglong),
		ctypes.c_ulonglong,
	]
BNMediumLevelILFreeOperandList = core.BNMediumLevelILFreeOperandList
BNMediumLevelILFreeOperandList.restype = None
BNMediumLevelILFreeOperandList.argtypes = [
		ctypes.POINTER(ctypes.c_ulonglong),
	]
BNMediumLevelILGetCurrentAddress = core.BNMediumLevelILGetCurrentAddress
BNMediumLevelILGetCurrentAddress.restype = ctypes.c_ulonglong
BNMediumLevelILGetCurrentAddress.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
	]
BNMediumLevelILGetInstructionStart = core.BNMediumLevelILGetInstructionStart
BNMediumLevelILGetInstructionStart.restype = ctypes.c_ulonglong
BNMediumLevelILGetInstructionStart.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
_BNMediumLevelILGetOperandList = core.BNMediumLevelILGetOperandList
_BNMediumLevelILGetOperandList.restype = ctypes.POINTER(ctypes.c_ulonglong)
_BNMediumLevelILGetOperandList.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNMediumLevelILGetOperandList(*args):
	result = _BNMediumLevelILGetOperandList(*args)
	if not result:
		return None
	return result
BNMediumLevelILGoto = core.BNMediumLevelILGoto
BNMediumLevelILGoto.restype = ctypes.c_ulonglong
BNMediumLevelILGoto.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(BNMediumLevelILLabel),
	]
BNMediumLevelILGotoWithLocation = core.BNMediumLevelILGotoWithLocation
BNMediumLevelILGotoWithLocation.restype = ctypes.c_ulonglong
BNMediumLevelILGotoWithLocation.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(BNMediumLevelILLabel),
		ctypes.c_ulonglong,
		ctypes.c_uint,
	]
BNMediumLevelILIf = core.BNMediumLevelILIf
BNMediumLevelILIf.restype = ctypes.c_ulonglong
BNMediumLevelILIf.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNMediumLevelILLabel),
		ctypes.POINTER(BNMediumLevelILLabel),
	]
BNMediumLevelILIfWithLocation = core.BNMediumLevelILIfWithLocation
BNMediumLevelILIfWithLocation.restype = ctypes.c_ulonglong
BNMediumLevelILIfWithLocation.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNMediumLevelILLabel),
		ctypes.POINTER(BNMediumLevelILLabel),
		ctypes.c_ulonglong,
		ctypes.c_uint,
	]
BNMediumLevelILInitLabel = core.BNMediumLevelILInitLabel
BNMediumLevelILInitLabel.restype = None
BNMediumLevelILInitLabel.argtypes = [
		ctypes.POINTER(BNMediumLevelILLabel),
	]
BNMediumLevelILMarkLabel = core.BNMediumLevelILMarkLabel
BNMediumLevelILMarkLabel.restype = None
BNMediumLevelILMarkLabel.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(BNMediumLevelILLabel),
	]
BNMediumLevelILSetCurrentAddress = core.BNMediumLevelILSetCurrentAddress
BNMediumLevelILSetCurrentAddress.restype = None
BNMediumLevelILSetCurrentAddress.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
	]
BNMetadataArrayAppend = core.BNMetadataArrayAppend
BNMetadataArrayAppend.restype = ctypes.c_bool
BNMetadataArrayAppend.argtypes = [
		ctypes.POINTER(BNMetadata),
		ctypes.POINTER(BNMetadata),
	]
_BNMetadataGetArray = core.BNMetadataGetArray
_BNMetadataGetArray.restype = ctypes.POINTER(ctypes.POINTER(BNMetadata))
_BNMetadataGetArray.argtypes = [
		ctypes.POINTER(BNMetadata),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNMetadataGetArray(*args):
	result = _BNMetadataGetArray(*args)
	if not result:
		return None
	return result
BNMetadataGetBoolean = core.BNMetadataGetBoolean
BNMetadataGetBoolean.restype = ctypes.c_bool
BNMetadataGetBoolean.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
BNMetadataGetDouble = core.BNMetadataGetDouble
BNMetadataGetDouble.restype = ctypes.c_double
BNMetadataGetDouble.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
_BNMetadataGetForIndex = core.BNMetadataGetForIndex
_BNMetadataGetForIndex.restype = ctypes.POINTER(BNMetadata)
_BNMetadataGetForIndex.argtypes = [
		ctypes.POINTER(BNMetadata),
		ctypes.c_ulonglong,
	]
def BNMetadataGetForIndex(*args):
	result = _BNMetadataGetForIndex(*args)
	if not result:
		return None
	return result
_BNMetadataGetForKey = core.BNMetadataGetForKey
_BNMetadataGetForKey.restype = ctypes.POINTER(BNMetadata)
_BNMetadataGetForKey.argtypes = [
		ctypes.POINTER(BNMetadata),
		ctypes.c_char_p,
	]
def BNMetadataGetForKey(*args):
	result = _BNMetadataGetForKey(*args)
	if not result:
		return None
	return result
_BNMetadataGetRaw = core.BNMetadataGetRaw
_BNMetadataGetRaw.restype = ctypes.POINTER(ctypes.c_ubyte)
_BNMetadataGetRaw.argtypes = [
		ctypes.POINTER(BNMetadata),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNMetadataGetRaw(*args):
	result = _BNMetadataGetRaw(*args)
	if not result:
		return None
	return result
BNMetadataGetSignedInteger = core.BNMetadataGetSignedInteger
BNMetadataGetSignedInteger.restype = ctypes.c_longlong
BNMetadataGetSignedInteger.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
_BNMetadataGetString = core.BNMetadataGetString
_BNMetadataGetString.restype = ctypes.POINTER(ctypes.c_byte)
_BNMetadataGetString.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
def BNMetadataGetString(*args):
	result = _BNMetadataGetString(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNMetadataGetType = core.BNMetadataGetType
BNMetadataGetType.restype = MetadataTypeEnum
BNMetadataGetType.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
BNMetadataGetUnsignedInteger = core.BNMetadataGetUnsignedInteger
BNMetadataGetUnsignedInteger.restype = ctypes.c_ulonglong
BNMetadataGetUnsignedInteger.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
_BNMetadataGetValueStore = core.BNMetadataGetValueStore
_BNMetadataGetValueStore.restype = ctypes.POINTER(BNMetadataValueStore)
_BNMetadataGetValueStore.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
def BNMetadataGetValueStore(*args):
	result = _BNMetadataGetValueStore(*args)
	if not result:
		return None
	return result
BNMetadataIsArray = core.BNMetadataIsArray
BNMetadataIsArray.restype = ctypes.c_bool
BNMetadataIsArray.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
BNMetadataIsBoolean = core.BNMetadataIsBoolean
BNMetadataIsBoolean.restype = ctypes.c_bool
BNMetadataIsBoolean.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
BNMetadataIsDouble = core.BNMetadataIsDouble
BNMetadataIsDouble.restype = ctypes.c_bool
BNMetadataIsDouble.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
BNMetadataIsEqual = core.BNMetadataIsEqual
BNMetadataIsEqual.restype = ctypes.c_bool
BNMetadataIsEqual.argtypes = [
		ctypes.POINTER(BNMetadata),
		ctypes.POINTER(BNMetadata),
	]
BNMetadataIsKeyValueStore = core.BNMetadataIsKeyValueStore
BNMetadataIsKeyValueStore.restype = ctypes.c_bool
BNMetadataIsKeyValueStore.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
BNMetadataIsRaw = core.BNMetadataIsRaw
BNMetadataIsRaw.restype = ctypes.c_bool
BNMetadataIsRaw.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
BNMetadataIsSignedInteger = core.BNMetadataIsSignedInteger
BNMetadataIsSignedInteger.restype = ctypes.c_bool
BNMetadataIsSignedInteger.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
BNMetadataIsString = core.BNMetadataIsString
BNMetadataIsString.restype = ctypes.c_bool
BNMetadataIsString.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
BNMetadataIsUnsignedInteger = core.BNMetadataIsUnsignedInteger
BNMetadataIsUnsignedInteger.restype = ctypes.c_bool
BNMetadataIsUnsignedInteger.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
BNMetadataRemoveIndex = core.BNMetadataRemoveIndex
BNMetadataRemoveIndex.restype = None
BNMetadataRemoveIndex.argtypes = [
		ctypes.POINTER(BNMetadata),
		ctypes.c_ulonglong,
	]
BNMetadataRemoveKey = core.BNMetadataRemoveKey
BNMetadataRemoveKey.restype = None
BNMetadataRemoveKey.argtypes = [
		ctypes.POINTER(BNMetadata),
		ctypes.c_char_p,
	]
BNMetadataSetValueForKey = core.BNMetadataSetValueForKey
BNMetadataSetValueForKey.restype = ctypes.c_bool
BNMetadataSetValueForKey.argtypes = [
		ctypes.POINTER(BNMetadata),
		ctypes.c_char_p,
		ctypes.POINTER(BNMetadata),
	]
BNMetadataSize = core.BNMetadataSize
BNMetadataSize.restype = ctypes.c_ulonglong
BNMetadataSize.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
BNNavigate = core.BNNavigate
BNNavigate.restype = ctypes.c_bool
BNNavigate.argtypes = [
		ctypes.POINTER(BNFileMetadata),
		ctypes.c_char_p,
		ctypes.c_ulonglong,
	]
_BNNewAnalysisCompletionEventReference = core.BNNewAnalysisCompletionEventReference
_BNNewAnalysisCompletionEventReference.restype = ctypes.POINTER(BNAnalysisCompletionEvent)
_BNNewAnalysisCompletionEventReference.argtypes = [
		ctypes.POINTER(BNAnalysisCompletionEvent),
	]
def BNNewAnalysisCompletionEventReference(*args):
	result = _BNNewAnalysisCompletionEventReference(*args)
	if not result:
		return None
	return result
_BNNewBackgroundTaskReference = core.BNNewBackgroundTaskReference
_BNNewBackgroundTaskReference.restype = ctypes.POINTER(BNBackgroundTask)
_BNNewBackgroundTaskReference.argtypes = [
		ctypes.POINTER(BNBackgroundTask),
	]
def BNNewBackgroundTaskReference(*args):
	result = _BNNewBackgroundTaskReference(*args)
	if not result:
		return None
	return result
_BNNewBasicBlockReference = core.BNNewBasicBlockReference
_BNNewBasicBlockReference.restype = ctypes.POINTER(BNBasicBlock)
_BNNewBasicBlockReference.argtypes = [
		ctypes.POINTER(BNBasicBlock),
	]
def BNNewBasicBlockReference(*args):
	result = _BNNewBasicBlockReference(*args)
	if not result:
		return None
	return result
_BNNewCallingConventionReference = core.BNNewCallingConventionReference
_BNNewCallingConventionReference.restype = ctypes.POINTER(BNCallingConvention)
_BNNewCallingConventionReference.argtypes = [
		ctypes.POINTER(BNCallingConvention),
	]
def BNNewCallingConventionReference(*args):
	result = _BNNewCallingConventionReference(*args)
	if not result:
		return None
	return result
_BNNewDisassemblySettingsReference = core.BNNewDisassemblySettingsReference
_BNNewDisassemblySettingsReference.restype = ctypes.POINTER(BNDisassemblySettings)
_BNNewDisassemblySettingsReference.argtypes = [
		ctypes.POINTER(BNDisassemblySettings),
	]
def BNNewDisassemblySettingsReference(*args):
	result = _BNNewDisassemblySettingsReference(*args)
	if not result:
		return None
	return result
_BNNewEnumerationReference = core.BNNewEnumerationReference
_BNNewEnumerationReference.restype = ctypes.POINTER(BNEnumeration)
_BNNewEnumerationReference.argtypes = [
		ctypes.POINTER(BNEnumeration),
	]
def BNNewEnumerationReference(*args):
	result = _BNNewEnumerationReference(*args)
	if not result:
		return None
	return result
_BNNewFileReference = core.BNNewFileReference
_BNNewFileReference.restype = ctypes.POINTER(BNFileMetadata)
_BNNewFileReference.argtypes = [
		ctypes.POINTER(BNFileMetadata),
	]
def BNNewFileReference(*args):
	result = _BNNewFileReference(*args)
	if not result:
		return None
	return result
_BNNewFunctionGraphBlockReference = core.BNNewFunctionGraphBlockReference
_BNNewFunctionGraphBlockReference.restype = ctypes.POINTER(BNFunctionGraphBlock)
_BNNewFunctionGraphBlockReference.argtypes = [
		ctypes.POINTER(BNFunctionGraphBlock),
	]
def BNNewFunctionGraphBlockReference(*args):
	result = _BNNewFunctionGraphBlockReference(*args)
	if not result:
		return None
	return result
_BNNewFunctionGraphReference = core.BNNewFunctionGraphReference
_BNNewFunctionGraphReference.restype = ctypes.POINTER(BNFunctionGraph)
_BNNewFunctionGraphReference.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
	]
def BNNewFunctionGraphReference(*args):
	result = _BNNewFunctionGraphReference(*args)
	if not result:
		return None
	return result
_BNNewFunctionReference = core.BNNewFunctionReference
_BNNewFunctionReference.restype = ctypes.POINTER(BNFunction)
_BNNewFunctionReference.argtypes = [
		ctypes.POINTER(BNFunction),
	]
def BNNewFunctionReference(*args):
	result = _BNNewFunctionReference(*args)
	if not result:
		return None
	return result
_BNNewLowLevelILFunctionReference = core.BNNewLowLevelILFunctionReference
_BNNewLowLevelILFunctionReference.restype = ctypes.POINTER(BNLowLevelILFunction)
_BNNewLowLevelILFunctionReference.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
	]
def BNNewLowLevelILFunctionReference(*args):
	result = _BNNewLowLevelILFunctionReference(*args)
	if not result:
		return None
	return result
_BNNewMainThreadActionReference = core.BNNewMainThreadActionReference
_BNNewMainThreadActionReference.restype = ctypes.POINTER(BNMainThreadAction)
_BNNewMainThreadActionReference.argtypes = [
		ctypes.POINTER(BNMainThreadAction),
	]
def BNNewMainThreadActionReference(*args):
	result = _BNNewMainThreadActionReference(*args)
	if not result:
		return None
	return result
_BNNewMediumLevelILFunctionReference = core.BNNewMediumLevelILFunctionReference
_BNNewMediumLevelILFunctionReference.restype = ctypes.POINTER(BNMediumLevelILFunction)
_BNNewMediumLevelILFunctionReference.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
	]
def BNNewMediumLevelILFunctionReference(*args):
	result = _BNNewMediumLevelILFunctionReference(*args)
	if not result:
		return None
	return result
_BNNewMetadataReference = core.BNNewMetadataReference
_BNNewMetadataReference.restype = ctypes.POINTER(BNMetadata)
_BNNewMetadataReference.argtypes = [
		ctypes.POINTER(BNMetadata),
	]
def BNNewMetadataReference(*args):
	result = _BNNewMetadataReference(*args)
	if not result:
		return None
	return result
_BNNewNamedTypeReference = core.BNNewNamedTypeReference
_BNNewNamedTypeReference.restype = ctypes.POINTER(BNNamedTypeReference)
_BNNewNamedTypeReference.argtypes = [
		ctypes.POINTER(BNNamedTypeReference),
	]
def BNNewNamedTypeReference(*args):
	result = _BNNewNamedTypeReference(*args)
	if not result:
		return None
	return result
_BNNewPlatformReference = core.BNNewPlatformReference
_BNNewPlatformReference.restype = ctypes.POINTER(BNPlatform)
_BNNewPlatformReference.argtypes = [
		ctypes.POINTER(BNPlatform),
	]
def BNNewPlatformReference(*args):
	result = _BNNewPlatformReference(*args)
	if not result:
		return None
	return result
_BNNewPluginReference = core.BNNewPluginReference
_BNNewPluginReference.restype = ctypes.POINTER(BNRepoPlugin)
_BNNewPluginReference.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
def BNNewPluginReference(*args):
	result = _BNNewPluginReference(*args)
	if not result:
		return None
	return result
_BNNewRepositoryManagerReference = core.BNNewRepositoryManagerReference
_BNNewRepositoryManagerReference.restype = ctypes.POINTER(BNRepositoryManager)
_BNNewRepositoryManagerReference.argtypes = [
		ctypes.POINTER(BNRepositoryManager),
	]
def BNNewRepositoryManagerReference(*args):
	result = _BNNewRepositoryManagerReference(*args)
	if not result:
		return None
	return result
_BNNewRepositoryReference = core.BNNewRepositoryReference
_BNNewRepositoryReference.restype = ctypes.POINTER(BNRepository)
_BNNewRepositoryReference.argtypes = [
		ctypes.POINTER(BNRepository),
	]
def BNNewRepositoryReference(*args):
	result = _BNNewRepositoryReference(*args)
	if not result:
		return None
	return result
_BNNewScriptingInstanceReference = core.BNNewScriptingInstanceReference
_BNNewScriptingInstanceReference.restype = ctypes.POINTER(BNScriptingInstance)
_BNNewScriptingInstanceReference.argtypes = [
		ctypes.POINTER(BNScriptingInstance),
	]
def BNNewScriptingInstanceReference(*args):
	result = _BNNewScriptingInstanceReference(*args)
	if not result:
		return None
	return result
_BNNewStructureReference = core.BNNewStructureReference
_BNNewStructureReference.restype = ctypes.POINTER(BNStructure)
_BNNewStructureReference.argtypes = [
		ctypes.POINTER(BNStructure),
	]
def BNNewStructureReference(*args):
	result = _BNNewStructureReference(*args)
	if not result:
		return None
	return result
_BNNewSymbolReference = core.BNNewSymbolReference
_BNNewSymbolReference.restype = ctypes.POINTER(BNSymbol)
_BNNewSymbolReference.argtypes = [
		ctypes.POINTER(BNSymbol),
	]
def BNNewSymbolReference(*args):
	result = _BNNewSymbolReference(*args)
	if not result:
		return None
	return result
_BNNewTemporaryFileReference = core.BNNewTemporaryFileReference
_BNNewTemporaryFileReference.restype = ctypes.POINTER(BNTemporaryFile)
_BNNewTemporaryFileReference.argtypes = [
		ctypes.POINTER(BNTemporaryFile),
	]
def BNNewTemporaryFileReference(*args):
	result = _BNNewTemporaryFileReference(*args)
	if not result:
		return None
	return result
_BNNewTypeReference = core.BNNewTypeReference
_BNNewTypeReference.restype = ctypes.POINTER(BNType)
_BNNewTypeReference.argtypes = [
		ctypes.POINTER(BNType),
	]
def BNNewTypeReference(*args):
	result = _BNNewTypeReference(*args)
	if not result:
		return None
	return result
_BNNewViewReference = core.BNNewViewReference
_BNNewViewReference.restype = ctypes.POINTER(BNBinaryView)
_BNNewViewReference.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
def BNNewViewReference(*args):
	result = _BNNewViewReference(*args)
	if not result:
		return None
	return result
BNNotifyDataInserted = core.BNNotifyDataInserted
BNNotifyDataInserted.restype = None
BNNotifyDataInserted.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNNotifyDataRemoved = core.BNNotifyDataRemoved
BNNotifyDataRemoved.restype = None
BNNotifyDataRemoved.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNNotifyDataWritten = core.BNNotifyDataWritten
BNNotifyDataWritten.restype = None
BNNotifyDataWritten.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNNotifyErrorForScriptingInstance = core.BNNotifyErrorForScriptingInstance
BNNotifyErrorForScriptingInstance.restype = None
BNNotifyErrorForScriptingInstance.argtypes = [
		ctypes.POINTER(BNScriptingInstance),
		ctypes.c_char_p,
	]
BNNotifyInputReadyStateForScriptingInstance = core.BNNotifyInputReadyStateForScriptingInstance
BNNotifyInputReadyStateForScriptingInstance.restype = None
BNNotifyInputReadyStateForScriptingInstance.argtypes = [
		ctypes.POINTER(BNScriptingInstance),
		ScriptingProviderInputReadyStateEnum,
	]
BNNotifyOutputForScriptingInstance = core.BNNotifyOutputForScriptingInstance
BNNotifyOutputForScriptingInstance.restype = None
BNNotifyOutputForScriptingInstance.argtypes = [
		ctypes.POINTER(BNScriptingInstance),
		ctypes.c_char_p,
	]
_BNOpenExistingDatabase = core.BNOpenExistingDatabase
_BNOpenExistingDatabase.restype = ctypes.POINTER(BNBinaryView)
_BNOpenExistingDatabase.argtypes = [
		ctypes.POINTER(BNFileMetadata),
		ctypes.c_char_p,
	]
def BNOpenExistingDatabase(*args):
	result = _BNOpenExistingDatabase(*args)
	if not result:
		return None
	return result
_BNOpenExistingDatabaseWithProgress = core.BNOpenExistingDatabaseWithProgress
_BNOpenExistingDatabaseWithProgress.restype = ctypes.POINTER(BNBinaryView)
_BNOpenExistingDatabaseWithProgress.argtypes = [
		ctypes.POINTER(BNFileMetadata),
		ctypes.c_char_p,
		ctypes.c_void_p,
		ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_ulonglong),
	]
def BNOpenExistingDatabaseWithProgress(*args):
	result = _BNOpenExistingDatabaseWithProgress(*args)
	if not result:
		return None
	return result
BNParseTypeString = core.BNParseTypeString
BNParseTypeString.restype = ctypes.c_bool
BNParseTypeString.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
		ctypes.POINTER(BNQualifiedNameAndType),
		ctypes.POINTER(ctypes.c_char_p),
	]
BNParseTypesFromSource = core.BNParseTypesFromSource
BNParseTypesFromSource.restype = ctypes.c_bool
BNParseTypesFromSource.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.POINTER(BNTypeParserResult),
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.c_ulonglong,
		ctypes.c_char_p,
	]
BNParseTypesFromSourceFile = core.BNParseTypesFromSourceFile
BNParseTypesFromSourceFile.restype = ctypes.c_bool
BNParseTypesFromSourceFile.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.c_char_p,
		ctypes.POINTER(BNTypeParserResult),
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.c_ulonglong,
		ctypes.c_char_p,
	]
BNPathExists = core.BNPathExists
BNPathExists.restype = ctypes.c_bool
BNPathExists.argtypes = [
		ctypes.c_char_p,
	]
BNPluginDisable = core.BNPluginDisable
BNPluginDisable.restype = ctypes.c_bool
BNPluginDisable.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
BNPluginEnable = core.BNPluginEnable
BNPluginEnable.restype = ctypes.c_bool
BNPluginEnable.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
_BNPluginGetApi = core.BNPluginGetApi
_BNPluginGetApi.restype = ctypes.POINTER(ctypes.c_byte)
_BNPluginGetApi.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
def BNPluginGetApi(*args):
	result = _BNPluginGetApi(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNPluginGetAuthor = core.BNPluginGetAuthor
_BNPluginGetAuthor.restype = ctypes.POINTER(ctypes.c_byte)
_BNPluginGetAuthor.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
def BNPluginGetAuthor(*args):
	result = _BNPluginGetAuthor(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNPluginGetDescription = core.BNPluginGetDescription
_BNPluginGetDescription.restype = ctypes.POINTER(ctypes.c_byte)
_BNPluginGetDescription.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
def BNPluginGetDescription(*args):
	result = _BNPluginGetDescription(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNPluginGetLicense = core.BNPluginGetLicense
_BNPluginGetLicense.restype = ctypes.POINTER(ctypes.c_byte)
_BNPluginGetLicense.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
def BNPluginGetLicense(*args):
	result = _BNPluginGetLicense(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNPluginGetLicenseText = core.BNPluginGetLicenseText
_BNPluginGetLicenseText.restype = ctypes.POINTER(ctypes.c_byte)
_BNPluginGetLicenseText.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
def BNPluginGetLicenseText(*args):
	result = _BNPluginGetLicenseText(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNPluginGetLongdescription = core.BNPluginGetLongdescription
_BNPluginGetLongdescription.restype = ctypes.POINTER(ctypes.c_byte)
_BNPluginGetLongdescription.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
def BNPluginGetLongdescription(*args):
	result = _BNPluginGetLongdescription(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNPluginGetMinimimVersions = core.BNPluginGetMinimimVersions
_BNPluginGetMinimimVersions.restype = ctypes.POINTER(ctypes.c_byte)
_BNPluginGetMinimimVersions.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
def BNPluginGetMinimimVersions(*args):
	result = _BNPluginGetMinimimVersions(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNPluginGetName = core.BNPluginGetName
_BNPluginGetName.restype = ctypes.POINTER(ctypes.c_byte)
_BNPluginGetName.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
def BNPluginGetName(*args):
	result = _BNPluginGetName(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNPluginGetPath = core.BNPluginGetPath
_BNPluginGetPath.restype = ctypes.POINTER(ctypes.c_byte)
_BNPluginGetPath.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
def BNPluginGetPath(*args):
	result = _BNPluginGetPath(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNPluginGetPluginTypes = core.BNPluginGetPluginTypes
_BNPluginGetPluginTypes.restype = ctypes.POINTER(PluginTypeEnum)
_BNPluginGetPluginTypes.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNPluginGetPluginTypes(*args):
	result = _BNPluginGetPluginTypes(*args)
	if not result:
		return None
	return result
BNPluginGetPluginUpdateStatus = core.BNPluginGetPluginUpdateStatus
BNPluginGetPluginUpdateStatus.restype = PluginUpdateStatusEnum
BNPluginGetPluginUpdateStatus.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
_BNPluginGetUrl = core.BNPluginGetUrl
_BNPluginGetUrl.restype = ctypes.POINTER(ctypes.c_byte)
_BNPluginGetUrl.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
def BNPluginGetUrl(*args):
	result = _BNPluginGetUrl(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNPluginGetVersion = core.BNPluginGetVersion
_BNPluginGetVersion.restype = ctypes.POINTER(ctypes.c_byte)
_BNPluginGetVersion.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
def BNPluginGetVersion(*args):
	result = _BNPluginGetVersion(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNPluginInstall = core.BNPluginInstall
BNPluginInstall.restype = ctypes.c_bool
BNPluginInstall.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
BNPluginIsEnabled = core.BNPluginIsEnabled
BNPluginIsEnabled.restype = ctypes.c_bool
BNPluginIsEnabled.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
BNPluginIsInstalled = core.BNPluginIsInstalled
BNPluginIsInstalled.restype = ctypes.c_bool
BNPluginIsInstalled.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
BNPluginSetEnabled = core.BNPluginSetEnabled
BNPluginSetEnabled.restype = None
BNPluginSetEnabled.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
		ctypes.c_bool,
	]
BNPluginUninstall = core.BNPluginUninstall
BNPluginUninstall.restype = ctypes.c_bool
BNPluginUninstall.argtypes = [
		ctypes.POINTER(BNRepoPlugin),
	]
BNPrepareToCopyLowLevelILBasicBlock = core.BNPrepareToCopyLowLevelILBasicBlock
BNPrepareToCopyLowLevelILBasicBlock.restype = None
BNPrepareToCopyLowLevelILBasicBlock.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.POINTER(BNBasicBlock),
	]
BNPrepareToCopyLowLevelILFunction = core.BNPrepareToCopyLowLevelILFunction
BNPrepareToCopyLowLevelILFunction.restype = None
BNPrepareToCopyLowLevelILFunction.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.POINTER(BNLowLevelILFunction),
	]
BNPrepareToCopyMediumLevelILBasicBlock = core.BNPrepareToCopyMediumLevelILBasicBlock
BNPrepareToCopyMediumLevelILBasicBlock.restype = None
BNPrepareToCopyMediumLevelILBasicBlock.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(BNBasicBlock),
	]
BNPrepareToCopyMediumLevelILFunction = core.BNPrepareToCopyMediumLevelILFunction
BNPrepareToCopyMediumLevelILFunction.restype = None
BNPrepareToCopyMediumLevelILFunction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.POINTER(BNMediumLevelILFunction),
	]
BNPreprocessSource = core.BNPreprocessSource
BNPreprocessSource.restype = ctypes.c_bool
BNPreprocessSource.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.c_ulonglong,
	]
BNRead16 = core.BNRead16
BNRead16.restype = ctypes.c_bool
BNRead16.argtypes = [
		ctypes.POINTER(BNBinaryReader),
		ctypes.POINTER(ctypes.c_ushort),
	]
BNRead32 = core.BNRead32
BNRead32.restype = ctypes.c_bool
BNRead32.argtypes = [
		ctypes.POINTER(BNBinaryReader),
		ctypes.POINTER(ctypes.c_uint),
	]
BNRead64 = core.BNRead64
BNRead64.restype = ctypes.c_bool
BNRead64.argtypes = [
		ctypes.POINTER(BNBinaryReader),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
BNRead8 = core.BNRead8
BNRead8.restype = ctypes.c_bool
BNRead8.argtypes = [
		ctypes.POINTER(BNBinaryReader),
		ctypes.POINTER(ctypes.c_ubyte),
	]
BNReadBE16 = core.BNReadBE16
BNReadBE16.restype = ctypes.c_bool
BNReadBE16.argtypes = [
		ctypes.POINTER(BNBinaryReader),
		ctypes.POINTER(ctypes.c_ushort),
	]
BNReadBE32 = core.BNReadBE32
BNReadBE32.restype = ctypes.c_bool
BNReadBE32.argtypes = [
		ctypes.POINTER(BNBinaryReader),
		ctypes.POINTER(ctypes.c_uint),
	]
BNReadBE64 = core.BNReadBE64
BNReadBE64.restype = ctypes.c_bool
BNReadBE64.argtypes = [
		ctypes.POINTER(BNBinaryReader),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
BNReadData = core.BNReadData
BNReadData.restype = ctypes.c_bool
BNReadData.argtypes = [
		ctypes.POINTER(BNBinaryReader),
		ctypes.c_void_p,
		ctypes.c_ulonglong,
	]
BNReadLE16 = core.BNReadLE16
BNReadLE16.restype = ctypes.c_bool
BNReadLE16.argtypes = [
		ctypes.POINTER(BNBinaryReader),
		ctypes.POINTER(ctypes.c_ushort),
	]
BNReadLE32 = core.BNReadLE32
BNReadLE32.restype = ctypes.c_bool
BNReadLE32.argtypes = [
		ctypes.POINTER(BNBinaryReader),
		ctypes.POINTER(ctypes.c_uint),
	]
BNReadLE64 = core.BNReadLE64
BNReadLE64.restype = ctypes.c_bool
BNReadLE64.argtypes = [
		ctypes.POINTER(BNBinaryReader),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
_BNReadViewBuffer = core.BNReadViewBuffer
_BNReadViewBuffer.restype = ctypes.POINTER(BNDataBuffer)
_BNReadViewBuffer.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
def BNReadViewBuffer(*args):
	result = _BNReadViewBuffer(*args)
	if not result:
		return None
	return result
BNReadViewData = core.BNReadViewData
BNReadViewData.restype = ctypes.c_ulonglong
BNReadViewData.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_void_p,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNReanalyzeAllFunctions = core.BNReanalyzeAllFunctions
BNReanalyzeAllFunctions.restype = None
BNReanalyzeAllFunctions.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
BNReanalyzeFunction = core.BNReanalyzeFunction
BNReanalyzeFunction.restype = None
BNReanalyzeFunction.argtypes = [
		ctypes.POINTER(BNFunction),
	]
BNRedo = core.BNRedo
BNRedo.restype = ctypes.c_bool
BNRedo.argtypes = [
		ctypes.POINTER(BNFileMetadata),
	]
_BNRegisterArchitecture = core.BNRegisterArchitecture
_BNRegisterArchitecture.restype = ctypes.POINTER(BNArchitecture)
_BNRegisterArchitecture.argtypes = [
		ctypes.c_char_p,
		ctypes.POINTER(BNCustomArchitecture),
	]
def BNRegisterArchitecture(*args):
	result = _BNRegisterArchitecture(*args)
	if not result:
		return None
	return result
BNRegisterArchitectureForViewType = core.BNRegisterArchitectureForViewType
BNRegisterArchitectureForViewType.restype = None
BNRegisterArchitectureForViewType.argtypes = [
		ctypes.POINTER(BNBinaryViewType),
		ctypes.c_uint,
		EndiannessEnum,
		ctypes.POINTER(BNArchitecture),
	]
BNRegisterArchitectureFunctionRecognizer = core.BNRegisterArchitectureFunctionRecognizer
BNRegisterArchitectureFunctionRecognizer.restype = None
BNRegisterArchitectureFunctionRecognizer.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(BNFunctionRecognizer),
	]
_BNRegisterBinaryViewType = core.BNRegisterBinaryViewType
_BNRegisterBinaryViewType.restype = ctypes.POINTER(BNBinaryViewType)
_BNRegisterBinaryViewType.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.POINTER(BNCustomBinaryViewType),
	]
def BNRegisterBinaryViewType(*args):
	result = _BNRegisterBinaryViewType(*args)
	if not result:
		return None
	return result
BNRegisterCallingConvention = core.BNRegisterCallingConvention
BNRegisterCallingConvention.restype = None
BNRegisterCallingConvention.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(BNCallingConvention),
	]
BNRegisterDataNotification = core.BNRegisterDataNotification
BNRegisterDataNotification.restype = None
BNRegisterDataNotification.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNBinaryDataNotification),
	]
BNRegisterDefaultPlatformForViewType = core.BNRegisterDefaultPlatformForViewType
BNRegisterDefaultPlatformForViewType.restype = None
BNRegisterDefaultPlatformForViewType.argtypes = [
		ctypes.POINTER(BNBinaryViewType),
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(BNPlatform),
	]
BNRegisterForPluginLoading = core.BNRegisterForPluginLoading
BNRegisterForPluginLoading.restype = None
BNRegisterForPluginLoading.argtypes = [
		ctypes.c_char_p,
		ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p),
		ctypes.c_void_p,
	]
BNRegisterGlobalFunctionRecognizer = core.BNRegisterGlobalFunctionRecognizer
BNRegisterGlobalFunctionRecognizer.restype = None
BNRegisterGlobalFunctionRecognizer.argtypes = [
		ctypes.POINTER(BNFunctionRecognizer),
	]
BNRegisterInteractionHandler = core.BNRegisterInteractionHandler
BNRegisterInteractionHandler.restype = None
BNRegisterInteractionHandler.argtypes = [
		ctypes.POINTER(BNInteractionHandlerCallbacks),
	]
BNRegisterLogListener = core.BNRegisterLogListener
BNRegisterLogListener.restype = None
BNRegisterLogListener.argtypes = [
		ctypes.POINTER(BNLogListener),
	]
BNRegisterMainThread = core.BNRegisterMainThread
BNRegisterMainThread.restype = None
BNRegisterMainThread.argtypes = [
		ctypes.POINTER(BNMainThreadCallbacks),
	]
BNRegisterObjectDestructionCallbacks = core.BNRegisterObjectDestructionCallbacks
BNRegisterObjectDestructionCallbacks.restype = None
BNRegisterObjectDestructionCallbacks.argtypes = [
		ctypes.POINTER(BNObjectDestructionCallbacks),
	]
BNRegisterPlatform = core.BNRegisterPlatform
BNRegisterPlatform.restype = None
BNRegisterPlatform.argtypes = [
		ctypes.c_char_p,
		ctypes.POINTER(BNPlatform),
	]
BNRegisterPlatformCallingConvention = core.BNRegisterPlatformCallingConvention
BNRegisterPlatformCallingConvention.restype = None
BNRegisterPlatformCallingConvention.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(BNCallingConvention),
	]
BNRegisterPlatformCdeclCallingConvention = core.BNRegisterPlatformCdeclCallingConvention
BNRegisterPlatformCdeclCallingConvention.restype = None
BNRegisterPlatformCdeclCallingConvention.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(BNCallingConvention),
	]
BNRegisterPlatformDefaultCallingConvention = core.BNRegisterPlatformDefaultCallingConvention
BNRegisterPlatformDefaultCallingConvention.restype = None
BNRegisterPlatformDefaultCallingConvention.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(BNCallingConvention),
	]
BNRegisterPlatformFastcallCallingConvention = core.BNRegisterPlatformFastcallCallingConvention
BNRegisterPlatformFastcallCallingConvention.restype = None
BNRegisterPlatformFastcallCallingConvention.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(BNCallingConvention),
	]
BNRegisterPlatformForViewType = core.BNRegisterPlatformForViewType
BNRegisterPlatformForViewType.restype = None
BNRegisterPlatformForViewType.argtypes = [
		ctypes.POINTER(BNBinaryViewType),
		ctypes.c_uint,
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(BNPlatform),
	]
BNRegisterPlatformStdcallCallingConvention = core.BNRegisterPlatformStdcallCallingConvention
BNRegisterPlatformStdcallCallingConvention.restype = None
BNRegisterPlatformStdcallCallingConvention.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(BNCallingConvention),
	]
BNRegisterPlatformTypes = core.BNRegisterPlatformTypes
BNRegisterPlatformTypes.restype = None
BNRegisterPlatformTypes.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNPlatform),
	]
BNRegisterPluginCommand = core.BNRegisterPluginCommand
BNRegisterPluginCommand.restype = None
BNRegisterPluginCommand.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView)),
		ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(BNBinaryView)),
		ctypes.c_void_p,
	]
BNRegisterPluginCommandForAddress = core.BNRegisterPluginCommandForAddress
BNRegisterPluginCommandForAddress.restype = None
BNRegisterPluginCommandForAddress.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.c_ulonglong),
		ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.c_ulonglong),
		ctypes.c_void_p,
	]
BNRegisterPluginCommandForFunction = core.BNRegisterPluginCommandForFunction
BNRegisterPluginCommandForFunction.restype = None
BNRegisterPluginCommandForFunction.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.POINTER(BNFunction)),
		ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.POINTER(BNFunction)),
		ctypes.c_void_p,
	]
BNRegisterPluginCommandForRange = core.BNRegisterPluginCommandForRange
BNRegisterPluginCommandForRange.restype = None
BNRegisterPluginCommandForRange.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.c_ulonglong, ctypes.c_ulonglong),
		ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(BNBinaryView), ctypes.c_ulonglong, ctypes.c_ulonglong),
		ctypes.c_void_p,
	]
BNRegisterScriptingInstanceOutputListener = core.BNRegisterScriptingInstanceOutputListener
BNRegisterScriptingInstanceOutputListener.restype = None
BNRegisterScriptingInstanceOutputListener.argtypes = [
		ctypes.POINTER(BNScriptingInstance),
		ctypes.POINTER(BNScriptingOutputListener),
	]
_BNRegisterScriptingProvider = core.BNRegisterScriptingProvider
_BNRegisterScriptingProvider.restype = ctypes.POINTER(BNScriptingProvider)
_BNRegisterScriptingProvider.argtypes = [
		ctypes.c_char_p,
		ctypes.POINTER(BNScriptingProviderCallbacks),
	]
def BNRegisterScriptingProvider(*args):
	result = _BNRegisterScriptingProvider(*args)
	if not result:
		return None
	return result
_BNRegisterTransformType = core.BNRegisterTransformType
_BNRegisterTransformType.restype = ctypes.POINTER(BNTransform)
_BNRegisterTransformType.argtypes = [
		TransformTypeEnum,
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.POINTER(BNCustomTransform),
	]
def BNRegisterTransformType(*args):
	result = _BNRegisterTransformType(*args)
	if not result:
		return None
	return result
BNRegisterUndoActionType = core.BNRegisterUndoActionType
BNRegisterUndoActionType.restype = None
BNRegisterUndoActionType.argtypes = [
		ctypes.c_char_p,
		ctypes.c_void_p,
		ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(BNUndoAction)),
	]
BNReleaseAdvancedFunctionAnalysisData = core.BNReleaseAdvancedFunctionAnalysisData
BNReleaseAdvancedFunctionAnalysisData.restype = None
BNReleaseAdvancedFunctionAnalysisData.argtypes = [
		ctypes.POINTER(BNFunction),
	]
BNReleaseAdvancedFunctionAnalysisDataMultiple = core.BNReleaseAdvancedFunctionAnalysisDataMultiple
BNReleaseAdvancedFunctionAnalysisDataMultiple.restype = None
BNReleaseAdvancedFunctionAnalysisDataMultiple.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.c_ulonglong,
	]
BNRemoveAnalysisFunction = core.BNRemoveAnalysisFunction
BNRemoveAnalysisFunction.restype = None
BNRemoveAnalysisFunction.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNFunction),
	]
BNRemoveAutoSection = core.BNRemoveAutoSection
BNRemoveAutoSection.restype = None
BNRemoveAutoSection.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
	]
BNRemoveAutoSegment = core.BNRemoveAutoSegment
BNRemoveAutoSegment.restype = None
BNRemoveAutoSegment.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNRemoveEnumerationMember = core.BNRemoveEnumerationMember
BNRemoveEnumerationMember.restype = None
BNRemoveEnumerationMember.argtypes = [
		ctypes.POINTER(BNEnumeration),
		ctypes.c_ulonglong,
	]
BNRemoveStructureMember = core.BNRemoveStructureMember
BNRemoveStructureMember.restype = None
BNRemoveStructureMember.argtypes = [
		ctypes.POINTER(BNStructure),
		ctypes.c_ulonglong,
	]
BNRemoveUserFunction = core.BNRemoveUserFunction
BNRemoveUserFunction.restype = None
BNRemoveUserFunction.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNFunction),
	]
BNRemoveUserSection = core.BNRemoveUserSection
BNRemoveUserSection.restype = None
BNRemoveUserSection.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
	]
BNRemoveUserSegment = core.BNRemoveUserSegment
BNRemoveUserSegment.restype = None
BNRemoveUserSegment.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNRemoveViewData = core.BNRemoveViewData
BNRemoveViewData.restype = ctypes.c_ulonglong
BNRemoveViewData.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNRenameAnalysisType = core.BNRenameAnalysisType
BNRenameAnalysisType.restype = None
BNRenameAnalysisType.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNQualifiedName),
		ctypes.POINTER(BNQualifiedName),
	]
BNReplaceEnumerationMember = core.BNReplaceEnumerationMember
BNReplaceEnumerationMember.restype = None
BNReplaceEnumerationMember.argtypes = [
		ctypes.POINTER(BNEnumeration),
		ctypes.c_ulonglong,
		ctypes.c_char_p,
		ctypes.c_ulonglong,
	]
BNReplaceLowLevelILExpr = core.BNReplaceLowLevelILExpr
BNReplaceLowLevelILExpr.restype = None
BNReplaceLowLevelILExpr.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNReplaceMediumLevelILExpr = core.BNReplaceMediumLevelILExpr
BNReplaceMediumLevelILExpr.restype = None
BNReplaceMediumLevelILExpr.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNReplaceMediumLevelILInstruction = core.BNReplaceMediumLevelILInstruction
BNReplaceMediumLevelILInstruction.restype = None
BNReplaceMediumLevelILInstruction.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNReplaceStructureMember = core.BNReplaceStructureMember
BNReplaceStructureMember.restype = None
BNReplaceStructureMember.argtypes = [
		ctypes.POINTER(BNStructure),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNTypeWithConfidence),
		ctypes.c_char_p,
	]
BNRepositoryFreePluginDirectoryList = core.BNRepositoryFreePluginDirectoryList
BNRepositoryFreePluginDirectoryList.restype = None
BNRepositoryFreePluginDirectoryList.argtypes = [
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.c_ulonglong,
	]
_BNRepositoryGetLocalReference = core.BNRepositoryGetLocalReference
_BNRepositoryGetLocalReference.restype = ctypes.POINTER(ctypes.c_byte)
_BNRepositoryGetLocalReference.argtypes = [
		ctypes.POINTER(BNRepository),
	]
def BNRepositoryGetLocalReference(*args):
	result = _BNRepositoryGetLocalReference(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNRepositoryGetPluginByPath = core.BNRepositoryGetPluginByPath
_BNRepositoryGetPluginByPath.restype = ctypes.POINTER(BNRepoPlugin)
_BNRepositoryGetPluginByPath.argtypes = [
		ctypes.POINTER(BNRepository),
		ctypes.c_char_p,
	]
def BNRepositoryGetPluginByPath(*args):
	result = _BNRepositoryGetPluginByPath(*args)
	if not result:
		return None
	return result
_BNRepositoryGetPlugins = core.BNRepositoryGetPlugins
_BNRepositoryGetPlugins.restype = ctypes.POINTER(ctypes.POINTER(BNRepoPlugin))
_BNRepositoryGetPlugins.argtypes = [
		ctypes.POINTER(BNRepository),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNRepositoryGetPlugins(*args):
	result = _BNRepositoryGetPlugins(*args)
	if not result:
		return None
	return result
_BNRepositoryGetPluginsPath = core.BNRepositoryGetPluginsPath
_BNRepositoryGetPluginsPath.restype = ctypes.POINTER(ctypes.c_byte)
_BNRepositoryGetPluginsPath.argtypes = [
		ctypes.POINTER(BNRepository),
	]
def BNRepositoryGetPluginsPath(*args):
	result = _BNRepositoryGetPluginsPath(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNRepositoryGetRemoteReference = core.BNRepositoryGetRemoteReference
_BNRepositoryGetRemoteReference.restype = ctypes.POINTER(ctypes.c_byte)
_BNRepositoryGetRemoteReference.argtypes = [
		ctypes.POINTER(BNRepository),
	]
def BNRepositoryGetRemoteReference(*args):
	result = _BNRepositoryGetRemoteReference(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNRepositoryGetRepoPath = core.BNRepositoryGetRepoPath
_BNRepositoryGetRepoPath.restype = ctypes.POINTER(ctypes.c_byte)
_BNRepositoryGetRepoPath.argtypes = [
		ctypes.POINTER(BNRepository),
	]
def BNRepositoryGetRepoPath(*args):
	result = _BNRepositoryGetRepoPath(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNRepositoryGetRepositoryByPath = core.BNRepositoryGetRepositoryByPath
_BNRepositoryGetRepositoryByPath.restype = ctypes.POINTER(BNRepository)
_BNRepositoryGetRepositoryByPath.argtypes = [
		ctypes.POINTER(BNRepositoryManager),
		ctypes.c_char_p,
	]
def BNRepositoryGetRepositoryByPath(*args):
	result = _BNRepositoryGetRepositoryByPath(*args)
	if not result:
		return None
	return result
_BNRepositoryGetUrl = core.BNRepositoryGetUrl
_BNRepositoryGetUrl.restype = ctypes.POINTER(ctypes.c_byte)
_BNRepositoryGetUrl.argtypes = [
		ctypes.POINTER(BNRepository),
	]
def BNRepositoryGetUrl(*args):
	result = _BNRepositoryGetUrl(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
BNRepositoryIsInitialized = core.BNRepositoryIsInitialized
BNRepositoryIsInitialized.restype = ctypes.c_bool
BNRepositoryIsInitialized.argtypes = [
		ctypes.POINTER(BNRepository),
	]
BNRepositoryManagerAddRepository = core.BNRepositoryManagerAddRepository
BNRepositoryManagerAddRepository.restype = ctypes.c_bool
BNRepositoryManagerAddRepository.argtypes = [
		ctypes.POINTER(BNRepositoryManager),
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNRepositoryManagerCheckForUpdates = core.BNRepositoryManagerCheckForUpdates
BNRepositoryManagerCheckForUpdates.restype = ctypes.c_bool
BNRepositoryManagerCheckForUpdates.argtypes = [
		ctypes.POINTER(BNRepositoryManager),
	]
BNRepositoryManagerDisablePlugin = core.BNRepositoryManagerDisablePlugin
BNRepositoryManagerDisablePlugin.restype = ctypes.c_bool
BNRepositoryManagerDisablePlugin.argtypes = [
		ctypes.POINTER(BNRepositoryManager),
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNRepositoryManagerEnablePlugin = core.BNRepositoryManagerEnablePlugin
BNRepositoryManagerEnablePlugin.restype = ctypes.c_bool
BNRepositoryManagerEnablePlugin.argtypes = [
		ctypes.POINTER(BNRepositoryManager),
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
_BNRepositoryManagerGetDefaultRepository = core.BNRepositoryManagerGetDefaultRepository
_BNRepositoryManagerGetDefaultRepository.restype = ctypes.POINTER(BNRepository)
_BNRepositoryManagerGetDefaultRepository.argtypes = [
		ctypes.POINTER(BNRepositoryManager),
	]
def BNRepositoryManagerGetDefaultRepository(*args):
	result = _BNRepositoryManagerGetDefaultRepository(*args)
	if not result:
		return None
	return result
_BNRepositoryManagerGetRepositories = core.BNRepositoryManagerGetRepositories
_BNRepositoryManagerGetRepositories.restype = ctypes.POINTER(ctypes.POINTER(BNRepository))
_BNRepositoryManagerGetRepositories.argtypes = [
		ctypes.POINTER(BNRepositoryManager),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNRepositoryManagerGetRepositories(*args):
	result = _BNRepositoryManagerGetRepositories(*args)
	if not result:
		return None
	return result
BNRepositoryManagerInstallPlugin = core.BNRepositoryManagerInstallPlugin
BNRepositoryManagerInstallPlugin.restype = ctypes.c_bool
BNRepositoryManagerInstallPlugin.argtypes = [
		ctypes.POINTER(BNRepositoryManager),
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNRepositoryManagerUninstallPlugin = core.BNRepositoryManagerUninstallPlugin
BNRepositoryManagerUninstallPlugin.restype = ctypes.c_bool
BNRepositoryManagerUninstallPlugin.argtypes = [
		ctypes.POINTER(BNRepositoryManager),
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNRepositoryManagerUpdatePlugin = core.BNRepositoryManagerUpdatePlugin
BNRepositoryManagerUpdatePlugin.restype = ctypes.c_bool
BNRepositoryManagerUpdatePlugin.argtypes = [
		ctypes.POINTER(BNRepositoryManager),
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNRequestAdvancedFunctionAnalysisData = core.BNRequestAdvancedFunctionAnalysisData
BNRequestAdvancedFunctionAnalysisData.restype = None
BNRequestAdvancedFunctionAnalysisData.argtypes = [
		ctypes.POINTER(BNFunction),
	]
BNSaveAutoSnapshot = core.BNSaveAutoSnapshot
BNSaveAutoSnapshot.restype = ctypes.c_bool
BNSaveAutoSnapshot.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
BNSaveAutoSnapshotWithProgress = core.BNSaveAutoSnapshotWithProgress
BNSaveAutoSnapshotWithProgress.restype = ctypes.c_bool
BNSaveAutoSnapshotWithProgress.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_void_p,
		ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_ulonglong),
	]
BNSaveLastRun = core.BNSaveLastRun
BNSaveLastRun.restype = None
BNSaveLastRun.argtypes = [
	]
BNSaveToFile = core.BNSaveToFile
BNSaveToFile.restype = ctypes.c_bool
BNSaveToFile.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNFileAccessor),
	]
BNSaveToFilename = core.BNSaveToFilename
BNSaveToFilename.restype = ctypes.c_bool
BNSaveToFilename.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
	]
BNSeekBinaryReader = core.BNSeekBinaryReader
BNSeekBinaryReader.restype = None
BNSeekBinaryReader.argtypes = [
		ctypes.POINTER(BNBinaryReader),
		ctypes.c_ulonglong,
	]
BNSeekBinaryReaderRelative = core.BNSeekBinaryReaderRelative
BNSeekBinaryReaderRelative.restype = None
BNSeekBinaryReaderRelative.argtypes = [
		ctypes.POINTER(BNBinaryReader),
		ctypes.c_longlong,
	]
BNSeekBinaryWriter = core.BNSeekBinaryWriter
BNSeekBinaryWriter.restype = None
BNSeekBinaryWriter.argtypes = [
		ctypes.POINTER(BNBinaryWriter),
		ctypes.c_ulonglong,
	]
BNSeekBinaryWriterRelative = core.BNSeekBinaryWriterRelative
BNSeekBinaryWriterRelative.restype = None
BNSeekBinaryWriterRelative.argtypes = [
		ctypes.POINTER(BNBinaryWriter),
		ctypes.c_longlong,
	]
BNSetActiveUpdateChannel = core.BNSetActiveUpdateChannel
BNSetActiveUpdateChannel.restype = None
BNSetActiveUpdateChannel.argtypes = [
		ctypes.c_char_p,
	]
BNSetArchitectureCdeclCallingConvention = core.BNSetArchitectureCdeclCallingConvention
BNSetArchitectureCdeclCallingConvention.restype = None
BNSetArchitectureCdeclCallingConvention.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(BNCallingConvention),
	]
BNSetArchitectureDefaultCallingConvention = core.BNSetArchitectureDefaultCallingConvention
BNSetArchitectureDefaultCallingConvention.restype = None
BNSetArchitectureDefaultCallingConvention.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(BNCallingConvention),
	]
BNSetArchitectureFastcallCallingConvention = core.BNSetArchitectureFastcallCallingConvention
BNSetArchitectureFastcallCallingConvention.restype = None
BNSetArchitectureFastcallCallingConvention.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(BNCallingConvention),
	]
BNSetArchitectureStdcallCallingConvention = core.BNSetArchitectureStdcallCallingConvention
BNSetArchitectureStdcallCallingConvention.restype = None
BNSetArchitectureStdcallCallingConvention.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.POINTER(BNCallingConvention),
	]
BNSetAutoBasicBlockHighlight = core.BNSetAutoBasicBlockHighlight
BNSetAutoBasicBlockHighlight.restype = None
BNSetAutoBasicBlockHighlight.argtypes = [
		ctypes.POINTER(BNBasicBlock),
		BNHighlightColor,
	]
BNSetAutoFunctionCallingConvention = core.BNSetAutoFunctionCallingConvention
BNSetAutoFunctionCallingConvention.restype = None
BNSetAutoFunctionCallingConvention.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNCallingConventionWithConfidence),
	]
BNSetAutoFunctionCanReturn = core.BNSetAutoFunctionCanReturn
BNSetAutoFunctionCanReturn.restype = None
BNSetAutoFunctionCanReturn.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNBoolWithConfidence),
	]
BNSetAutoFunctionClobberedRegisters = core.BNSetAutoFunctionClobberedRegisters
BNSetAutoFunctionClobberedRegisters.restype = None
BNSetAutoFunctionClobberedRegisters.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNRegisterSetWithConfidence),
	]
BNSetAutoFunctionHasVariableArguments = core.BNSetAutoFunctionHasVariableArguments
BNSetAutoFunctionHasVariableArguments.restype = None
BNSetAutoFunctionHasVariableArguments.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNBoolWithConfidence),
	]
BNSetAutoFunctionParameterVariables = core.BNSetAutoFunctionParameterVariables
BNSetAutoFunctionParameterVariables.restype = None
BNSetAutoFunctionParameterVariables.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNParameterVariablesWithConfidence),
	]
BNSetAutoFunctionReturnType = core.BNSetAutoFunctionReturnType
BNSetAutoFunctionReturnType.restype = None
BNSetAutoFunctionReturnType.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNTypeWithConfidence),
	]
BNSetAutoFunctionStackAdjustment = core.BNSetAutoFunctionStackAdjustment
BNSetAutoFunctionStackAdjustment.restype = None
BNSetAutoFunctionStackAdjustment.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNSizeWithConfidence),
	]
BNSetAutoIndirectBranches = core.BNSetAutoIndirectBranches
BNSetAutoIndirectBranches.restype = None
BNSetAutoIndirectBranches.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNArchitectureAndAddress),
		ctypes.c_ulonglong,
	]
BNSetAutoInstructionHighlight = core.BNSetAutoInstructionHighlight
BNSetAutoInstructionHighlight.restype = None
BNSetAutoInstructionHighlight.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		BNHighlightColor,
	]
BNSetAutoUpdatesEnabled = core.BNSetAutoUpdatesEnabled
BNSetAutoUpdatesEnabled.restype = None
BNSetAutoUpdatesEnabled.argtypes = [
		ctypes.c_bool,
	]
BNSetBackgroundTaskProgressText = core.BNSetBackgroundTaskProgressText
BNSetBackgroundTaskProgressText.restype = None
BNSetBackgroundTaskProgressText.argtypes = [
		ctypes.POINTER(BNBackgroundTask),
		ctypes.c_char_p,
	]
BNSetBinaryReaderEndianness = core.BNSetBinaryReaderEndianness
BNSetBinaryReaderEndianness.restype = None
BNSetBinaryReaderEndianness.argtypes = [
		ctypes.POINTER(BNBinaryReader),
		EndiannessEnum,
	]
BNSetBinaryViewTypeArchitectureConstant = core.BNSetBinaryViewTypeArchitectureConstant
BNSetBinaryViewTypeArchitectureConstant.restype = None
BNSetBinaryViewTypeArchitectureConstant.argtypes = [
		ctypes.POINTER(BNArchitecture),
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_ulonglong,
	]
BNSetBinaryWriterEndianness = core.BNSetBinaryWriterEndianness
BNSetBinaryWriterEndianness.restype = None
BNSetBinaryWriterEndianness.argtypes = [
		ctypes.POINTER(BNBinaryWriter),
		EndiannessEnum,
	]
BNSetBundledPluginDirectory = core.BNSetBundledPluginDirectory
BNSetBundledPluginDirectory.restype = None
BNSetBundledPluginDirectory.argtypes = [
		ctypes.c_char_p,
	]
BNSetCommentForAddress = core.BNSetCommentForAddress
BNSetCommentForAddress.restype = None
BNSetCommentForAddress.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.c_ulonglong,
		ctypes.c_char_p,
	]
BNSetCurrentPluginLoadOrder = core.BNSetCurrentPluginLoadOrder
BNSetCurrentPluginLoadOrder.restype = None
BNSetCurrentPluginLoadOrder.argtypes = [
		PluginLoadOrderEnum,
	]
BNSetDataBufferByte = core.BNSetDataBufferByte
BNSetDataBufferByte.restype = None
BNSetDataBufferByte.argtypes = [
		ctypes.POINTER(BNDataBuffer),
		ctypes.c_ulonglong,
		ctypes.c_ubyte,
	]
BNSetDataBufferContents = core.BNSetDataBufferContents
BNSetDataBufferContents.restype = None
BNSetDataBufferContents.argtypes = [
		ctypes.POINTER(BNDataBuffer),
		ctypes.c_void_p,
		ctypes.c_ulonglong,
	]
BNSetDataBufferLength = core.BNSetDataBufferLength
BNSetDataBufferLength.restype = None
BNSetDataBufferLength.argtypes = [
		ctypes.POINTER(BNDataBuffer),
		ctypes.c_ulonglong,
	]
BNSetDefaultArchitecture = core.BNSetDefaultArchitecture
BNSetDefaultArchitecture.restype = None
BNSetDefaultArchitecture.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNArchitecture),
	]
BNSetDefaultPlatform = core.BNSetDefaultPlatform
BNSetDefaultPlatform.restype = None
BNSetDefaultPlatform.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNPlatform),
	]
BNSetDisassemblyMaximumSymbolWidth = core.BNSetDisassemblyMaximumSymbolWidth
BNSetDisassemblyMaximumSymbolWidth.restype = None
BNSetDisassemblyMaximumSymbolWidth.argtypes = [
		ctypes.POINTER(BNDisassemblySettings),
		ctypes.c_ulonglong,
	]
BNSetDisassemblySettingsOption = core.BNSetDisassemblySettingsOption
BNSetDisassemblySettingsOption.restype = None
BNSetDisassemblySettingsOption.argtypes = [
		ctypes.POINTER(BNDisassemblySettings),
		DisassemblyOptionEnum,
		ctypes.c_bool,
	]
BNSetDisassemblyWidth = core.BNSetDisassemblyWidth
BNSetDisassemblyWidth.restype = None
BNSetDisassemblyWidth.argtypes = [
		ctypes.POINTER(BNDisassemblySettings),
		ctypes.c_ulonglong,
	]
BNSetFileMetadataNavigationHandler = core.BNSetFileMetadataNavigationHandler
BNSetFileMetadataNavigationHandler.restype = None
BNSetFileMetadataNavigationHandler.argtypes = [
		ctypes.POINTER(BNFileMetadata),
		ctypes.POINTER(BNNavigationHandler),
	]
BNSetFilename = core.BNSetFilename
BNSetFilename.restype = None
BNSetFilename.argtypes = [
		ctypes.POINTER(BNFileMetadata),
		ctypes.c_char_p,
	]
BNSetFunctionAutoType = core.BNSetFunctionAutoType
BNSetFunctionAutoType.restype = None
BNSetFunctionAutoType.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNType),
	]
BNSetFunctionComment = core.BNSetFunctionComment
BNSetFunctionComment.restype = None
BNSetFunctionComment.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.c_char_p,
	]
BNSetFunctionGraphBlockMargins = core.BNSetFunctionGraphBlockMargins
BNSetFunctionGraphBlockMargins.restype = None
BNSetFunctionGraphBlockMargins.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
		ctypes.c_int,
		ctypes.c_int,
	]
BNSetFunctionGraphCompleteCallback = core.BNSetFunctionGraphCompleteCallback
BNSetFunctionGraphCompleteCallback.restype = None
BNSetFunctionGraphCompleteCallback.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
		ctypes.c_void_p,
		ctypes.CFUNCTYPE(None, ctypes.c_void_p),
	]
BNSetFunctionGraphOption = core.BNSetFunctionGraphOption
BNSetFunctionGraphOption.restype = None
BNSetFunctionGraphOption.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
		DisassemblyOptionEnum,
		ctypes.c_bool,
	]
BNSetFunctionTypeCanReturn = core.BNSetFunctionTypeCanReturn
BNSetFunctionTypeCanReturn.restype = None
BNSetFunctionTypeCanReturn.argtypes = [
		ctypes.POINTER(BNType),
		ctypes.POINTER(BNBoolWithConfidence),
	]
BNSetFunctionUserType = core.BNSetFunctionUserType
BNSetFunctionUserType.restype = None
BNSetFunctionUserType.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNType),
	]
BNSetIntegerConstantDisplayType = core.BNSetIntegerConstantDisplayType
BNSetIntegerConstantDisplayType.restype = None
BNSetIntegerConstantDisplayType.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		IntegerDisplayTypeEnum,
	]
BNSetPlatformSystemCallConvention = core.BNSetPlatformSystemCallConvention
BNSetPlatformSystemCallConvention.restype = None
BNSetPlatformSystemCallConvention.argtypes = [
		ctypes.POINTER(BNPlatform),
		ctypes.POINTER(BNCallingConvention),
	]
BNSetScriptingInstanceCurrentAddress = core.BNSetScriptingInstanceCurrentAddress
BNSetScriptingInstanceCurrentAddress.restype = None
BNSetScriptingInstanceCurrentAddress.argtypes = [
		ctypes.POINTER(BNScriptingInstance),
		ctypes.c_ulonglong,
	]
BNSetScriptingInstanceCurrentBasicBlock = core.BNSetScriptingInstanceCurrentBasicBlock
BNSetScriptingInstanceCurrentBasicBlock.restype = None
BNSetScriptingInstanceCurrentBasicBlock.argtypes = [
		ctypes.POINTER(BNScriptingInstance),
		ctypes.POINTER(BNBasicBlock),
	]
BNSetScriptingInstanceCurrentBinaryView = core.BNSetScriptingInstanceCurrentBinaryView
BNSetScriptingInstanceCurrentBinaryView.restype = None
BNSetScriptingInstanceCurrentBinaryView.argtypes = [
		ctypes.POINTER(BNScriptingInstance),
		ctypes.POINTER(BNBinaryView),
	]
BNSetScriptingInstanceCurrentFunction = core.BNSetScriptingInstanceCurrentFunction
BNSetScriptingInstanceCurrentFunction.restype = None
BNSetScriptingInstanceCurrentFunction.argtypes = [
		ctypes.POINTER(BNScriptingInstance),
		ctypes.POINTER(BNFunction),
	]
BNSetScriptingInstanceCurrentSelection = core.BNSetScriptingInstanceCurrentSelection
BNSetScriptingInstanceCurrentSelection.restype = None
BNSetScriptingInstanceCurrentSelection.argtypes = [
		ctypes.POINTER(BNScriptingInstance),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNSetStructureAlignment = core.BNSetStructureAlignment
BNSetStructureAlignment.restype = None
BNSetStructureAlignment.argtypes = [
		ctypes.POINTER(BNStructure),
		ctypes.c_ulonglong,
	]
BNSetStructurePacked = core.BNSetStructurePacked
BNSetStructurePacked.restype = None
BNSetStructurePacked.argtypes = [
		ctypes.POINTER(BNStructure),
		ctypes.c_bool,
	]
BNSetStructureType = core.BNSetStructureType
BNSetStructureType.restype = None
BNSetStructureType.argtypes = [
		ctypes.POINTER(BNStructure),
		StructureTypeEnum,
	]
BNSetStructureWidth = core.BNSetStructureWidth
BNSetStructureWidth.restype = None
BNSetStructureWidth.argtypes = [
		ctypes.POINTER(BNStructure),
		ctypes.c_ulonglong,
	]
BNSetSymbolAutoDefined = core.BNSetSymbolAutoDefined
BNSetSymbolAutoDefined.restype = None
BNSetSymbolAutoDefined.argtypes = [
		ctypes.POINTER(BNSymbol),
		ctypes.c_bool,
	]
BNSetTypeReferenceClass = core.BNSetTypeReferenceClass
BNSetTypeReferenceClass.restype = None
BNSetTypeReferenceClass.argtypes = [
		ctypes.POINTER(BNNamedTypeReference),
		NamedTypeReferenceClassEnum,
	]
BNSetTypeReferenceId = core.BNSetTypeReferenceId
BNSetTypeReferenceId.restype = None
BNSetTypeReferenceId.argtypes = [
		ctypes.POINTER(BNNamedTypeReference),
		ctypes.c_char_p,
	]
BNSetTypeReferenceName = core.BNSetTypeReferenceName
BNSetTypeReferenceName.restype = None
BNSetTypeReferenceName.argtypes = [
		ctypes.POINTER(BNNamedTypeReference),
		ctypes.POINTER(BNQualifiedName),
	]
BNSetUserBasicBlockHighlight = core.BNSetUserBasicBlockHighlight
BNSetUserBasicBlockHighlight.restype = None
BNSetUserBasicBlockHighlight.argtypes = [
		ctypes.POINTER(BNBasicBlock),
		BNHighlightColor,
	]
BNSetUserFunctionCallingConvention = core.BNSetUserFunctionCallingConvention
BNSetUserFunctionCallingConvention.restype = None
BNSetUserFunctionCallingConvention.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNCallingConventionWithConfidence),
	]
BNSetUserFunctionCanReturn = core.BNSetUserFunctionCanReturn
BNSetUserFunctionCanReturn.restype = None
BNSetUserFunctionCanReturn.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNBoolWithConfidence),
	]
BNSetUserFunctionClobberedRegisters = core.BNSetUserFunctionClobberedRegisters
BNSetUserFunctionClobberedRegisters.restype = None
BNSetUserFunctionClobberedRegisters.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNRegisterSetWithConfidence),
	]
BNSetUserFunctionHasVariableArguments = core.BNSetUserFunctionHasVariableArguments
BNSetUserFunctionHasVariableArguments.restype = None
BNSetUserFunctionHasVariableArguments.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNBoolWithConfidence),
	]
BNSetUserFunctionParameterVariables = core.BNSetUserFunctionParameterVariables
BNSetUserFunctionParameterVariables.restype = None
BNSetUserFunctionParameterVariables.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNParameterVariablesWithConfidence),
	]
BNSetUserFunctionReturnType = core.BNSetUserFunctionReturnType
BNSetUserFunctionReturnType.restype = None
BNSetUserFunctionReturnType.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNTypeWithConfidence),
	]
BNSetUserFunctionStackAdjustment = core.BNSetUserFunctionStackAdjustment
BNSetUserFunctionStackAdjustment.restype = None
BNSetUserFunctionStackAdjustment.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNSizeWithConfidence),
	]
BNSetUserIndirectBranches = core.BNSetUserIndirectBranches
BNSetUserIndirectBranches.restype = None
BNSetUserIndirectBranches.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNArchitectureAndAddress),
		ctypes.c_ulonglong,
	]
BNSetUserInstructionHighlight = core.BNSetUserInstructionHighlight
BNSetUserInstructionHighlight.restype = None
BNSetUserInstructionHighlight.argtypes = [
		ctypes.POINTER(BNFunction),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		BNHighlightColor,
	]
BNSetWorkerThreadCount = core.BNSetWorkerThreadCount
BNSetWorkerThreadCount.restype = None
BNSetWorkerThreadCount.argtypes = [
		ctypes.c_ulonglong,
	]
BNSettingFlushSettings = core.BNSettingFlushSettings
BNSettingFlushSettings.restype = ctypes.c_bool
BNSettingFlushSettings.argtypes = [
	]
BNSettingGetBool = core.BNSettingGetBool
BNSettingGetBool.restype = ctypes.c_bool
BNSettingGetBool.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_bool,
	]
BNSettingGetDouble = core.BNSettingGetDouble
BNSettingGetDouble.restype = ctypes.c_double
BNSettingGetDouble.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_double,
	]
BNSettingGetInteger = core.BNSettingGetInteger
BNSettingGetInteger.restype = ctypes.c_longlong
BNSettingGetInteger.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_longlong,
	]
_BNSettingGetIntegerList = core.BNSettingGetIntegerList
_BNSettingGetIntegerList.restype = ctypes.POINTER(ctypes.c_longlong)
_BNSettingGetIntegerList.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.POINTER(ctypes.c_longlong),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNSettingGetIntegerList(*args):
	result = _BNSettingGetIntegerList(*args)
	if not result:
		return None
	return result
_BNSettingGetString = core.BNSettingGetString
_BNSettingGetString.restype = ctypes.POINTER(ctypes.c_byte)
_BNSettingGetString.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
def BNSettingGetString(*args):
	result = _BNSettingGetString(*args)
	string = ctypes.cast(result, ctypes.c_char_p).value
	BNFreeString(result)
	return string
_BNSettingGetStringList = core.BNSettingGetStringList
_BNSettingGetStringList.restype = ctypes.POINTER(ctypes.c_char_p)
_BNSettingGetStringList.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.POINTER(ctypes.c_ulonglong),
	]
def BNSettingGetStringList(*args):
	result = _BNSettingGetStringList(*args)
	if not result:
		return None
	return result
BNSettingIsBool = core.BNSettingIsBool
BNSettingIsBool.restype = ctypes.c_bool
BNSettingIsBool.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNSettingIsDouble = core.BNSettingIsDouble
BNSettingIsDouble.restype = ctypes.c_bool
BNSettingIsDouble.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNSettingIsInteger = core.BNSettingIsInteger
BNSettingIsInteger.restype = ctypes.c_bool
BNSettingIsInteger.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNSettingIsIntegerList = core.BNSettingIsIntegerList
BNSettingIsIntegerList.restype = ctypes.c_bool
BNSettingIsIntegerList.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNSettingIsPresent = core.BNSettingIsPresent
BNSettingIsPresent.restype = ctypes.c_bool
BNSettingIsPresent.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNSettingIsString = core.BNSettingIsString
BNSettingIsString.restype = ctypes.c_bool
BNSettingIsString.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNSettingIsStringList = core.BNSettingIsStringList
BNSettingIsStringList.restype = ctypes.c_bool
BNSettingIsStringList.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNSettingRemoveSetting = core.BNSettingRemoveSetting
BNSettingRemoveSetting.restype = ctypes.c_bool
BNSettingRemoveSetting.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_bool,
	]
BNSettingRemoveSettingGroup = core.BNSettingRemoveSettingGroup
BNSettingRemoveSettingGroup.restype = ctypes.c_bool
BNSettingRemoveSettingGroup.argtypes = [
		ctypes.c_char_p,
		ctypes.c_bool,
	]
BNSettingSetBool = core.BNSettingSetBool
BNSettingSetBool.restype = ctypes.c_bool
BNSettingSetBool.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_bool,
		ctypes.c_bool,
	]
BNSettingSetDouble = core.BNSettingSetDouble
BNSettingSetDouble.restype = ctypes.c_bool
BNSettingSetDouble.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_double,
		ctypes.c_bool,
	]
BNSettingSetInteger = core.BNSettingSetInteger
BNSettingSetInteger.restype = ctypes.c_bool
BNSettingSetInteger.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_longlong,
		ctypes.c_bool,
	]
BNSettingSetIntegerList = core.BNSettingSetIntegerList
BNSettingSetIntegerList.restype = ctypes.c_bool
BNSettingSetIntegerList.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.POINTER(ctypes.c_longlong),
		ctypes.c_ulonglong,
		ctypes.c_bool,
	]
BNSettingSetString = core.BNSettingSetString
BNSettingSetString.restype = ctypes.c_bool
BNSettingSetString.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_bool,
	]
BNSettingSetStringList = core.BNSettingSetStringList
BNSettingSetStringList.restype = ctypes.c_bool
BNSettingSetStringList.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.c_ulonglong,
		ctypes.c_bool,
	]
BNShowHTMLReport = core.BNShowHTMLReport
BNShowHTMLReport.restype = None
BNShowHTMLReport.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNShowMarkdownReport = core.BNShowMarkdownReport
BNShowMarkdownReport.restype = None
BNShowMarkdownReport.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNShowMessageBox = core.BNShowMessageBox
BNShowMessageBox.restype = MessageBoxButtonResultEnum
BNShowMessageBox.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		MessageBoxButtonSetEnum,
		MessageBoxIconEnum,
	]
BNShowPlainTextReport = core.BNShowPlainTextReport
BNShowPlainTextReport.restype = None
BNShowPlainTextReport.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
		ctypes.c_char_p,
	]
BNShutdown = core.BNShutdown
BNShutdown.restype = None
BNShutdown.argtypes = [
	]
BNSkipAndReturnValue = core.BNSkipAndReturnValue
BNSkipAndReturnValue.restype = ctypes.c_bool
BNSkipAndReturnValue.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNArchitecture),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNStartFunctionGraphLayout = core.BNStartFunctionGraphLayout
BNStartFunctionGraphLayout.restype = None
BNStartFunctionGraphLayout.argtypes = [
		ctypes.POINTER(BNFunctionGraph),
		FunctionGraphTypeEnum,
	]
BNToVariableIdentifier = core.BNToVariableIdentifier
BNToVariableIdentifier.restype = ctypes.c_ulonglong
BNToVariableIdentifier.argtypes = [
		ctypes.POINTER(BNVariable),
	]
BNTypeGetMemberAccess = core.BNTypeGetMemberAccess
BNTypeGetMemberAccess.restype = BNMemberAccessWithConfidence
BNTypeGetMemberAccess.argtypes = [
		ctypes.POINTER(BNType),
	]
BNTypeGetMemberScope = core.BNTypeGetMemberScope
BNTypeGetMemberScope.restype = BNMemberScopeWithConfidence
BNTypeGetMemberScope.argtypes = [
		ctypes.POINTER(BNType),
	]
BNTypeGetTypeName = core.BNTypeGetTypeName
BNTypeGetTypeName.restype = BNQualifiedName
BNTypeGetTypeName.argtypes = [
		ctypes.POINTER(BNType),
	]
BNTypeHasVariableArguments = core.BNTypeHasVariableArguments
BNTypeHasVariableArguments.restype = BNBoolWithConfidence
BNTypeHasVariableArguments.argtypes = [
		ctypes.POINTER(BNType),
	]
BNTypeSetConst = core.BNTypeSetConst
BNTypeSetConst.restype = None
BNTypeSetConst.argtypes = [
		ctypes.POINTER(BNType),
		ctypes.POINTER(BNBoolWithConfidence),
	]
BNTypeSetMemberAccess = core.BNTypeSetMemberAccess
BNTypeSetMemberAccess.restype = None
BNTypeSetMemberAccess.argtypes = [
		ctypes.POINTER(BNType),
		ctypes.POINTER(BNMemberAccessWithConfidence),
	]
BNTypeSetMemberScope = core.BNTypeSetMemberScope
BNTypeSetMemberScope.restype = None
BNTypeSetMemberScope.argtypes = [
		ctypes.POINTER(BNType),
		ctypes.POINTER(BNMemberScopeWithConfidence),
	]
BNTypeSetTypeName = core.BNTypeSetTypeName
BNTypeSetTypeName.restype = None
BNTypeSetTypeName.argtypes = [
		ctypes.POINTER(BNType),
		ctypes.POINTER(BNQualifiedName),
	]
BNTypeSetVolatile = core.BNTypeSetVolatile
BNTypeSetVolatile.restype = None
BNTypeSetVolatile.argtypes = [
		ctypes.POINTER(BNType),
		ctypes.POINTER(BNBoolWithConfidence),
	]
BNUndefineAnalysisType = core.BNUndefineAnalysisType
BNUndefineAnalysisType.restype = None
BNUndefineAnalysisType.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_char_p,
	]
BNUndefineAutoSymbol = core.BNUndefineAutoSymbol
BNUndefineAutoSymbol.restype = None
BNUndefineAutoSymbol.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNSymbol),
	]
BNUndefineDataVariable = core.BNUndefineDataVariable
BNUndefineDataVariable.restype = None
BNUndefineDataVariable.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNUndefineUserAnalysisType = core.BNUndefineUserAnalysisType
BNUndefineUserAnalysisType.restype = None
BNUndefineUserAnalysisType.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNQualifiedName),
	]
BNUndefineUserDataVariable = core.BNUndefineUserDataVariable
BNUndefineUserDataVariable.restype = None
BNUndefineUserDataVariable.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
	]
BNUndefineUserSymbol = core.BNUndefineUserSymbol
BNUndefineUserSymbol.restype = None
BNUndefineUserSymbol.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNSymbol),
	]
BNUndo = core.BNUndo
BNUndo.restype = ctypes.c_bool
BNUndo.argtypes = [
		ctypes.POINTER(BNFileMetadata),
	]
BNUnregisterDataNotification = core.BNUnregisterDataNotification
BNUnregisterDataNotification.restype = None
BNUnregisterDataNotification.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.POINTER(BNBinaryDataNotification),
	]
BNUnregisterLogListener = core.BNUnregisterLogListener
BNUnregisterLogListener.restype = None
BNUnregisterLogListener.argtypes = [
		ctypes.POINTER(BNLogListener),
	]
BNUnregisterObjectDestructionCallbacks = core.BNUnregisterObjectDestructionCallbacks
BNUnregisterObjectDestructionCallbacks.restype = None
BNUnregisterObjectDestructionCallbacks.argtypes = [
		ctypes.POINTER(BNObjectDestructionCallbacks),
	]
BNUnregisterScriptingInstanceOutputListener = core.BNUnregisterScriptingInstanceOutputListener
BNUnregisterScriptingInstanceOutputListener.restype = None
BNUnregisterScriptingInstanceOutputListener.argtypes = [
		ctypes.POINTER(BNScriptingInstance),
		ctypes.POINTER(BNScriptingOutputListener),
	]
BNUpdateAnalysis = core.BNUpdateAnalysis
BNUpdateAnalysis.restype = None
BNUpdateAnalysis.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
BNUpdateAnalysisAndWait = core.BNUpdateAnalysisAndWait
BNUpdateAnalysisAndWait.restype = None
BNUpdateAnalysisAndWait.argtypes = [
		ctypes.POINTER(BNBinaryView),
	]
BNUpdateLogListeners = core.BNUpdateLogListeners
BNUpdateLogListeners.restype = None
BNUpdateLogListeners.argtypes = [
	]
BNUpdateLowLevelILOperand = core.BNUpdateLowLevelILOperand
BNUpdateLowLevelILOperand.restype = None
BNUpdateLowLevelILOperand.argtypes = [
		ctypes.POINTER(BNLowLevelILFunction),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNUpdateMediumLevelILOperand = core.BNUpdateMediumLevelILOperand
BNUpdateMediumLevelILOperand.restype = None
BNUpdateMediumLevelILOperand.argtypes = [
		ctypes.POINTER(BNMediumLevelILFunction),
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
		ctypes.c_ulonglong,
	]
BNUpdateToLatestVersion = core.BNUpdateToLatestVersion
BNUpdateToLatestVersion.restype = UpdateResultEnum
BNUpdateToLatestVersion.argtypes = [
		ctypes.c_char_p,
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_ulonglong),
		ctypes.c_void_p,
	]
BNUpdateToVersion = core.BNUpdateToVersion
BNUpdateToVersion.restype = UpdateResultEnum
BNUpdateToVersion.argtypes = [
		ctypes.c_char_p,
		ctypes.c_char_p,
		ctypes.POINTER(ctypes.c_char_p),
		ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_ulonglong),
		ctypes.c_void_p,
	]
BNUpdatesChecked = core.BNUpdatesChecked
BNUpdatesChecked.restype = None
BNUpdatesChecked.argtypes = [
	]
BNWaitForMainThreadAction = core.BNWaitForMainThreadAction
BNWaitForMainThreadAction.restype = None
BNWaitForMainThreadAction.argtypes = [
		ctypes.POINTER(BNMainThreadAction),
	]
BNWasFunctionAutomaticallyDiscovered = core.BNWasFunctionAutomaticallyDiscovered
BNWasFunctionAutomaticallyDiscovered.restype = ctypes.c_bool
BNWasFunctionAutomaticallyDiscovered.argtypes = [
		ctypes.POINTER(BNFunction),
	]
BNWorkerEnqueue = core.BNWorkerEnqueue
BNWorkerEnqueue.restype = None
BNWorkerEnqueue.argtypes = [
		ctypes.c_void_p,
		ctypes.CFUNCTYPE(None, ctypes.c_void_p),
	]
BNWorkerInteractiveEnqueue = core.BNWorkerInteractiveEnqueue
BNWorkerInteractiveEnqueue.restype = None
BNWorkerInteractiveEnqueue.argtypes = [
		ctypes.c_void_p,
		ctypes.CFUNCTYPE(None, ctypes.c_void_p),
	]
BNWorkerPriorityEnqueue = core.BNWorkerPriorityEnqueue
BNWorkerPriorityEnqueue.restype = None
BNWorkerPriorityEnqueue.argtypes = [
		ctypes.c_void_p,
		ctypes.CFUNCTYPE(None, ctypes.c_void_p),
	]
BNWrite16 = core.BNWrite16
BNWrite16.restype = ctypes.c_bool
BNWrite16.argtypes = [
		ctypes.POINTER(BNBinaryWriter),
		ctypes.c_ushort,
	]
BNWrite32 = core.BNWrite32
BNWrite32.restype = ctypes.c_bool
BNWrite32.argtypes = [
		ctypes.POINTER(BNBinaryWriter),
		ctypes.c_uint,
	]
BNWrite64 = core.BNWrite64
BNWrite64.restype = ctypes.c_bool
BNWrite64.argtypes = [
		ctypes.POINTER(BNBinaryWriter),
		ctypes.c_ulonglong,
	]
BNWrite8 = core.BNWrite8
BNWrite8.restype = ctypes.c_bool
BNWrite8.argtypes = [
		ctypes.POINTER(BNBinaryWriter),
		ctypes.c_ubyte,
	]
BNWriteBE16 = core.BNWriteBE16
BNWriteBE16.restype = ctypes.c_bool
BNWriteBE16.argtypes = [
		ctypes.POINTER(BNBinaryWriter),
		ctypes.c_ushort,
	]
BNWriteBE32 = core.BNWriteBE32
BNWriteBE32.restype = ctypes.c_bool
BNWriteBE32.argtypes = [
		ctypes.POINTER(BNBinaryWriter),
		ctypes.c_uint,
	]
BNWriteBE64 = core.BNWriteBE64
BNWriteBE64.restype = ctypes.c_bool
BNWriteBE64.argtypes = [
		ctypes.POINTER(BNBinaryWriter),
		ctypes.c_ulonglong,
	]
BNWriteData = core.BNWriteData
BNWriteData.restype = ctypes.c_bool
BNWriteData.argtypes = [
		ctypes.POINTER(BNBinaryWriter),
		ctypes.c_void_p,
		ctypes.c_ulonglong,
	]
BNWriteLE16 = core.BNWriteLE16
BNWriteLE16.restype = ctypes.c_bool
BNWriteLE16.argtypes = [
		ctypes.POINTER(BNBinaryWriter),
		ctypes.c_ushort,
	]
BNWriteLE32 = core.BNWriteLE32
BNWriteLE32.restype = ctypes.c_bool
BNWriteLE32.argtypes = [
		ctypes.POINTER(BNBinaryWriter),
		ctypes.c_uint,
	]
BNWriteLE64 = core.BNWriteLE64
BNWriteLE64.restype = ctypes.c_bool
BNWriteLE64.argtypes = [
		ctypes.POINTER(BNBinaryWriter),
		ctypes.c_ulonglong,
	]
BNWriteViewBuffer = core.BNWriteViewBuffer
BNWriteViewBuffer.restype = ctypes.c_ulonglong
BNWriteViewBuffer.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.POINTER(BNDataBuffer),
	]
BNWriteViewData = core.BNWriteViewData
BNWriteViewData.restype = ctypes.c_ulonglong
BNWriteViewData.argtypes = [
		ctypes.POINTER(BNBinaryView),
		ctypes.c_ulonglong,
		ctypes.c_void_p,
		ctypes.c_ulonglong,
	]
_BNZlibCompress = core.BNZlibCompress
_BNZlibCompress.restype = ctypes.POINTER(BNDataBuffer)
_BNZlibCompress.argtypes = [
		ctypes.POINTER(BNDataBuffer),
	]
def BNZlibCompress(*args):
	result = _BNZlibCompress(*args)
	if not result:
		return None
	return result
_BNZlibDecompress = core.BNZlibDecompress
_BNZlibDecompress.restype = ctypes.POINTER(BNDataBuffer)
_BNZlibDecompress.argtypes = [
		ctypes.POINTER(BNDataBuffer),
	]
def BNZlibDecompress(*args):
	result = _BNZlibDecompress(*args)
	if not result:
		return None
	return result

# Helper functions
def handle_of_type(value, handle_type):
	if isinstance(value, ctypes.POINTER(handle_type)) or isinstance(value, ctypes.c_void_p):
		return ctypes.cast(value, ctypes.POINTER(handle_type))
	raise ValueError, 'expected pointer to %s' % str(handle_type)

# Set path for core plugins
BNSetBundledPluginDirectory(os.path.join(_base_path, "plugins"))
