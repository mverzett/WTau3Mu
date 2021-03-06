import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

json = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'


DoubleMuonLowMass_Run2016B_23Sep2016     = kreator.makeDataComponent("DoubleMuonLowMass_Run2016B_23Sep2016"    , "/DoubleMuonLowMass/Run2016B-23Sep2016-v3/MINIAOD" , "CMS", ".*root", json)
DoubleMuonLowMass_Run2016C_23Sep2016     = kreator.makeDataComponent("DoubleMuonLowMass_Run2016C_23Sep2016"    , "/DoubleMuonLowMass/Run2016C-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json)
DoubleMuonLowMass_Run2016D_23Sep2016     = kreator.makeDataComponent("DoubleMuonLowMass_Run2016D_23Sep2016"    , "/DoubleMuonLowMass/Run2016D-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json)
DoubleMuonLowMass_Run2016E_23Sep2016     = kreator.makeDataComponent("DoubleMuonLowMass_Run2016E_23Sep2016"    , "/DoubleMuonLowMass/Run2016E-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json)
DoubleMuonLowMass_Run2016F_23Sep2016     = kreator.makeDataComponent("DoubleMuonLowMass_Run2016F_23Sep2016"    , "/DoubleMuonLowMass/Run2016F-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json)
DoubleMuonLowMass_Run2016G_23Sep2016     = kreator.makeDataComponent("DoubleMuonLowMass_Run2016G_23Sep2016"    , "/DoubleMuonLowMass/Run2016G-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json)

DoubleMuonLowMass_Run2016H_PromptReco_v1 = kreator.makeDataComponent("DoubleMuonLowMass_Run2016H_PromptReco_v1", "/DoubleMuonLowMass/Run2016H-PromptReco-v1/MINIAOD", "CMS", ".*root", json)
DoubleMuonLowMass_Run2016H_PromptReco_v2 = kreator.makeDataComponent("DoubleMuonLowMass_Run2016H_PromptReco_v2", "/DoubleMuonLowMass/Run2016H-PromptReco-v2/MINIAOD", "CMS", ".*root", json)
DoubleMuonLowMass_Run2016H_PromptReco_v3 = kreator.makeDataComponent("DoubleMuonLowMass_Run2016H_PromptReco_v3", "/DoubleMuonLowMass/Run2016H-PromptReco-v3/MINIAOD", "CMS", ".*root", json)

datasamplesDoubleMuLowMass = [
    DoubleMuonLowMass_Run2016B_23Sep2016    ,
    DoubleMuonLowMass_Run2016C_23Sep2016    ,
    DoubleMuonLowMass_Run2016D_23Sep2016    ,
    DoubleMuonLowMass_Run2016E_23Sep2016    ,
    DoubleMuonLowMass_Run2016F_23Sep2016    ,
    DoubleMuonLowMass_Run2016G_23Sep2016    ,
    DoubleMuonLowMass_Run2016H_PromptReco_v1,
    DoubleMuonLowMass_Run2016H_PromptReco_v2,
    DoubleMuonLowMass_Run2016H_PromptReco_v3,
]
