import enum

class ActionType(enum.IntEnum):
	TemporaryAction = 0
	DataModificationAction = 1
	AnalysisAction = 2
	DataModificationAndAnalysisAction = 3


class AnalysisState(enum.IntEnum):
	IdleState = 0
	DisassembleState = 1
	AnalyzeState = 2


class BranchType(enum.IntEnum):
	UnconditionalBranch = 0
	FalseBranch = 1
	TrueBranch = 2
	CallDestination = 3
	FunctionReturn = 4
	SystemCall = 5
	IndirectBranch = 6
	UnresolvedBranch = 127


class CallingConventionName(enum.IntEnum):
	NoCallingConvention = 0
	CdeclCallingConvention = 1
	PascalCallingConvention = 2
	ThisCallCallingConvention = 3
	STDCallCallingConvention = 4
	FastcallCallingConvention = 5
	CLRCallCallingConvention = 6
	EabiCallCallingConvention = 7
	VectorCallCallingConvention = 8


class DisassemblyOption(enum.IntEnum):
	ShowAddress = 0
	ShowOpcode = 1
	ExpandLongOpcode = 2
	ShowVariablesAtTopOfGraph = 3
	ShowVariableTypesWhenAssigned = 4
	ShowDefaultRegisterTypes = 5
	ShowCallParameterNames = 6
	GroupLinearDisassemblyFunctions = 64
	ShowFlagUsage = 128


class Endianness(enum.IntEnum):
	LittleEndian = 0
	BigEndian = 1


class FindFlag(enum.IntEnum):
	NoFindFlags = 0
	FindCaseInsensitive = 1


class FlagRole(enum.IntEnum):
	SpecialFlagRole = 0
	ZeroFlagRole = 1
	PositiveSignFlagRole = 2
	NegativeSignFlagRole = 3
	CarryFlagRole = 4
	OverflowFlagRole = 5
	HalfCarryFlagRole = 6
	EvenParityFlagRole = 7
	OddParityFlagRole = 8


class FormInputFieldType(enum.IntEnum):
	LabelFormField = 0
	SeparatorFormField = 1
	TextLineFormField = 2
	MultilineTextFormField = 3
	IntegerFormField = 4
	AddressFormField = 5
	ChoiceFormField = 6
	OpenFileNameFormField = 7
	SaveFileNameFormField = 8
	DirectoryNameFormField = 9


class FunctionGraphType(enum.IntEnum):
	NormalFunctionGraph = 0
	LowLevelILFunctionGraph = 1
	LiftedILFunctionGraph = 2
	LowLevelILSSAFormFunctionGraph = 3
	MediumLevelILFunctionGraph = 4
	MediumLevelILSSAFormFunctionGraph = 5
	MappedMediumLevelILFunctionGraph = 6
	MappedMediumLevelILSSAFormFunctionGraph = 7


class HighlightColorStyle(enum.IntEnum):
	StandardHighlightColor = 0
	MixedHighlightColor = 1
	CustomHighlightColor = 2


class HighlightStandardColor(enum.IntEnum):
	NoHighlightColor = 0
	BlueHighlightColor = 1
	GreenHighlightColor = 2
	CyanHighlightColor = 3
	RedHighlightColor = 4
	MagentaHighlightColor = 5
	YellowHighlightColor = 6
	OrangeHighlightColor = 7
	WhiteHighlightColor = 8
	BlackHighlightColor = 9


class ILBranchDependence(enum.IntEnum):
	NotBranchDependent = 0
	TrueBranchDependent = 1
	FalseBranchDependent = 2


class ImplicitRegisterExtend(enum.IntEnum):
	NoExtend = 0
	ZeroExtendToFullWidth = 1
	SignExtendToFullWidth = 2


class InstructionTextTokenContext(enum.IntEnum):
	NoTokenContext = 0
	LocalVariableTokenContext = 1
	DataVariableTokenContext = 2
	FunctionReturnTokenContext = 3


class InstructionTextTokenType(enum.IntEnum):
	TextToken = 0
	InstructionToken = 1
	OperandSeparatorToken = 2
	RegisterToken = 3
	IntegerToken = 4
	PossibleAddressToken = 5
	BeginMemoryOperandToken = 6
	EndMemoryOperandToken = 7
	FloatingPointToken = 8
	AnnotationToken = 9
	CodeRelativeAddressToken = 10
	ArgumentNameToken = 11
	HexDumpByteValueToken = 12
	HexDumpSkippedByteToken = 13
	HexDumpInvalidByteToken = 14
	HexDumpTextToken = 15
	OpcodeToken = 16
	StringToken = 17
	CharacterConstantToken = 18
	KeywordToken = 19
	TypeNameToken = 20
	FieldNameToken = 21
	CodeSymbolToken = 64
	DataSymbolToken = 65
	LocalVariableToken = 66
	ImportToken = 67
	AddressDisplayToken = 68
	IndirectImportToken = 69


class IntegerDisplayType(enum.IntEnum):
	DefaultIntegerDisplayType = 0
	BinaryDisplayType = 1
	SignedOctalDisplayType = 2
	UnsignedOctalDisplayType = 3
	SignedDecimalDisplayType = 4
	UnsignedDecimalDisplayType = 5
	SignedHexadecimalDisplayType = 6
	UnsignedHexadecimalDisplayType = 7
	CharacterConstantDisplayType = 8
	PointerDisplayType = 9


class LinearDisassemblyLineType(enum.IntEnum):
	BlankLineType = 0
	CodeDisassemblyLineType = 1
	DataVariableLineType = 2
	HexDumpLineType = 3
	FunctionHeaderLineType = 4
	FunctionHeaderStartLineType = 5
	FunctionHeaderEndLineType = 6
	FunctionContinuationLineType = 7
	LocalVariableLineType = 8
	LocalVariableListEndLineType = 9
	FunctionEndLineType = 10
	NoteStartLineType = 11
	NoteLineType = 12
	NoteEndLineType = 13
	SectionStartLineType = 14
	SectionEndLineType = 15
	SectionSeparatorLineType = 16
	NonContiguousSeparatorLineType = 17


class LogLevel(enum.IntEnum):
	DebugLog = 0
	InfoLog = 1
	WarningLog = 2
	ErrorLog = 3
	AlertLog = 4


class LowLevelILFlagCondition(enum.IntEnum):
	LLFC_E = 0
	LLFC_NE = 1
	LLFC_SLT = 2
	LLFC_ULT = 3
	LLFC_SLE = 4
	LLFC_ULE = 5
	LLFC_SGE = 6
	LLFC_UGE = 7
	LLFC_SGT = 8
	LLFC_UGT = 9
	LLFC_NEG = 10
	LLFC_POS = 11
	LLFC_O = 12
	LLFC_NO = 13


class LowLevelILOperation(enum.IntEnum):
	LLIL_NOP = 0
	LLIL_SET_REG = 1
	LLIL_SET_REG_SPLIT = 2
	LLIL_SET_FLAG = 3
	LLIL_LOAD = 4
	LLIL_STORE = 5
	LLIL_PUSH = 6
	LLIL_POP = 7
	LLIL_REG = 8
	LLIL_CONST = 9
	LLIL_CONST_PTR = 10
	LLIL_FLAG = 11
	LLIL_FLAG_BIT = 12
	LLIL_ADD = 13
	LLIL_ADC = 14
	LLIL_SUB = 15
	LLIL_SBB = 16
	LLIL_AND = 17
	LLIL_OR = 18
	LLIL_XOR = 19
	LLIL_LSL = 20
	LLIL_LSR = 21
	LLIL_ASR = 22
	LLIL_ROL = 23
	LLIL_RLC = 24
	LLIL_ROR = 25
	LLIL_RRC = 26
	LLIL_MUL = 27
	LLIL_MULU_DP = 28
	LLIL_MULS_DP = 29
	LLIL_DIVU = 30
	LLIL_DIVU_DP = 31
	LLIL_DIVS = 32
	LLIL_DIVS_DP = 33
	LLIL_MODU = 34
	LLIL_MODU_DP = 35
	LLIL_MODS = 36
	LLIL_MODS_DP = 37
	LLIL_NEG = 38
	LLIL_NOT = 39
	LLIL_SX = 40
	LLIL_ZX = 41
	LLIL_LOW_PART = 42
	LLIL_JUMP = 43
	LLIL_JUMP_TO = 44
	LLIL_CALL = 45
	LLIL_CALL_STACK_ADJUST = 46
	LLIL_RET = 47
	LLIL_NORET = 48
	LLIL_IF = 49
	LLIL_GOTO = 50
	LLIL_FLAG_COND = 51
	LLIL_CMP_E = 52
	LLIL_CMP_NE = 53
	LLIL_CMP_SLT = 54
	LLIL_CMP_ULT = 55
	LLIL_CMP_SLE = 56
	LLIL_CMP_ULE = 57
	LLIL_CMP_SGE = 58
	LLIL_CMP_UGE = 59
	LLIL_CMP_SGT = 60
	LLIL_CMP_UGT = 61
	LLIL_TEST_BIT = 62
	LLIL_BOOL_TO_INT = 63
	LLIL_ADD_OVERFLOW = 64
	LLIL_SYSCALL = 65
	LLIL_BP = 66
	LLIL_TRAP = 67
	LLIL_UNDEF = 68
	LLIL_UNIMPL = 69
	LLIL_UNIMPL_MEM = 70
	LLIL_SET_REG_SSA = 71
	LLIL_SET_REG_SSA_PARTIAL = 72
	LLIL_SET_REG_SPLIT_SSA = 73
	LLIL_REG_SPLIT_DEST_SSA = 74
	LLIL_REG_SSA = 75
	LLIL_REG_SSA_PARTIAL = 76
	LLIL_SET_FLAG_SSA = 77
	LLIL_FLAG_SSA = 78
	LLIL_FLAG_BIT_SSA = 79
	LLIL_CALL_SSA = 80
	LLIL_SYSCALL_SSA = 81
	LLIL_CALL_PARAM_SSA = 82
	LLIL_CALL_STACK_SSA = 83
	LLIL_CALL_OUTPUT_SSA = 84
	LLIL_LOAD_SSA = 85
	LLIL_STORE_SSA = 86
	LLIL_REG_PHI = 87
	LLIL_FLAG_PHI = 88
	LLIL_MEM_PHI = 89


class MediumLevelILOperation(enum.IntEnum):
	MLIL_NOP = 0
	MLIL_SET_VAR = 1
	MLIL_SET_VAR_FIELD = 2
	MLIL_SET_VAR_SPLIT = 3
	MLIL_LOAD = 4
	MLIL_LOAD_STRUCT = 5
	MLIL_STORE = 6
	MLIL_STORE_STRUCT = 7
	MLIL_VAR = 8
	MLIL_VAR_FIELD = 9
	MLIL_ADDRESS_OF = 10
	MLIL_ADDRESS_OF_FIELD = 11
	MLIL_CONST = 12
	MLIL_CONST_PTR = 13
	MLIL_IMPORT = 14
	MLIL_ADD = 15
	MLIL_ADC = 16
	MLIL_SUB = 17
	MLIL_SBB = 18
	MLIL_AND = 19
	MLIL_OR = 20
	MLIL_XOR = 21
	MLIL_LSL = 22
	MLIL_LSR = 23
	MLIL_ASR = 24
	MLIL_ROL = 25
	MLIL_RLC = 26
	MLIL_ROR = 27
	MLIL_RRC = 28
	MLIL_MUL = 29
	MLIL_MULU_DP = 30
	MLIL_MULS_DP = 31
	MLIL_DIVU = 32
	MLIL_DIVU_DP = 33
	MLIL_DIVS = 34
	MLIL_DIVS_DP = 35
	MLIL_MODU = 36
	MLIL_MODU_DP = 37
	MLIL_MODS = 38
	MLIL_MODS_DP = 39
	MLIL_NEG = 40
	MLIL_NOT = 41
	MLIL_SX = 42
	MLIL_ZX = 43
	MLIL_LOW_PART = 44
	MLIL_JUMP = 45
	MLIL_JUMP_TO = 46
	MLIL_CALL = 47
	MLIL_CALL_UNTYPED = 48
	MLIL_CALL_OUTPUT = 49
	MLIL_CALL_PARAM = 50
	MLIL_RET = 51
	MLIL_NORET = 52
	MLIL_IF = 53
	MLIL_GOTO = 54
	MLIL_CMP_E = 55
	MLIL_CMP_NE = 56
	MLIL_CMP_SLT = 57
	MLIL_CMP_ULT = 58
	MLIL_CMP_SLE = 59
	MLIL_CMP_ULE = 60
	MLIL_CMP_SGE = 61
	MLIL_CMP_UGE = 62
	MLIL_CMP_SGT = 63
	MLIL_CMP_UGT = 64
	MLIL_TEST_BIT = 65
	MLIL_BOOL_TO_INT = 66
	MLIL_ADD_OVERFLOW = 67
	MLIL_SYSCALL = 68
	MLIL_SYSCALL_UNTYPED = 69
	MLIL_BP = 70
	MLIL_TRAP = 71
	MLIL_UNDEF = 72
	MLIL_UNIMPL = 73
	MLIL_UNIMPL_MEM = 74
	MLIL_SET_VAR_SSA = 75
	MLIL_SET_VAR_SSA_FIELD = 76
	MLIL_SET_VAR_SPLIT_SSA = 77
	MLIL_SET_VAR_ALIASED = 78
	MLIL_SET_VAR_ALIASED_FIELD = 79
	MLIL_VAR_SSA = 80
	MLIL_VAR_SSA_FIELD = 81
	MLIL_VAR_ALIASED = 82
	MLIL_VAR_ALIASED_FIELD = 83
	MLIL_CALL_SSA = 84
	MLIL_CALL_UNTYPED_SSA = 85
	MLIL_SYSCALL_SSA = 86
	MLIL_SYSCALL_UNTYPED_SSA = 87
	MLIL_CALL_PARAM_SSA = 88
	MLIL_CALL_OUTPUT_SSA = 89
	MLIL_LOAD_SSA = 90
	MLIL_LOAD_STRUCT_SSA = 91
	MLIL_STORE_SSA = 92
	MLIL_STORE_STRUCT_SSA = 93
	MLIL_VAR_PHI = 94
	MLIL_MEM_PHI = 95


class MemberAccess(enum.IntEnum):
	NoAccess = 0
	PrivateAccess = 1
	ProtectedAccess = 2
	PublicAccess = 3


class MemberScope(enum.IntEnum):
	NoScope = 0
	StaticScope = 1
	VirtualScope = 2
	ThunkScope = 3
	FriendScope = 4


class MessageBoxButtonResult(enum.IntEnum):
	NoButton = 0
	YesButton = 1
	OKButton = 2
	CancelButton = 3


class MessageBoxButtonSet(enum.IntEnum):
	OKButtonSet = 0
	YesNoButtonSet = 1
	YesNoCancelButtonSet = 2


class MessageBoxIcon(enum.IntEnum):
	InformationIcon = 0
	QuestionIcon = 1
	WarningIcon = 2
	ErrorIcon = 3


class MetadataType(enum.IntEnum):
	InvalidDataType = 0
	BooleanDataType = 1
	StringDataType = 2
	UnsignedIntegerDataType = 3
	SignedIntegerDataType = 4
	DoubleDataType = 5
	RawDataType = 6
	KeyValueDataType = 7
	ArrayDataType = 8


class ModificationStatus(enum.IntEnum):
	Original = 0
	Changed = 1
	Inserted = 2


class NameType(enum.IntEnum):
	NoNameType = 0
	ConstructorNameType = 1
	DestructorNameType = 2
	OperatorNewNameType = 3
	OperatorDeleteNameType = 4
	OperatorAssignNameType = 5
	OperatorRightShiftNameType = 6
	OperatorLeftShiftNameType = 7
	OperatorNotNameType = 8
	OperatorEqualNameType = 9
	OperatorNotEqualNameType = 10
	OperatorArrayNameType = 11
	OperatorArrowNameType = 12
	OperatorStarNameType = 13
	OperatorIncrementNameType = 14
	OperatorDecrementNameType = 15
	OperatorMinusNameType = 16
	OperatorPlusNameType = 17
	OperatorBitAndNameType = 18
	OperatorArrowStarNameType = 19
	OperatorDivideNameType = 20
	OperatorModulusNameType = 21
	OperatorLessThanNameType = 22
	OperatorLessThanEqualNameType = 23
	OperatorGreaterThanNameType = 24
	OperatorGreaterThanEqualNameType = 25
	OperatorCommaNameType = 26
	OperatorParenthesesNameType = 27
	OperatorTildeNameType = 28
	OperatorXorNameType = 29
	OperatorBitOrNameType = 30
	OperatorLogicalAndNameType = 31
	OperatorLogicalOrNameType = 32
	OperatorStarEqualNameType = 33
	OperatorPlusEqualNameType = 34
	OperatorMinusEqualNameType = 35
	OperatorDivideEqualNameType = 36
	OperatorModulusEqualNameType = 37
	OperatorRightShiftEqualNameType = 38
	OperatorLeftShiftEqualNameType = 39
	OperatorAndEqualNameType = 40
	OperatorOrEqualNameType = 41
	OperatorXorEqualNameType = 42
	VFTableNameType = 43
	VBTableNameType = 44
	VCallNameType = 45
	TypeofNameType = 46
	LocalStaticGuardNameType = 47
	StringNameType = 48
	VBaseDestructorNameType = 49
	VectorDeletingDestructorNameType = 50
	DefaultConstructorClosureNameType = 51
	ScalarDeletingDestructorNameType = 52
	VectorConstructorIteratorNameType = 53
	VectorDestructorIteratorNameType = 54
	VectorVBaseConstructorIteratoreNameType = 55
	VirtualDisplacementMapNameType = 56
	EHVectorConstructorIteratorNameType = 57
	EHVectorDestructorIteratorNameType = 58
	EHVectorVBaseConstructorIteratorNameType = 59
	CopyConstructorClosureNameType = 60
	UDTReturningNameType = 61
	LocalVFTableNameType = 62
	LocalVFTableConstructorClosureNameType = 63
	OperatorNewArrayNameType = 64
	OperatorDeleteArrayNameType = 65
	PlacementDeleteClosureNameType = 66
	PlacementDeleteClosureArrayNameType = 67
	OperatorReturnTypeNameType = 68
	RttiTypeDescriptor = 69
	RttiBaseClassDescriptor = 70
	RttiBaseClassArray = 71
	RttiClassHeirarchyDescriptor = 72
	RttiCompleteObjectLocator = 73
	OperatorUnaryMinusNameType = 74
	OperatorUnaryPlusNameType = 75
	OperatorUnaryBitAndNameType = 76
	OperatorUnaryStarNameType = 77


class NamedTypeReferenceClass(enum.IntEnum):
	UnknownNamedTypeClass = 0
	TypedefNamedTypeClass = 1
	ClassNamedTypeClass = 2
	StructNamedTypeClass = 3
	UnionNamedTypeClass = 4
	EnumNamedTypeClass = 5


class PluginCommandType(enum.IntEnum):
	DefaultPluginCommand = 0
	AddressPluginCommand = 1
	RangePluginCommand = 2
	FunctionPluginCommand = 3


class PluginLoadOrder(enum.IntEnum):
	EarlyPluginLoadOrder = 0
	NormalPluginLoadOrder = 1
	LatePluginLoadOrder = 2


class PluginOrigin(enum.IntEnum):
	OfficialPluginOrigin = 0
	CommunityPluginOrigin = 1
	OtherPluginOrigin = 2


class PluginType(enum.IntEnum):
	CorePluginType = 0
	UiPluginType = 1
	ArchitecturePluginType = 2
	BinaryViewPluginType = 3


class PluginUpdateStatus(enum.IntEnum):
	UpToDatePluginStatus = 0
	UpdatesAvailablePluginStatus = 1


class PointerSuffix(enum.IntEnum):
	Ptr64Suffix = 0
	UnalignedSuffix = 1
	RestrictSuffix = 2
	ReferenceSuffix = 3
	LvalueSuffix = 4


class ReferenceType(enum.IntEnum):
	PointerReferenceType = 0
	ReferenceReferenceType = 1
	RValueReferenceType = 2
	NoReference = 3


class RegisterValueType(enum.IntEnum):
	UndeterminedValue = 0
	EntryValue = 1
	ConstantValue = 2
	ConstantPointerValue = 3
	StackFrameOffset = 4
	ReturnAddressValue = 5
	ImportedAddressValue = 6
	SignedRangeValue = 7
	UnsignedRangeValue = 8
	LookupTableValue = 9
	InSetOfValues = 10
	NotInSetOfValues = 11


class ScriptingProviderExecuteResult(enum.IntEnum):
	InvalidScriptInput = 0
	IncompleteScriptInput = 1
	SuccessfulScriptExecution = 2


class ScriptingProviderInputReadyState(enum.IntEnum):
	NotReadyForInput = 0
	ReadyForScriptExecution = 1
	ReadyForScriptProgramInput = 2


class SectionSemantics(enum.IntEnum):
	DefaultSectionSemantics = 0
	ReadOnlyCodeSectionSemantics = 1
	ReadOnlyDataSectionSemantics = 2
	ReadWriteDataSectionSemantics = 3


class SegmentFlag(enum.IntEnum):
	SegmentExecutable = 1
	SegmentWritable = 2
	SegmentReadable = 4
	SegmentContainsData = 8
	SegmentContainsCode = 16
	SegmentDenyWrite = 32
	SegmentDenyExecute = 64


class StringType(enum.IntEnum):
	AsciiString = 0
	Utf16String = 1
	Utf32String = 2


class StructureType(enum.IntEnum):
	ClassStructureType = 0
	StructStructureType = 1
	UnionStructureType = 2


class SymbolType(enum.IntEnum):
	FunctionSymbol = 0
	ImportAddressSymbol = 1
	ImportedFunctionSymbol = 2
	DataSymbol = 3
	ImportedDataSymbol = 4


class TransformType(enum.IntEnum):
	BinaryCodecTransform = 0
	TextCodecTransform = 1
	UnicodeCodecTransform = 2
	DecodeTransform = 3
	BinaryEncodeTransform = 4
	TextEncodeTransform = 5
	EncryptTransform = 6
	InvertingTransform = 7
	HashTransform = 8


class TypeClass(enum.IntEnum):
	VoidTypeClass = 0
	BoolTypeClass = 1
	IntegerTypeClass = 2
	FloatTypeClass = 3
	StructureTypeClass = 4
	EnumerationTypeClass = 5
	PointerTypeClass = 6
	ArrayTypeClass = 7
	FunctionTypeClass = 8
	VarArgsTypeClass = 9
	ValueTypeClass = 10
	NamedTypeReferenceClass = 11


class UpdateResult(enum.IntEnum):
	UpdateFailed = 0
	UpdateSuccess = 1
	AlreadyUpToDate = 2


class VariableSourceType(enum.IntEnum):
	StackVariableSourceType = 0
	RegisterVariableSourceType = 1
	FlagVariableSourceType = 2
