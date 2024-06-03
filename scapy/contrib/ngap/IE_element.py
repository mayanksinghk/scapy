import common_types

# Base class for Information Element (IE)
class IEBase(Packet):
    pass


# Radio Network Layer Related IEs
# 9.3.1.1 Message Type
class IEMessageType(IEBase):
    name="Message Type"
    fields_desc = []
    pass

# 9.3.1.2 Cause
class IECause(IEBase):
    name="Cause"
    fields_desc = []
    pass

# 9.3.1.3 Criticality Diagnostics
class IECriticalityDiagnostics(IEBase):
    name="Criticality Diagnostics"
    fields_desc = []
    pass

# 9.3.1.4 Bit Rate
class IEBitRate(IEBase):
    name="Bit Rate"
    fields_desc = []
    pass

# 9.3.1.5 Global RAN Node ID
class IEGlobalRANNodeID(IEBase):
    name="Global RAN Node ID"
    fields_desc = []
    pass

# 9.3.1.6 Global gNB ID
class IEGlobalgNBID(IEBase):
    name="Global gNB ID"
    fields_desc = []
    pass

# 9.3.1.7 NR CGI
class IENRCGI(IEBase):
    name="NR CGI"
    fields_desc = []
    pass

# 9.3.1.8 Global ng-eNB ID
class IEGlobalngeNBID(IEBase):
    name="Global ng-eNB ID"
    fields_desc = []
    pass

# 9.3.1.9 E-UTRA CGI
class IEEUTRACGI(IEBase):
    name="E-UTRA CGI"
    fields_desc = []
    pass

# 9.3.1.10 GBR QoS Flow Information
class IEGBRQoSFlowInformation(IEBase):
    name="GBR QoS Flow Information"
    fields_desc = []
    pass

# 9.3.1.12 QoS Flow Level QoS Parameters
class IEQoSFlowLevelQoSParameters(IEBase):
    name="QoS FLow Level QoS Parameters"
    fields_desc = []
    pass

# 9.3.1.13 QoS Flow List with Cause 
class IEQoSFlowListwithCause(IEBase):
    name="QoS Flow List with Cause"
    fields_desc = []
    pass

# 9.3.1.14 Trace Activation
class IETraceActivation(IEBase):
    name="Trace Activation"
    fields_desc = []
    pass

# 9.3.1.15 Core Network Assistance Information for RRC INACTIVE
class IECoreNetworkAssistanceInfoforRRCINACTIVE(IEBase):
    name="Core Network Assistance Information for RRC INACTIVE"
    fields_desc = []
    pass

# 9.3.1.16 User Location Information
class IEUserLocationInformation(IEBase):
    name="User Location Information"
    fields_desc = []
    pass

# 9.3.1.17 Slice Support List
class IESliceSupportList(IEBase):
    name="Slice Support List"
    fields_desc = []
    pass

# 9.3.1.18 Dynamic 5QI Descriptor
class IEDynamic5QIDescriptor(IEBase):
    name="Dynamic 5QI Descriptor"
    fields_desc = []
    pass

# 9.3.1.19 Allocation and Retention Policy 
class IEAllocationandRetentionPolicy(IEBase):
    name="Allocation and Retention Policy"
    fields_desc = []
    pass

# 9.3.1.20 Source to Target Transport Container
class IESourcetoTargetTransportContainer(IEBase):
    name="Source to Target Transport Container"
    fields_desc = []
    pass

# 9.3.1.21 Target to Source Transparent Container
class IETargettoSourceTransparentContainer(IEBase):
    name="Target to Source Transparent Container"
    fields_desc = []
    pass

# 9.3.1.22 Handover Type
class IEHandoverType(IEBase):
    name="Handover Type"
    fields_desc = []
    pass

# 9.3.1.23 MICO Mode Indication
class IEMICOModeIndication(IEBase):
    name="MICO Mode Indication"
    fields_desc = []
    pass

# 9.3.1.24 S-NSSAI
class IES_NSSAI(IEBase):
    name="S-NSSAI"
    fields_desc = []
    pass

# 9.3.1.25 Target ID
class IETargetID(IEBase):
    name="Target ID"
    pass

# 9.3.1.26 Emergency Fallback Indicator
class IEEmergencyFallbackIndicator(IEBase):
    name="Emergency Fallback Indicator"
    fields_desc = []
    pass

# 9.3.1.27 Security Indication
class IESecurityIndication(IEBase):
    name="Security Indication"
    fields_desc = []
    pass

# 9.3.1.28 Non Dynamic 5QI Descriptor
class IENonDynamic5QIDescriptor(IEBase):
    name="Non Dynamic 5QI Descriptor"
    fields_desc = []
    pass

# 9.3.1.29 Source NG-RAN Node to Target NG-RAN Node Transparent Container
class IESourceNG_RANNodetoTargetNG_RANNodeTransparentContainer(IEBase):
    name="Source NG-RAN Node to target NG-RAN Node Transparent Container"
    fields_desc = []
    pass

# 9.3.1.30 Target NG-RAN Node to Source NG-RAN Node Transparent Container
class IETargetNG_RANNodetoSourceNG_RANNodeTransparentContainer(IEBase):
    name="Target NG-RAN Node to Source NG-RAN Node Transparent Container"
    fields_desc = []
    pass

# 9.3.1.31 Allowed NSSAI
class IEAllowedNSSAI(IEBase):
    name="Allowed NSSAI"
    fields_desc = []
    pass

# 9.3.1.32 Relative AMF Capacity
class IERelativeAMFCapacity(IEBase):
    name="Relative AMF Capacity"
    fields_desc = []
    pass

# 9.3.1.33 DL Forwarding
class IEDLForwarding(IEBase):
    name="DL Forwarding"
    fields_desc = []
    pass

# 9.3.1.34 DRBs to QoS Flows Mapping List
class IEDRBstoQoSFlowsMappingList(IEBase):
    name="DRBs to QoS Flows Mapping List"
    fields_desc = []
    pass

# 9.3.1.35 Message Identifier
class IEMessageIdentifier(IEBase):
    name="Message Identifier"
    fields_desc = []
    pass

# 9.3.1.36 Serial Number
class IESerialNumber(IEBase):
    name="Serial Number"
    fields_desc = []
    pass

# 9.3.1.37 Warning Area List
class IEWarningAreaList(IEBase):
    name="Warning Area List"
    fields_desc = []
    pass

# 9.3.1.38 Number of Broadcasts Requested
class IENumberofBroadcastsRequested(IEBase):
    name="Number of Broadcasts Requested"
    fields_desc = []
    pass

# 9.3.1.39 Warning Type
class IEWarningType(IEBase):
    name="Warning Type"
    fields_desc = []
    pass

# 9.3.1.41 Data Coding Scheme
class IEDataCodingScheme(IEBase):
    name="Data Coding Scheme"
    fields_desc = []
    pass

# 9.3.1.42 Warning Message Contents
class IEWarningMessageContents(IEBase):
    name="Warning Message Contents"
    fields_desc = []
    pass

# 9.3.1.43 Broadcast Completed Area List
class IEBroadcastCompletedAreaList(IEBase):
    name="Broadcast Completed Area List"
    fields_desc = []
    pass

# 9.3.1.44 Broadcast Cancelled Area List
class IEBroadcastCancelledAreaList(IEBase):
    name="Broadcast Cancelled Area List"
    fields_desc = []
    pass

# 9.3.1.45 Number of Broadcasts
class IENumberofBroadcasts(IEBase):
    name="Number of Broadcasts"
    fields_desc = []
    pass

# 9.3.1.46 Concurrent Warning Message Indicator
class IEConcurrentWarningMessageIndicator(IEBase):
    name="Concurrent Warning Message Indicator"
    fields_desc = []
    pass

# 9.3.1.47 Cancel-All Warning Messages Indicator
class IECancel_AllWarningMessagesIndicator(IEBase):
    name="Cancel-All Warning Message Indicator"
    fields_desc = []
    pass

# 9.3.1.48 Emergency Area ID
class IEEmergencyAreaID(IEBase):
    name="Emergency Area ID"
    fields_desc = []
    pass

# 9.3.1.49 Repetition Period
class IERepetitionPeriod(IEBase):
    name="Repetition Period"
    fields_desc = []
    pass

# 9.3.1.50 PDU Session ID
class IEPDUSessionID(IEBase):
    name="PDU Session ID"
    fields_desc = []
    pass

# 9.3.1.51 QoS Flow Identifier
class IEQoSFlowIdentifier(IEBase):
    name="QoS Flow Identifier"
    fields_desc = []
    pass

# 9.3.1.52 PDU Session Type
class IEPDUSessionType(IEBase):
    name="PDU Session Type"
    fields_desc = []
    pass

# 9.3.1.53 DRB ID
class IEDRBID(IEBase):
    name="DRB ID"
    fields_desc = []
    pass

# 9.3.1.54 Masked IMEISV
class IEMaskedIMEISV(IEBase):
    name="Masked IMEISV"
    fields_desc = []
    pass

# 9.3.1.55 New Security Context Indicator
class IENewSecurityContextIndicator(IEBase):
    name="New Security Context Indicator"
    fields_desc = []
    pass

# 9.3.1.56 Time to Wait
class IETimetoWait(IEBase):
    name="Time to Wait"
    fields_desc = []
    pass

# 9.3.1.57 Global N3IWF ID
class IEGlobalN3IWFID(IEBase):
    name="Global N3IWF ID"
    fields_desc = []
    pass

# 9.3.1.58 UE Aggregate Maximum Bit Rate
class IEUEAggregateMaximumBitRate(IEBase):
    name="UE Aggregate Maximum Bit Rate"
    fields_desc = []
    pass

# 9.3.1.59 Security Result
class IESecurityResult(IEBase):
    name="Security Result"
    fields_desc = []
    pass

# 9.3.1.60 User Plane Security Information
class IEUserPlaneSecurityInformation(IEBase):
    name="User Plane Security Information"
    fields_desc = []
    pass

# 9.3.1.61 Index to RAT/Frequency Selection Priority
class IEIndextoRATorFrequencySelectionPriority(IEBase):
    name="Index to RAT/Frequency Selection Priority"
    fields_desc = []
    pass

# 9.3.1.62 Data Forwarding Accepted
class IEDataForwardingAccepted(IEBase):
    name="Data Forwarding Accepted"
    fields_desc = []
    pass

# 9.3.1.63 Data Forwarding Not Possible
class IEDataForwardingNotPossible(IEBase):
    name="Data Forwarding Not Possible"
    fields_desc = []
    pass

# 9.3.1.64 Direct Forwarding Path Availability
class IEDirectForwardingPathAvailability(IEBase):
    name="Direct Forwarding Path Availablility"
    fields_desc = []
    pass

# 9.3.1.65 Location Reporting Request Type
class IELocationReportingRequestType(IEBase):
    name="Location Reporting Request Type"
    fields_desc = []
    pass

# 9.3.1.66 Area of Interest
class IEAreaofInterest(IEBase):
    name="Area of Interest"
    fields_desc = []
    pass

# 9.3.1.67 UE Presence in Area of Interest List
class IEUEPresenceinAreaofInterestList(IEBase):
    name="UE Presence in Area of Interest List"
    fields_desc = []
    pass

# 9.3.1.68 UE Radio Capability for Paging
class IEUERadioCapabilityforPaging(IEBase):
    name="UE Radio Capability for Paging"
    fields_desc = []
    pass

# 9.3.1.69 Assistance Data for Paging
class IEAssistanceDataforPaging(IEBase):
    name="Assistance Data for Paging"
    fields_desc = []
    pass

# 9.3.1.70 Assistance Data for Recommended Cells
class IEAssistanceDataforRecommendedCells(IEBase):
    name="Assistance Data for Recommended Calls"
    fields_desc = []
    pass

# 9.3.1.71 Recommended Cells for Paging
class IERecommendedCellsforPaging(IEBase):
    name="Recommmended Cells for Paging"
    fields_desc = []
    pass

# 9.3.1.72 Paging Attempt Information
class IEPagingAttemptInformation(IEBase):
    name="Paging Attempt Information"
    fields_desc = []
    pass

# 9.3.1.73 NG-RAN CGI
class IENG_RANCGI(IEBase):
    name="NG-RAN CGI"
    fields_desc = []
    pass

# 9.3.1.74 UE Radio Capability
class IEUERadioCapability(IEBase):
    name="UE Radio Capability"
    fields_desc = []
    pass

# 9.3.1.74a UE Radio Capability - E-UTRA Format
class IEUERadioCapability_E_UTRAFormat(IEBase):
    name="UE Radio Capability - E-UTRA format"
    fields_desc = []
    pass

# 9.3.1.75 Time Stamp
class IETimeStamp(IEBase):
    name="Time Stamp"
    fields_desc = []
    pass

# 9.3.1.76 Location Reporting Reference ID
class IELocationReportingReferenceID(IEBase):
    name="Location Reporting Reference ID"
    fields_desc = []
    pass

# 9.3.1.77 Data Forwarding Response DRB List
class IEDataForwardingResponseDRBList(IEBase):
    name="Data Forwarding Response DRB List"
    fields_desc = []
    pass

# 9.3.1.78 Paging Priority
class IEPagingPriority(IEBase):
    name="Paging Priority"
    fields_desc = []
    pass

# 9.3.1.79 Packet Loss Rate
class IEPacketLossRate(IEBase):
    name="Packet Loss Rate"
    fields_desc = []
    pass

# 9.3.1.80 Packet Delay Budget
class IEPacketDelayBudget(IEBase):
    name="Packet Delay Budget"
    fields_desc = []
    pass

# 9.3.1.81 Packet Error Rate
class IEPacketErrorRate(IEBase):
    name="Packet Error Rate"
    fields_desc = []
    pass

# 9.3.1.82 Averaging Window
class IEAveragingWindow(IEBase):
    name="Averging Window"
    fields_desc = []
    pass

# 9.3.1.83 Maximum Data Burst Volume
class IEMaximumDataBurstVolume(IEBase):
    name="Maximum Data Burst Volume"
    fields_desc = []
    pass

# 9.3.1.84 Priority Level
class IEPriorityLevel(IEBase):
    name="Priority Level"
    fields_desc = []
    pass

# 9.3.1.85 Mobility Restriction List
class IEMobilityRestrictionList(IEBase):
    name="Mobility Restriction List"
    fields_desc = []
    pass

# 9.3.1.86 UE Security Capabilities
class IEUESecurityCapabilities(IEBase):
    name="UE Security Capabilities"
    fields_desc = []
    pass

# 9.3.1.87 Security Key
class IESecurityKey(IEBase):
    name="Security Key"
    fields_desc = []
    pass

# 9.3.1.88 Security Context
class IESecurityContext(IEBase):
    name="Security Context"
    fields_desc = []
    pass

# 9.3.1.89 IMS Voice Support Indicator
class IEIMSVoiceSupportIndicator(IEBase):
    name="IMS Voice Support Indicator"
    fields_desc = []
    pass

# 9.3.1.90 Paging DRX
class IEPagingDRX(IEBase):
    name="Paging DRX"
    fields_desc = []
    pass

# 9.3.1.91 RRC Inactive Transition Report Request 
class IERRCInactiveTransitionReportRequest(IEBase):
    name="RRC Inactive Transition Report Request"
    fields_desc = []
    pass

# 9.3.1.92 RRC State
class IERRCState(IEBase):
    name="RRC State"
    fields_desc = []
    pass

# 9.3.1.93 Expected UE Behaviour
class IEExpectedUEBehaviour(IEBase):
    name="Expected UE Behaviour"
    fields_desc = []
    pass

# 9.3.1.94 Expected UE Activity Behaviour
class IEExpectedUEActivityBehaviour(IEBase):
    name="Expected UE Activity Behaviour"
    fields_desc = []
    pass

# 9.3.1.95 UE History Information
class IEUEHistoryInformation(IEBase):
    name="UE History Information"
    fields_desc = []
    pass

# 9.3.1.96 Last Visited Cell Information
class IELastVisitedCellInformation(IEBase):
    name="Last Visited Cell Information"
    fields_desc = []
    pass

# 9.3.1.97 Last Visited NG-RAN Cell Information
class IELastVisitedNG_RANCellInformation(IEBase):
    name="Last Visited NG-RAN Cell Information"
    fields_desc = []
    pass

# 9.3.1.98 Cell Type
class IECellType(IEBase):
    name="Cell Type"
    fields_desc = []
    pass

# 9.3.1.99 Associated QoS Flow List
class IEAssociatedQoSFlowList(IEBase):
    name="Associtated QoS Flow List"
    fields_desc = []
    pass

# 9.3.1.100 Information on Recommended Cells and RAN Nodes for Paging
class IEInformationonRecommendedCellsandRANNodesforPaging(IEBase):
    name="Information on Recommended Cells and RAN Nodes for Paging"
    fields_desc = []
    pass

# 9.3.1.101 Recommended RAN Nodes for Paging
class IERecommendedRANNodesforPaging(IEBase):
    name="Recommended RAN Nodes for Paging"
    fields_desc = []
    pass

# 9.3.1.102 PDU Session Aggregate Maximum Bit Rate
class IEPDUSessionAggregateMaximumBitRate(IEBase):
    name="PDU Session Aggregate Maximum Bit Rate"
    fields_desc = []
    pass

# 9.3.1.103 Maximum Integrity Protected Data Rate
class IEMaximumIntegrityProtectedDataRate(IEBase):
    name="Maximum Integrity Protected Data Rate"
    fields_desc = []
    pass

# 9.3.1.104 Overload Response
class IEOverloadResponse(IEBase):
    name="Overload Response"
    fields_desc = []
    pass

# 9.3.1.105 Overload Action
class IEOverloadAction(IEBase):
    name="Overload Action"
    fields_desc = []
    pass

# 9.3.1.106 Traffic Load Reduction Indication
class IETrafficLoadReductionIndication(IEBase):
    name="Traffic Load Reduction Indication"
    fields_desc = []
    pass

# 9.3.1.107 Slice Overload List
class IESliceOverloadList(IEBase):
    name="Slice Overload List"
    fields_desc = []
    pass

# 9.3.1.108 RAN Status Transfer Transparent Container
class IERANStatusTransferTransparentContainer(IEBase):
    name="RAN Status Transfer Transparent Container"
    fields_desc = []
    pass

# 9.3.1.109 COUNT Value for PDCP SN Length 12
class IECOUNTValueforPDCPSNLength12(IEBase):
    name="COUNT Value for PDCP SN Length 12"
    fields_desc = []
    pass

d# 9.3.1.110 COUNT Value for PDCP SN Length 18
class IECOUNTValueforPDCPSNLength18(IEBase):
    name="COUNT Value for PDCP SN Length 18"
    fields_desc = []
    pass

# 9.3.1.111 RRC Establishment Cause
class IERRCEstablishmentCause(IEBase):
    name="RRC Establishment Cause"
    fields_desc = []
    pass

# 9.3.1.112 Warning Area Coordinates
class IEWarningAreaCoordinates(IEBase):
    name="Warning Area Coordinates"
    fields_desc = []
    pass

# 9.3.1.113 Network Instance
class IENetworkInstance(IEBase):
    name="Network Instance"
    fields_desc = []
    pass

# 9.3.1.114 Secondary RAT Usage Information
class IESecondaryRATUsageInformation(IEBase):
    name="Secondary RAT Usage Information"
    fields_desc = []
    pass


# 9.3.1.115 Volume Timed Report List
class IEVolumeTimedReportList(IEBase):
    name="Volume Timed Report List"
    fields_desc = []
    pass

# 9.3.1.116 Redirection for Voice EPS Fallback
class IERedirectionforVoiceEPSFallback(IEBase):
    name="Redirection for Voice EPS Fallback"
    fields_desc = []
    pass

# 9.3.1.117 UE Retention Information
class IEUERetentionInformation(IEBase):
    name="UE Retention Information"
    fields_desc = []
    pass

# 9.3.1.118 UL Forwarding
class IEULForwarding(IEBase):
    name="UL Forwarding"
    fields_desc = []
    pass

# 9.3.1.119 CN Assisted RAN Parameters Tuning
class IECNAssistedRANParametersTuning(IEBase):
    name="CN Assisted RAN Parameters Tuning"
    fields_desc = []
    pass

# 9.3.1.120 Common Network Instance
class IECommonNetworkInstance(IEBase):
    name="Common Network Instance"
    fields_desc = []
    pass

# 9.3.1.121 Data Forwarding Response E-RAB List
class IEDataForwardingResponseE_RABList(IEBase):
    name="Data Forwarding Response E-RAB List"
    fields_desc = []
    pass

# 9.3.1.122 gNB Set ID
class IEgNBSetID(IEBase):
    name="gNB Set ID"
    fields_desc = []
    pass

# 9.3.1.123 RNC-ID
class IERNC_ID(IEBase):
    name="RNC-ID"
    fields_desc = []
    pass

# 9.3.1.124 Extended RNC-ID
class IEExtendedRNC_ID(IEBase):
    name="Extended RNC-ID"
    fields_desc = []
    pass

# 9.3.1.125 RAT Information
class IERATInformation(IEBase):
    name="RAT Information"
    fields_desc = []
    pass

# 9.3.1.126 Extended RAT Restriction Information
class IEExtendedRATRestrictionInformation(IEBase):
    name="Extended RAT Restriction Information"
    fields_desc = []
    pass

# 9.3.1.127 SgNB UE X2AP ID
class IESgNBUEX2APID(IEBase):
    name="SgNB UE X2AP ID"
    fields_desc = []
    pass

# 9.3.1.128 SRVCC Operation Possible 
class IESRVCCOperationPossible(IEBase):
    name="SRVCC Operation Possible"
    fields_desc = []
    pass

# 9.3.1.129 IAB Authorized
class IEIABAuthorized(IEBase):
    name="IAB Authorized"
    fields_desc = []
    pass

# 9.3.1.130 TSC Traffic Characteristics
class IETSCTrafficCharacteristics(IEBase):
    name="TSC Traffic Characteristics"
    fields_desc = []
    pass

# 9.3.1.131 TSC Assistance Information
class IETSCAssistanceInformation(IEBase):
    name="TSC Assistance Information"
    fields_desc = []
    pass

# 9.3.1.132 Periodicity
class IEPeriodicity(IEBase):
    name="Periodicity"
    fields_desc = []
    pass

# 9.3.1.133 Burst Arrival Time
class IEBurstArrivalTime(IEBase):
    name="Burst Arrival Time"
    fields_desc = []
    pass

# 9.3.1.134 Redundant QoS Flow Indicator
class IERedundantQoSFlowIndicator(IEBase):
    name="Redundant QoS Flow Indicator"
    fields_desc = []
    pass

# 9.3.1.135 Extended Packet Delay Budget
class IEExtendedPacketDelayBudget(IEBase):
    name="Extended Packet Delay Budget"
    fields_desc = []
    pass

# 9.3.1.136 Redundant PDU Session Information
class IERedundantPDUSessionInformation(IEBase):
    name="Redundant PDU Session Information"
    fields_desc = []
    pass

# 9.3.1.137 NB-IoT Default Paging DRX
class IENB_IoTDefaultPagingDRX(IEBase):
    name="NB-IoT Default Paging DRX"
    fields_desc = []
    pass

# 9.3.1.138 NB-IoT Paging eDRX Information
class IENB_IoTPagingeDRXInformation(IEBase):
    name="NB-IoT Paging eDRX Information"
    fields_desc = []
    pass

# 9.3.1.139 NB-IoT Paging DRX
class IENB_IoTPagingDRX(IEBase):
    name="NB-IoT Paging DRX"
    fields_desc = []
    pass

# 9.3.1.140 Enhanced Coverage Restriction
class IEEnhancedCoverageRestriction(IEBase):
    name="Enhanced Coverage Restriction"
    fields_desc = []
    pass

# 9.3.1.141 Paging Assistance Data for CE Capable UE
class IEPagingAssistanceDataforCECapableUE(IEBase):
    name="Paging Assistance Data for CE Capable UE"
    fields_desc = []
    pass

# 9.3.1.142 UE Radio Capability ID
class IEUERadioCapabilityID(IEBase):
    name="UE Radio Capability ID"
    fields_desc = []
    pass

# 9.3.1.143 WUS Assistance Information
class IEWUSAssistanceInformation(IEBase):
    name="WUS Assistance Information"
    fields_desc = []
    pass

# 9.3.1.144 UE Differentiation Information
class IEUEDifferentiationInformation(IEBase):
    name="UE Differentiation Information"
    fields_desc = []
    pass

# 9.3.1.145 NB-IoT UE Priority
class IENB_IoTUEPriority(IEBase):
    name="NB-IoT UE Priority"
    fields_desc = []
    pass

# 9.3.1.146 NR V2X Services Authorized
class IENRV2XServicesAuthorized(IEBase):
    name="NR V2X Services Authorized"
    fields_desc = []
    pass

# 9.3.1.147 LTE V2X Services Authorized
class IELTEV2XServicesAuthorized(IEBase):
    name="LTE V2X Services Authorized"
    fields_desc = []
    pass

# 9.3.1.148 NR UE Sidelink Aggregate Maximum Bit Rate
class IENRUESidelinkAggregateMaximumBitRate(IEBase):
    name="NR UE Sidelink Aggregate Maximum Bit Rate"
    fields_desc = []
    pass

# 9.3.1.149 LTE UE Sidelink Aggregate Maximum Bit Rate
class IELTEUESidelinkAggregateMaximumBitRate(IEBase):
    name="LTE UE Sidelink Aggregate Maximum Bit Rate"
    fields_desc = []
    pass

# 9.3.1.150 PC5 QoS Parameters
class IEPC5QoSParameters(IEBase):
    name="PC5 QoS Parameters"
    fields_desc = []
    pass

# 9.3.1.151 Alternative QoS Parameters Set List
class IEAlternativeQoSParametersSetList(IEBase):
    name="ALternative QoS Parameters Set List"
    fields_desc = []
    pass

# 9.3.1.152 Alternative QoS Parameters Set Index
class IEAlternativeQoSParametersSetIndex(IEBase):
    name="Alternative QoS Parameters Set Index"
    fields_desc = []
    pass

# 9.3.1.153 Alternative QoS Parameters Set Notify Index
class IEAlternativeQoSParametersSetNotifyIndex(IEBase):
    name="Alternative QoS Parameters Set Notify Index"
    fields_desc = []
    pass

# 9.3.1.154 Paging eDRX Information
class IEPagingeDRXInformation(IEBase):
    name="Paging eDRX Information"
    fields_desc = []
    pass

# 9.3.1.155 CE-mode-B Restricted
class IECE_mode_BRestricted(IEBase):
    name="CE-mode-B Restricted"
    fields_desc = []
    pass

# 9.3.1.156 CE-mode-B Support Indicator
class IECE_mode_BSupportIndicator(IEBase):
    name="CE-mode-B Support Indicator"
    fields_desc = []
    pass

# 9.3.1.157 LTE-M Indication
class IELTE_MIndication(IEBase):
    name="LTE-M Indication"
    fields_desc = []
    pass

# 9.3.1.158 Suspend Request Indication
class IESuspendRequestIndication(IEBase):
    name="Suspend Request Indication"
    fields_desc = []
    pass

# 9.3.1.159 Suspend Response Indication
class IESuspendResponseIndication(IEBase):
    name="Suspend Response Indication"
    fields_desc = []
    pass

# 9.3.1.160 UE User Plane CIoT Support Indicator
class IEUEUserPlaneCIoTSupportIndicator(IEBase):
    name="UE User Plane CIoT Support Indicator"
    fields_desc = []
    pass

# 9.3.1.161 Global TNGF ID
class IEGlobalTNGFID(IEBase):
    name="Global TNGF ID"
    fields_desc = []
    pass

# 9.3.1.162 Global W-AGF ID
class IEGlobalW_AGFID(IEBase):
    name="Global W-AGF ID"
    fields_desc = []
    pass

# 9.3.1.163 Global TWIF ID
class IEGlobalTWIFID(IEBase):
    name="Global TWIF ID"
    fields_desc = []
    pass

# 9.3.1.164 W-AGF User Location Information
class IEW_AGFUserLocationInformation(IEBase):
    name="W-AGF User Location Information"
    fields_desc = []
    pass

# 9.3.1.165 Global eNB ID
class IEGlobaleNBID(IEBase):
    name="Global eNB ID"
    fields_desc = []
    pass

# 9.3.1.166 UE History Information from UE
class IEUEHistoryInformationfromUE(IEBase):
    name="UE History Information from UE"
    pass

# 9.3.1.167 MDT Configuration
class IEMDTConfiguration(IEBase):
    name="MDT Configuration"
    fields_desc = []
    pass

# 9.3.1.168 MDT PLMN List
class IEMDTPLMNList(IEBase):
    name="MDT PLMN List"
    fields_desc = []
    pass

# 9.3.1.169 MDT Configuration-NR
class IEMDTConfiguration_NR(IEBase):
    name="MDT Configuration-NR"
    fields_desc = []
    pass

# 9.3.1.170 MDT Configuration-EUTRA
class IEMDTConfiguration_EUTRA(IEBase):
    name="MDT Configuration-EUTRA"
    fields_desc = []
    pass

# 9.3.1.171 M1 Configuration
class IEM1Configuration(IEBase):
    name="M1 Configuration"
    fields_desc = []
    pass

# 9.3.1.172 M4 Configuration
class IEM4Configuration(IEBase):
    name="M4 Configuration"
    fields_desc = []
    pass

# 9.3.1.173 M5 Configuration
class IEM5Configuration(IEBase):
    name="M5 Configuration"
    fields_desc = []
    pass

# 9.3.1.174 M6 Configuration
class IEM6Configuration(IEBase):
    name="M6 Configuration"
    fields_desc = []
    pass

# 9.3.1.175 M7 Configuration
class IEM7Configuration(IEBase):
    name="M7 Configuration"
    fields_desc = []
    pass

# 9.3.1.176 MDT Location Information
class IEMDTLocationInformation(IEBase):
    name="MDT Location Information"
    fields_desc = []
    pass

# 9.3.1.177 Bluetooth Measurement Configuration
class IEBluetoothMeasurementConfiguration(IEBase):
    name="Bluetooth Measurement Configuration"
    fields_desc = []
    pass

# 9.3.1.178 WLAN Measurement Configuration
class IEWLANMeasurementConfiguration(IEBase):
    name="WLAN Measurement Configuration"
    fields_desc = []
    pass

# 9.3.1.179 Sensor Measurement Configuration
class IESensorMeasurementConfiguration(IEBase):
    name="Sensor Measurement Configuration"
    fields_desc = []
    pass

# 9.3.1.180 Event Trigger Logged MDT Configuration
class IEEventTriggerLoggedMDTConfiguration(IEBase):
    name="Event Trigger Logged MDT Configuration"
    fields_desc = []
    pass

# 9.3.1.181 NR Frequency Info
class IENRFrequencyInfo(IEBase):
    name="NR Frequency Info"
    fields_desc = []
    pass

# 9.3.1.182 Area Scope of Neighbour Cells
class IEAreaScopeofNeighbourCells(IEBase):
    name="Area Scope of Neighbour Cells"
    pass
    
# 9.3.1.183 NPN Paging Assistance Information
class IENPNPagingAssistanceInformation(IEBase):
    name="NPN Paging Assistnace Information"
    fields_desc = []
    pass

# 9.3.1.184 NPN Mobility Information
class IENPNMobilityInformation(IEBase):
    name="NPN Mobility Information"
    fields_desc = []
    pass

# 9.3.1.185 Cell CAG Information
class IECellCAGInformation(IEBase):
    name="Cell CAG Information"
    fields_desc = []
    pass

# 9.3.1.186 Target to Source Failure Transparent Container
class IETargettoSourceFailureTransparentContainer(IEBase):
    name="Target to Source Failure Transparent Container"
    fields_desc = []
    pass

# 9.3.1.187 Target NG-RAN Node to Source NG-RAN Node Failure Transparent Container
class IETargetNG_RANNodetoSourceNG_RANNodeFailureTransparentContainer(IEBase):
    name="Target NG-RAN Node to Source NG-RAN Node Failure Transparent Container"
    pass

# 9.3.1.188 DAPS Request Information
class IEDAPSRequestInformation(IEBase):
    name="DAPS Request Information"
    fields_desc = []
    pass

# 9.3.1.189 DAPS Response Information
class IEDAPSResponseInformation(IEBase):
    name="DAPS Response Information"
    fields_desc = []
    pass

# 9.3.1.190 Early Status Transfer Transparent Container
class IEEarlyStatusTransferTransparentContainer(IEBase):
    name="Early Status Transfer Transparent Container"
    fields_desc = []
    pass

# 9.3.1.191 Extended Slice Support List
class IEExtendedSliceSupportList(IEBase):
    name="Extended Slice Support List"
    fields_desc = []
    pass

# 9.3.1.192 UE Capability Info Request
class IEUECapabilityInfoRequest(IEBase):
    name="UE Capability Info Request"
    fields_desc = []
    pass

# 9.3.1.193 Extended RAN Node Name
class IEExtendedRANNodeName(IEBase):
    name="Extended RAN Node Name"
    fields_desc = []
    pass

# 9.3.1.194 MICO All PLMN
class IEMICOAllPLMN(IEBase):
    name="MICO All PLMN"
    fields_desc = []
    pass

# ----------------------------------------------------------------------------------------------------------
# 9.3.2 Transport Network Layer Related IEs
# 9.3.2.1 QoS Flow per TNL Information List
class IEQoSFlowperTNLInformationList(IEBase):
    name="QoS Flow per TNL Information List"
    fields_desc = []
    pass

# 9.3.2.2 UP Transport Layer Information
class IEUPTransportLayerInformation(IEBase):
    name="UP Transport Layer Information"
    fields_desc = []
    pass

# 9.3.2.3 E-RAB ID
class IEE_RABID(IEBase):
    name="E-RAB ID"
    fields_desc = []
    pass

# 9.3.2.4 Transport Layer Address
class IETransportLayerAddress(IEBase):
    name="Transport Layer Address"
    fields_desc = []
    pass

# 9.3.2.5 GTP-TEID
class IEGTP_TEID(IEBase):
    name="GTP-TEID"
    fields_desc = []
    pass

# 9.3.2.6 CP Transport Layer Information
class IECPTransportLayerInformation(IEBase):
    name="CP Transport Layer Information"
    fields_desc = []
    pass

# 9.3.2.7 TNL Association List
class IETNLAssociationList(IEBase):
    name="TNL Association List"
    fields_desc = []
    pass

# 9.3.2.8 QoS Flow per TNL Information
class IEQoSFlowperTNLInformation(IEBase):
    name="QoS Flow per TNL Information"
    fields_desc = []
    pass

# 9.3.2.9 TNL Association Usage
class IETNLAssociationUsage(IEBase):
    name="TNL Association Usage"
    fields_desc = []
    pass

# 9.3.2.10 TNL Address Weight Factor
class IETNLAddressWeightFactor(IEBase):
    name="TNL Address Weight Factor"
    fields_desc = []
    pass

# 9.3.2.11 UP Transport Layer Information Pair List
class IEUPTransportLayerInformationPairList(IEBase):
    name="UP Transport Layer Information Pair List"
    pass

# 9.3.2.12 UP Transport Layer Information List
class IEUPTransportLayerInformationList(IEBase):
    name="UP Transport Layer Information List"
    fields_desc = []
    pass

# 9.3.2.13 QoS Flow List with Data Forwarding
class IEQoSFlowListwithDataForwarding(IEBase):
    name="QoS Flow List with Data Forwarding"
    fields_desc = []
    pass

# 9.3.2.14 URI
class IEURI(IEBase):
    name="URI"
    fields_desc = []
    pass


# ----------------------------------------------------------------------------------------------------------
# 9.3.3 NAS Related IEs
# 9.3.3.1 AMF UE NGAP ID
class IEAMFUENGAPID(IEBase):
    name="AMF UE NGAP ID"
    fields_desc = []
    pass

# 9.3.3.2 RAN UE NGAP ID
class IERANUENGAPID(IEBase):
    name="RAN UE NGAP ID"
    fields_desc = []
    pass

# 9.3.3.3 GUAMI
class IEGUAMI(IEBase):
    name="GUAMI"
    fields_desc = []
    pass

# 9.3.3.4 NAS-PDU
class IENAS_PDU(IEBase):
    name="NAS-PDU"
    fields_desc = []
    pass

# 9.3.3.5 PLMN Identity
class IEPLMNIdentity(IEBase):
    name="PLMN Identity"
    fields_desc = []
    pass

# 9.3.3.6 SON Configuration Transfer
class IESONConfigurationTransfer(IEBase):
    name="SON Configuration Transfer"
    fields_desc = []
    pass

# 9.3.3.7 SON Information
class IESONInformation(IEBase):
    name="SON Information"
    fields_desc = []
    pass

# 9.3.3.8 SON Information Reply
class IESONInformationReply(IEBase):
    name="SON Information Reply"
    fields_desc = []
    pass

# 9.3.3.9 Xn TNL Configuration Info
class IEXnTNLConfigurationInfo(IEBase):
    name="Xn TNL Configuration Info"
    fields_desc = []
    pass

# 9.3.3.10 TAC
class IETAC(IEBase):
    name="TAC"
    fields_desc = []
    pass

# 9.3.3.11 TAI
class IETAI(IEBase):
    name="TAI"
    fields_desc = []
    pass

# 9.3.3.12 AMF Set ID
class IEAMFSetID(IEBase):
    name="AMF Set ID"
    fields_desc = []
    pass

# 9.3.3.13 Routing ID
class IERoutingID(IEBase):
    name="Routing ID"
    fields_desc = []
    pass

# 9.3.3.14 NRPPa-PDU
class IENRPPa_PDU(IEBase):
    name="NRPPa-PDU"
    fields_desc = []
    pass

# 9.3.3.15 RAN Paging Priority
class IERANPagingPriority(IEBase):
    name="RAN Paging Priority"
    fields_desc = []
    pass

# 9.3.3.16 EPS TAC
class IEEPSTAC(IEBase):
    name="EPS TAC"
    fields_desc = []
    pass

# 9.3.3.17 EPS TAI
class IEEPSTAI(IEBase):
    name="EPS TAI"
    fields_desc = []
    pass

# 9.3.3.18 UE Paging Identity
class IEUEPagingIdentity(IEBase):
    name="UE Paging Identity"
    fields_desc = []
    pass

# 9.3.3.19 AMF Pointer
class IEAMFPointer(IEBase):
    name="AMF Pointer"
    fields_desc = []
    pass

# 9.3.3.20 5G-S-TMSI
class IE5G_S_TMSI(IEBase):
    name="5G-S-TMSI"
    fields_desc = []
    pass

# 9.3.3.21 AMF Name
class IEAMFName(IEBase):
    name="AMF Name"
    fields_desc = []
    pass

# 9.3.3.22 Paging Origin
class IEPagingOrigin(IEBase):
    name="Paging Origin"
    fields_desc = []
    pass

# 9.3.3.23 UE Identity Index Value
class IEUEIdentityIndexValue(IEBase):
    name="UE Identity Index Value"
    fields_desc = []
    pass

# 9.3.3.24 Periodic Registration Update Timer
class IEPeriodicRegistrationUpdateTimer(IEBase):
    name="Periodic Registration Update Timer"
    fields_desc = []
    pass

# 9.3.3.25 UE-associated Logical NG-connection List
class IEUE_associatedLogicalNG_connectionList(IEBase):
    name="UE-associated Logical NG-connection List"
    fields_desc = []
    pass

# 9.3.3.26 NAS Security Parameters from NG-RAN
class IENASSecurityParametersfromNG_RAN(IEBase):
    name="NAS Security Parameters from NG-RAN"
    fields_desc = []
    pass

# 9.3.3.27 Source to Target AMF Information Reroute
class IESourcetoTargetAMFInformationReroute(IEBase):
    name="Source to target AMF Information Reroute"
    fields_desc = []
    pass

# 9.3.3.28 RIM Information Transfer
class IERIMInformationTransfer(IEBase):
    name="RIM Information Transfer"
    fields_desc = []
    pass

# 9.3.3.29 RIM Information
class IERIMInformation(IEBase):
    name="RIM Information"
    fields_desc = []
    pass

# 9.3.3.30 LAI
class IELAI(IEBase):
    name="LAI"
    fields_desc = []
    pass

# 9.3.3.31 Extended Connected Time
class IEExtendedConnectedTime(IEBase):
    name="Extended Connected Time"
    fields_desc = []
    pass

# 9.3.3.32 End Indication
class IEEndIndication(IEBase):
    name="End Indication"
    fields_desc = []
    pass

# 9.3.3.33 Inter-system SON Configuration Transfer
class IEInter_systemSONConfigurationTransfer(IEBase):
    name="Inter-system SON Configuration Transfer"
    fields_desc = []
    pass

# 9.3.3.34 Inter-system SON Information
class IEInter_systemSONInformation(IEBase):
    name="Inter-system SON Information"
    fields_desc = []
    pass

# 9.3.3.35 SON Information Report
class IESONInformationReport(IEBase):
    name="SON Information Report"
    fields_desc = []
    pass

# 9.3.3.36 Inter-system SON Information Report
class IEInter_systemSONInformationReport(IEBase):
    name="Inter-system SON Information Report"
    fields_desc = []
    pass

# 9.3.3.37 Failure Indication
class IEFailureIndication(IEBase):
    name="Failure Indication"
    fields_desc = []
    pass

# 9.3.3.38 Inter-system Failure Indication
class IEIntersystemFailureIndication(IEBase):
    name="Inter-system Failure Indication"
    fields_desc = []
    pass

# 9.3.3.39 HO Report
class IEHOReport(IEBase):
    name="HO Report"
    fields_desc = []
    pass

# 9.3.3.40 Inter-system HO Report
class IEInter_systemHOReport(IEBase):
    name="Inter-system HO Report"
    pass

# 9.3.3.41 UE RLF Report Container
class IEUERLFReportContainer(IEBase):
    name="UE RLF Report Container"
    fields_desc = []
    pass

# 9.3.3.42 NID
class IENID(IEBase):
    name="NID"
    fields_desc = []
    pass

# 9.3.3.43 CAG ID
class IECAGID(IEBase):
    name="CAG ID"
    fields_desc = []
    pass

# 9.3.3.44 NPN Support
class IENPNSupport(IEBase):
    name="NPN Support"
    fields_desc = []
    pass

# 9.3.3.45 Allowed PNI-NPN List
class IEAllowedPNI_NPNList(IEBase):
    name="Allowed PNI-NPN List"
    fields_desc = []
    pass

# 9.3.3.46 NPN Access Information
class IENPNAccessInformation(IEBase):
    name="NPN Access Information"
    fields_desc = []
    pass

# 9.3.3.47 Cell CAG List
class IECellCAGList(IEBase):
    name="Cell CAG List"
    fields_desc = []
    pass

# 9.3.3.48 UL CP Security Information
class IEULCPSecurityInformation(IEBase):
    name="UL CP Security Information"
    fields_desc = []
    pass

# 9.3.3.49 DL CP Security Information
class IEDLCPSecurityInformation(IEBase):
    name="DL CP Security Information"
    fields_desc = []
    pass

# 9.3.3.50 Configured TAC Indication
class IEConfiguredTACIndication(IEBase):
    name="Configured TAC Indication"
    fields_desc = []
    pass

# 9.3.3.51 Extended AMF Name
class IEExtendedAMFName(IEBase):
    name="Extended AMF Name"
    fields_desc = []
    pass

# 9.3.3.52 Extended UE Identity Index Value
class IEExtendedUEIdentityIndexValue(IEBase):
    name="Extended UE Identity Index Value"
    fields_desc = []
    pass


# ----------------------------------------------------------------------------------------------------------
# 9.3.4 SMF Related IEs

# 9.3.4.1 PDU Session Resource Setup Request Transfer
class IEPDUSessionResourceSetupRequestTransfer(IEBase):
    name="PDU Session Resource Setup Request Transfer"
    fields_desc = []
    pass

# 9.3.4.2 PDU Session Resource Setup Response Transfer
class IEPDUSessionResourceSetupResponseTransfer(IEBase):
    name="PDU Session Resource Setup Response Transfer"
    fields_desc = []
    pass

# 9.3.4.3 PDU Session Resource Modify Request Transfer
class IEPDUSessionResourceModifyRequestTransfer(IEBase):
    name="PDU Session Resource Modify Request Transfer"
    fields_desc = []
    pass

# 9.3.4.4 PDU Session Resource Modify Response Transfer
class IEPDUSessionResourceModifyResponseTransfer(IEBase):
    name="PDU Session Reource Modify Response Transfer"
    fields_desc = []
    pass

# 9.3.4.5 PDU Session Resource Notify Transfer
class IEPDUSessionResourceNotifyTransfer(IEBase):
    name="PDU Session Resource Notify Transfer"
    fields_desc = []
    pass

# 9.3.4.6 PDU Session Resource Modify Indication Transfer
class IEPDUSessionResourceModifyIndicationTransfer(IEBase):
    name="PDU Session Resource Modify Indication Transfer"
    fields_desc = []
    pass

# 9.3.4.7 PDU Session Resource Modify Confirm Transfer
class IEPDUSessionResourceModifyConfirmTransfer(IEBase):
    name="PDU Session Resource Modify Confirm Transfer"
    fields_desc = []
    pass

# 9.3.4.8 Path Switch Request Transfer
class IEPathSwitchRequestTransfer(IEBase):
    name="Path Switch Request Transfer"
    fields_desc = []
    pass

# 9.3.4.9 Path Switch Request Acknowledge Transfer
class IEPathSwitchRequestAcknowledgeTransfer(IEBase):
    name="Path Switch Request Acknowledge Transfer"
    fields_desc = []
    pass

# 9.3.4.10 Handover Command Transfer
class IEHandoverCommandTransfer(IEBase):
    name="Handover Command Transfer"
    fields_desc = []
    pass

# 9.3.4.11 Handover Request Acknowledge Transfer
class IEHandoverRequestAcknowledgeTransfer(IEBase):
    name="Handover Request Acknowledge Transfer"
    fields_desc = []
    pass

# 9.3.4.12 PDU Session Resource Release Command Transfer
class IEPDUSessionResourceReleaseCommandTransfer(IEBase):
    name="PDU Session Resource Release Command Transfer"
    fields_desc = []
    pass

# 9.3.4.13 PDU Session Resource Notify Released Transfer
class IEPDUSessionResourceNotifyReleasedTransfer(IEBase):
    name="PDU Session Resource Notify Released Transfer"
    fields_desc = []
    pass

# 9.3.4.14 Handover Required Transfer
class IEHandoverRequiredTransfer(IEBase):
    name="Handover Required Transfer"
    fields_desc = []
    pass

# 9.3.4.15 Path Switch Request Setup Failed Transfer
class IEPathSwitchRequestSetupFailedTransfer(IEBase):
    name="Path Switch Request Setup Failed Transfer"
    fields_desc = []
    pass

# 9.3.4.16 PDU Session Resource Setup Unsuccessful Transfer
class IEPDUSessionResourceSetupUnsuccessfulTransfer(IEBase):
    name="PDU Session Resource Setup Unsuccessful Transfer"
    fields_desc = []
    pass

# 9.3.4.17 PDU Session Resource Modify Unsuccessful Transfer
class IEPDUSessionResourceModifyUnsuccessfulTransfer(IEBase):
    name="PDU Session Resource Modify Unsuccessful Transfer"
    fields_desc = []
    pass

# 9.3.4.18 Handover Preparation Unsuccessful Transfer
class IEHandoverPreparationUnsuccessfulTransfer(IEBase):
    name="Handover Preparation unsuccessful Transfer"
    fields_desc = []
    pass

# 9.3.4.19 Handover Resource Allocation Unsuccessful Transfer
class IEHandoverResourceAllocationUnsuccessfulTransfer(IEBase):
    name="Handover Resource Allocation Unsuccessful Transfer"
    fields_desc = []
    pass

# 9.3.4.20 Path Switch Request Unsuccessful Transfer
class IEPathSwitchRequestUnsuccessfulTransfer(IEBase):
    name="Path Switch Request Unsuccessful Transfer"
    fields_desc = []
    pass

# 9.3.4.21 PDU Session Resource Release Response Transfer
class IEPDUSessionResourceReleaseResponseTransfer(IEBase):
    name="PDU Session Resource Release Response Transfer"
    fields_desc = []
    pass

# 9.3.4.22 PDU Session Resource Modify Indication Unsuccessful Transfer
class IEPDUSessionResourceModifyIndicationUnsuccessfulTransfer(IEBase):
    name="PDU Session Resource Modify Indication Unsuccessful Transfer"
    fields_desc = []
    pass

# 9.3.4.23 Secondary RAT Data Usage Report Transfer
class IESecondaryRATDataUsageReportTransfer(IEBase):
    name="Secondary RAT Data Usage Report Transfer"
    fields_desc = []
    pass

# 9.3.4.24 UE Context Resume Request Transfer
class IEUEContextResumeRequestTransfer(IEBase):
    name="UE Context Resume Request Transfer"
    fields_desc = []
    pass

# 9.3.4.25 UE Context Resume Response Transfer
class IEUEContextResumeResponseTransfer(IEBase):
    name="UE Context Resume Response Transfer"
    fields_desc = []
    pass

# 9.3.4.26 UE Context Suspend Request Transfer
class IEUEContextSuspendRequestTransfer(IEBase):
    name="UE Context Suspend Request Transfer"
    pass


