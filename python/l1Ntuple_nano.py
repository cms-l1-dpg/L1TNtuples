# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: l1Ntuple -s RAW2DIGI --era=Run2_2016 --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulFromRAW --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleRAWEMU --conditions=80X_dataRun2_Prompt_v8 -n 100 --data --no_exec --no_output --filein=/store/data/Run2016B/ZeroBias/RAW/v2/000/273/425/00000/D4A39245-0D1A-E611-9371-02163E014336.root
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
import FWCore.Utilities.FileUtils as FileUtils
import os,sys

#input files
pathname=sys.argv[2]
filename=sys.argv[3]
shortfilename=os.path.splitext(filename)[0]


from Configuration.StandardSequences.Eras import eras

process = cms.Process('RAW2DIGI',eras.Run2_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

#number of Events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

#input file
process.source = cms.Source("NewEventStreamFileReader",
    fileNames = cms.untracked.vstring(pathname+filename),
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('l1Ntuple nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

# emulate
process.simGtStage2Digis = cms.EDProducer("L1TGlobalProducer",
    ProduceL1GtDaqRecord = cms.bool(True),
    ProduceL1GtObjectMapRecord = cms.bool(True),
    ExtInputTag = cms.InputTag("hltGtStage2Digis"),
    MuonInputTag = cms.InputTag("hltGtStage2Digis", "Muon"),
    EtSumInputTag = cms.InputTag("hltGtStage2Digis", "EtSum"),
    EGammaInputTag = cms.InputTag("hltGtStage2Digis", "EGamma"),
    TauInputTag = cms.InputTag("hltGtStage2Digis", "Tau"),
    JetInputTag = cms.InputTag("hltGtStage2Digis", "Jet"),
)
process.SimL1TGlobal = cms.Sequence(process.simGtStage2Digis)
process.ugtEmu_step = cms.Path(process.SimL1TGlobal)

# Next we load ES producers for any conditions that are not yet in GT,
# using the Era configuration.
process.load('L1Trigger.L1TGlobal.hackConditions_cff')
#process.L1TGlobalPrescalesVetos.PrescaleXMLFile = cms.string('prescale.xml')
#process.L1TGlobalPrescalesVetos.FinOrMaskXMLFile = cms.string('masks.xml')
process.simGtStage2Digis.AlgorithmTriggersUnmasked = cms.bool(True)
process.simGtStage2Digis.AlgorithmTriggersUnprescaled = cms.bool(True)
process.load('L1Trigger.L1TGlobal.TriggerMenu_cff')
process.TriggerMenu.L1TriggerMenuFile = cms.string('UGT_L1_MENU_ugt_l1_l1menu_collisions2017_dev_r5_v3_CONF.xml')


# Load prescales/masks from GT
# comment out the line "from L1Trigger.L1TGlobal.PrescalesVetos_cff import *" in hackConditions_cff"
from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup
process.l1conddb = cms.ESSource("PoolDBESSource",
    CondDBSetup,
    #connect = cms.string('sqlite:./o2o/l1config.db'),
    connect = cms.string("frontier://FrontierPrep/CMS_CONDITIONS"),
    toGet   = cms.VPSet(
    cms.PSet(
        record = cms.string('L1TGlobalPrescalesVetosRcd'),
        tag = cms.string("L1TGlobalPrescalesVetos_Stage2v0_hlt")
        )
    )
)

# Schedule definition
process.endjob_step = cms.EndPath(process.endOfProcess)
process.schedule = cms.Schedule(process.ugtEmu_step, process.endjob_step)

# customisation of the process.
# Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleRAWEMU 

#call to customisation function L1NtupleRAWEMU imported from L1Trigger.L1TNtuples.customiseL1Ntuple
process = L1NtupleRAWEMU(process)

# remove modules not needed
for module in (process.l1CaloTowerTree, process.l1UpgradeTfMuonTree, process.l1HOTree):
  process.L1NtupleRAW.remove(module)
process.l1uGTTree.ugtToken = cms.InputTag("hltGtStage2Digis")

for module in (process.l1EventTree, process.l1UpgradeTfMuonEmuTree, process.l1CaloTowerEmuTree, process.l1UpgradeEmuTree):
  process.L1NtupleEMU.remove(module)
process.l1uGTEmuTree.ugtToken = cms.InputTag("simGtStage2Digis")

process.l1UpgradeTree.egToken = cms.untracked.InputTag("hltGtStage2Digis","EGamma")
process.l1UpgradeTree.tauTokens = cms.untracked.VInputTag(cms.InputTag("hltGtStage2Digis","Tau"))
process.l1UpgradeTree.jetToken = cms.untracked.InputTag("hltGtStage2Digis","Jet")
process.l1UpgradeTree.muonToken = cms.untracked.InputTag("hltGtStage2Digis","Muon")
process.l1UpgradeTree.sumToken = cms.untracked.InputTag("hltGtStage2Digis","EtSum")

process.TFileService.fileName = cms.string('L1Ntuple_'+shortfilename+'.root')
# End of customisation functions
