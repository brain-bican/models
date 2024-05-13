from __future__ import annotations 
from datetime import (
    datetime,
    date
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION 
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        field_validator
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
    )

metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass


class AmplifiedCdnaRnaAmplificationPassFail(str, Enum):
    # The RNA amplification passed the QA/QC
    Pass = "Pass"
    # The RNA amplification failed the QA/QC
    Fail = "Fail"
    # The RNA amplification low passed the QA/QC
    Low_QC = "Low QC"
    # Library Prep not evaluated for QA/QC
    Not_evaluated = "Not evaluated"


class BarcodedCellSampleTechnique(str, Enum):
    # Multiome
    Multiome = "Multiome"
    # ATACOnly
    ATACOnly = "ATACOnly"
    # GEXOnly
    GEXOnly = "GEXOnly"
    # snm3C-seq
    snm3C_seq = "snm3C-seq"


class DissociatedCellSampleCellPrepType(str, Enum):
    # isolated nuclei
    Nuclei = "Nuclei"
    # isolated whole cells
    Cells = "Cells"


class DissociatedCellSampleCellLabelBarcode(str, Enum):
    # 10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    CMO301 = "CMO301"
    # 10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    CMO302 = "CMO302"
    # 10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    CMO303 = "CMO303"
    # 10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    CMO304 = "CMO304"
    # 10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    CMO305 = "CMO305"
    # 10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    CMO306 = "CMO306"
    # 10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    CMO307 = "CMO307"
    # 10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    CMO308 = "CMO308"
    # 10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    CMO309 = "CMO309"
    # 10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    CMO310 = "CMO310"
    # 10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    CMO311 = "CMO311"
    # 10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    CMO312 = "CMO312"
    # Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    number_2nt_001 = "2nt-001"
    # Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    number_2nt_002 = "2nt-002"
    # Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    number_2nt_003 = "2nt-003"
    # Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    number_2nt_004 = "2nt-004"
    # Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    number_3nt_001 = "3nt-001"
    # Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    number_3nt_002 = "3nt-002"
    # Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    number_3nt_003 = "3nt-003"
    # Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    number_3nt_004 = "3nt-004"
    # Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    number_3nt_005 = "3nt-005"
    # Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    number_3nt_006 = "3nt-006"


class LibraryTechnique(str, Enum):
    # SMARTSeqSC
    SMARTSeqSC = "SMARTSeqSC"
    # SmartSeq3
    SmartSeq3 = "SmartSeq3"
    # 10xV3.1
    number_10xV3FULL_STOP1 = "10xV3.1"
    # 10xV3.1_HT
    number_10xV3FULL_STOP1_HT = "10xV3.1_HT"
    # 10xMultiome;GEX
    number_10xMultiomeSEMICOLONGEX = "10xMultiome;GEX"
    # 10xMultiome;ATAC
    number_10xMultiomeSEMICOLONATAC = "10xMultiome;ATAC"
    # 10xATAC_V2.0
    number_10xATAC_V2FULL_STOP0 = "10xATAC_V2.0"
    # 10XMultiome-CellHashing;GEX
    number_10XMultiome_CellHashingSEMICOLONGEX = "10XMultiome-CellHashing;GEX"
    # 10XMultiome-CellHashing;ATAC
    number_10XMultiome_CellHashingSEMICOLONATAC = "10XMultiome-CellHashing;ATAC"
    # 10XMultiome-Cell Hashing;Barcode
    number_10XMultiome_Cell_HashingSEMICOLONBarcode = "10XMultiome-Cell Hashing;Barcode"
    # 10xV3.1_CellPlex;GEX
    number_10xV3FULL_STOP1_CellPlexSEMICOLONGEX = "10xV3.1_CellPlex;GEX"
    # 10xV3.1_CellPlex;Barcode
    number_10xV3FULL_STOP1_CellPlexSEMICOLONBarcode = "10xV3.1_CellPlex;Barcode"
    # 10xV3.1_HT_CellPlex;GEX
    number_10xV3FULL_STOP1_HT_CellPlexSEMICOLONGEX = "10xV3.1_HT_CellPlex;GEX"
    # 10xV3.1_HT_CellPlex;Barcode
    number_10xV3FULL_STOP1_HT_CellPlexSEMICOLONBarcode = "10xV3.1_HT_CellPlex;Barcode"
    # MethylC-Seq
    MethylC_Seq = "MethylC-Seq"
    # snm3C-seq
    snm3C_seq = "snm3C-seq"
    # snmCT-seq
    snmCT_seq = "snmCT-seq"
    # scATAC-seq
    scATAC_seq = "scATAC-seq"
    # MERFISH
    MERFISH = "MERFISH"
    # Slide-seq MERFISH
    Slide_seq_MERFISH = "Slide-seq MERFISH"
    # whole brain MERFISH
    whole_brain_MERFISH = "whole brain MERFISH"
    # DBiT RNA-seq
    DBiT_RNA_seq = "DBiT RNA-seq"
    # DBiT ATAC-seq
    DBiT_ATAC_seq = "DBiT ATAC-seq"


class LibraryPrepPassFail(str, Enum):
    # Library Prep passed the QA/QC
    Pass = "Pass"
    # Library Prep failed the QA/QC
    Fail = "Fail"
    # Library Prep low passed the QA/QC
    Low_QC = "Low QC"
    # Library Prep not evaluated for QA/QC
    Not_evaluated = "Not evaluated"


class LibraryR1R2Index(str, Enum):
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_A1 = "SI-TT-A1"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_A2 = "SI-TT-A2"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_A3 = "SI-TT-A3"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_A4 = "SI-TT-A4"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_A5 = "SI-TT-A5"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_A6 = "SI-TT-A6"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_A7 = "SI-TT-A7"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_A8 = "SI-TT-A8"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_A9 = "SI-TT-A9"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_A10 = "SI-TT-A10"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_A11 = "SI-TT-A11"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_A12 = "SI-TT-A12"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_B1 = "SI-TT-B1"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_B2 = "SI-TT-B2"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_B3 = "SI-TT-B3"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_B4 = "SI-TT-B4"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_B5 = "SI-TT-B5"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_B6 = "SI-TT-B6"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_B7 = "SI-TT-B7"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_B8 = "SI-TT-B8"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_B9 = "SI-TT-B9"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_B10 = "SI-TT-B10"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_B11 = "SI-TT-B11"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_B12 = "SI-TT-B12"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_C1 = "SI-TT-C1"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_C2 = "SI-TT-C2"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_C3 = "SI-TT-C3"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_C4 = "SI-TT-C4"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_C5 = "SI-TT-C5"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_C6 = "SI-TT-C6"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_C7 = "SI-TT-C7"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_C8 = "SI-TT-C8"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_C9 = "SI-TT-C9"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_C10 = "SI-TT-C10"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_C11 = "SI-TT-C11"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_C12 = "SI-TT-C12"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_D1 = "SI-TT-D1"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_D2 = "SI-TT-D2"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_D3 = "SI-TT-D3"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_D4 = "SI-TT-D4"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_D5 = "SI-TT-D5"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_D6 = "SI-TT-D6"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_D7 = "SI-TT-D7"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_D8 = "SI-TT-D8"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_D9 = "SI-TT-D9"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_D10 = "SI-TT-D10"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_D11 = "SI-TT-D11"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_D12 = "SI-TT-D12"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_E1 = "SI-TT-E1"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_E2 = "SI-TT-E2"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_E3 = "SI-TT-E3"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_E4 = "SI-TT-E4"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_E5 = "SI-TT-E5"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_E6 = "SI-TT-E6"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_E7 = "SI-TT-E7"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_E8 = "SI-TT-E8"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_E9 = "SI-TT-E9"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_E10 = "SI-TT-E10"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_E11 = "SI-TT-E11"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_E12 = "SI-TT-E12"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_F1 = "SI-TT-F1"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_F2 = "SI-TT-F2"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_F3 = "SI-TT-F3"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_F4 = "SI-TT-F4"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_F5 = "SI-TT-F5"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_F6 = "SI-TT-F6"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_F7 = "SI-TT-F7"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_F8 = "SI-TT-F8"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_F9 = "SI-TT-F9"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_F10 = "SI-TT-F10"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_F11 = "SI-TT-F11"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_F12 = "SI-TT-F12"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_G1 = "SI-TT-G1"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_G2 = "SI-TT-G2"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_G3 = "SI-TT-G3"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_G4 = "SI-TT-G4"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_G5 = "SI-TT-G5"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_G6 = "SI-TT-G6"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_G7 = "SI-TT-G7"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_G8 = "SI-TT-G8"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_G9 = "SI-TT-G9"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_G10 = "SI-TT-G10"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_G11 = "SI-TT-G11"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_G12 = "SI-TT-G12"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_H1 = "SI-TT-H1"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_H2 = "SI-TT-H2"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_H3 = "SI-TT-H3"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_H4 = "SI-TT-H4"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_H5 = "SI-TT-H5"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_H6 = "SI-TT-H6"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_H7 = "SI-TT-H7"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_H8 = "SI-TT-H8"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_H9 = "SI-TT-H9"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_H10 = "SI-TT-H10"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_H11 = "SI-TT-H11"
    # 10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    SI_TT_H12 = "SI-TT-H12"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_A1 = "SI-NN-A1"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_A2 = "SI-NN-A2"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_A3 = "SI-NN-A3"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_A4 = "SI-NN-A4"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_A5 = "SI-NN-A5"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_A6 = "SI-NN-A6"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_A7 = "SI-NN-A7"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_A8 = "SI-NN-A8"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_A9 = "SI-NN-A9"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_A10 = "SI-NN-A10"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_A11 = "SI-NN-A11"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_A12 = "SI-NN-A12"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_B1 = "SI-NN-B1"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_B2 = "SI-NN-B2"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_B3 = "SI-NN-B3"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_B4 = "SI-NN-B4"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_B5 = "SI-NN-B5"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_B6 = "SI-NN-B6"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_B7 = "SI-NN-B7"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_B8 = "SI-NN-B8"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_B9 = "SI-NN-B9"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_B10 = "SI-NN-B10"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_B11 = "SI-NN-B11"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_B12 = "SI-NN-B12"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_C1 = "SI-NN-C1"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_C2 = "SI-NN-C2"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_C3 = "SI-NN-C3"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_C4 = "SI-NN-C4"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_C5 = "SI-NN-C5"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_C6 = "SI-NN-C6"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_C7 = "SI-NN-C7"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_C8 = "SI-NN-C8"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_C9 = "SI-NN-C9"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_C10 = "SI-NN-C10"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_C11 = "SI-NN-C11"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_C12 = "SI-NN-C12"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_D1 = "SI-NN-D1"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_D2 = "SI-NN-D2"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_D3 = "SI-NN-D3"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_D4 = "SI-NN-D4"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_D5 = "SI-NN-D5"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_D6 = "SI-NN-D6"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_D7 = "SI-NN-D7"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_D8 = "SI-NN-D8"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_D9 = "SI-NN-D9"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_D10 = "SI-NN-D10"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_D11 = "SI-NN-D11"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_D12 = "SI-NN-D12"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_E1 = "SI-NN-E1"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_E2 = "SI-NN-E2"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_E3 = "SI-NN-E3"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_E4 = "SI-NN-E4"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_E5 = "SI-NN-E5"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_E6 = "SI-NN-E6"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_E7 = "SI-NN-E7"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_E8 = "SI-NN-E8"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_E9 = "SI-NN-E9"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_E10 = "SI-NN-E10"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_E11 = "SI-NN-E11"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_E12 = "SI-NN-E12"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_F1 = "SI-NN-F1"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_F2 = "SI-NN-F2"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_F3 = "SI-NN-F3"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_F4 = "SI-NN-F4"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_F5 = "SI-NN-F5"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_F6 = "SI-NN-F6"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_F7 = "SI-NN-F7"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_F8 = "SI-NN-F8"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_F9 = "SI-NN-F9"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_F10 = "SI-NN-F10"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_F11 = "SI-NN-F11"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_F12 = "SI-NN-F12"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_G1 = "SI-NN-G1"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_G2 = "SI-NN-G2"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_G3 = "SI-NN-G3"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_G4 = "SI-NN-G4"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_G5 = "SI-NN-G5"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_G6 = "SI-NN-G6"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_G7 = "SI-NN-G7"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_G8 = "SI-NN-G8"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_G9 = "SI-NN-G9"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_G10 = "SI-NN-G10"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_G11 = "SI-NN-G11"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_G12 = "SI-NN-G12"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_H1 = "SI-NN-H1"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_H2 = "SI-NN-H2"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_H3 = "SI-NN-H3"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_H4 = "SI-NN-H4"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_H5 = "SI-NN-H5"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_H6 = "SI-NN-H6"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_H7 = "SI-NN-H7"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_H8 = "SI-NN-H8"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_H9 = "SI-NN-H9"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_H10 = "SI-NN-H10"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_H11 = "SI-NN-H11"
    # 10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    SI_NN_H12 = "SI-NN-H12"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_A1 = "SI-NA-A1"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_B1 = "SI-NA-B1"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_C1 = "SI-NA-C1"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_D1 = "SI-NA-D1"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_E1 = "SI-NA-E1"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_F1 = "SI-NA-F1"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_G1 = "SI-NA-G1"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_H1 = "SI-NA-H1"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_A2 = "SI-NA-A2"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_B2 = "SI-NA-B2"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_C2 = "SI-NA-C2"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_D2 = "SI-NA-D2"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_E2 = "SI-NA-E2"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_F2 = "SI-NA-F2"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_G2 = "SI-NA-G2"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_H2 = "SI-NA-H2"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_A3 = "SI-NA-A3"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_B3 = "SI-NA-B3"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_C3 = "SI-NA-C3"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_D3 = "SI-NA-D3"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_E3 = "SI-NA-E3"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_F3 = "SI-NA-F3"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_G3 = "SI-NA-G3"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_H3 = "SI-NA-H3"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_A4 = "SI-NA-A4"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_B4 = "SI-NA-B4"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_C4 = "SI-NA-C4"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_D4 = "SI-NA-D4"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_E4 = "SI-NA-E4"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_F4 = "SI-NA-F4"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_G4 = "SI-NA-G4"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_H4 = "SI-NA-H4"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_A5 = "SI-NA-A5"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_B5 = "SI-NA-B5"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_C5 = "SI-NA-C5"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_D5 = "SI-NA-D5"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_E5 = "SI-NA-E5"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_F5 = "SI-NA-F5"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_G5 = "SI-NA-G5"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_H5 = "SI-NA-H5"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_A6 = "SI-NA-A6"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_B6 = "SI-NA-B6"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_C6 = "SI-NA-C6"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_D6 = "SI-NA-D6"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_E6 = "SI-NA-E6"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_F6 = "SI-NA-F6"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_G6 = "SI-NA-G6"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_H6 = "SI-NA-H6"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_A7 = "SI-NA-A7"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_B7 = "SI-NA-B7"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_C7 = "SI-NA-C7"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_D7 = "SI-NA-D7"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_E7 = "SI-NA-E7"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_F7 = "SI-NA-F7"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_G7 = "SI-NA-G7"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_H7 = "SI-NA-H7"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_A8 = "SI-NA-A8"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_B8 = "SI-NA-B8"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_C8 = "SI-NA-C8"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_D8 = "SI-NA-D8"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_E8 = "SI-NA-E8"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_F8 = "SI-NA-F8"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_G8 = "SI-NA-G8"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_H8 = "SI-NA-H8"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_A9 = "SI-NA-A9"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_B9 = "SI-NA-B9"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_C9 = "SI-NA-C9"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_D9 = "SI-NA-D9"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_E9 = "SI-NA-E9"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_F9 = "SI-NA-F9"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_G9 = "SI-NA-G9"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_H9 = "SI-NA-H9"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_A10 = "SI-NA-A10"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_B10 = "SI-NA-B10"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_C10 = "SI-NA-C10"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_D10 = "SI-NA-D10"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_E10 = "SI-NA-E10"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_F10 = "SI-NA-F10"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_G10 = "SI-NA-G10"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_H10 = "SI-NA-H10"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_A11 = "SI-NA-A11"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_B11 = "SI-NA-B11"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_C11 = "SI-NA-C11"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_D11 = "SI-NA-D11"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_E11 = "SI-NA-E11"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_F11 = "SI-NA-F11"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_G11 = "SI-NA-G11"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_H11 = "SI-NA-H11"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_A12 = "SI-NA-A12"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_B12 = "SI-NA-B12"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_C12 = "SI-NA-C12"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_D12 = "SI-NA-D12"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_E12 = "SI-NA-E12"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_F12 = "SI-NA-F12"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_G12 = "SI-NA-G12"
    # 10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    SI_NA_H12 = "SI-NA-H12"
    # NeryLab 384_SetB
    SetB_A1 = "SetB-A1"
    # NeryLab 384_SetB
    SetB_A10 = "SetB-A10"
    # NeryLab 384_SetB
    SetB_A11 = "SetB-A11"
    # NeryLab 384_SetB
    SetB_A12 = "SetB-A12"
    # NeryLab 384_SetB
    SetB_A13 = "SetB-A13"
    # NeryLab 384_SetB
    SetB_A14 = "SetB-A14"
    # NeryLab 384_SetB
    SetB_A15 = "SetB-A15"
    # NeryLab 384_SetB
    SetB_A16 = "SetB-A16"
    # NeryLab 384_SetB
    SetB_A17 = "SetB-A17"
    # NeryLab 384_SetB
    SetB_A18 = "SetB-A18"
    # NeryLab 384_SetB
    SetB_A19 = "SetB-A19"
    # NeryLab 384_SetB
    SetB_A2 = "SetB-A2"
    # NeryLab 384_SetB
    SetB_A20 = "SetB-A20"
    # NeryLab 384_SetB
    SetB_A21 = "SetB-A21"
    # NeryLab 384_SetB
    SetB_A22 = "SetB-A22"
    # NeryLab 384_SetB
    SetB_A23 = "SetB-A23"
    # NeryLab 384_SetB
    SetB_A24 = "SetB-A24"
    # NeryLab 384_SetB
    SetB_A3 = "SetB-A3"
    # NeryLab 384_SetB
    SetB_A4 = "SetB-A4"
    # NeryLab 384_SetB
    SetB_A5 = "SetB-A5"
    # NeryLab 384_SetB
    SetB_A6 = "SetB-A6"
    # NeryLab 384_SetB
    SetB_A7 = "SetB-A7"
    # NeryLab 384_SetB
    SetB_A8 = "SetB-A8"
    # NeryLab 384_SetB
    SetB_A9 = "SetB-A9"
    # NeryLab 384_SetB
    SetB_B1 = "SetB-B1"
    # NeryLab 384_SetB
    SetB_B10 = "SetB-B10"
    # NeryLab 384_SetB
    SetB_B11 = "SetB-B11"
    # NeryLab 384_SetB
    SetB_B12 = "SetB-B12"
    # NeryLab 384_SetB
    SetB_B13 = "SetB-B13"
    # NeryLab 384_SetB
    SetB_B14 = "SetB-B14"
    # NeryLab 384_SetB
    SetB_B15 = "SetB-B15"
    # NeryLab 384_SetB
    SetB_B16 = "SetB-B16"
    # NeryLab 384_SetB
    SetB_B17 = "SetB-B17"
    # NeryLab 384_SetB
    SetB_B18 = "SetB-B18"
    # NeryLab 384_SetB
    SetB_B19 = "SetB-B19"
    # NeryLab 384_SetB
    SetB_B2 = "SetB-B2"
    # NeryLab 384_SetB
    SetB_B20 = "SetB-B20"
    # NeryLab 384_SetB
    SetB_B21 = "SetB-B21"
    # NeryLab 384_SetB
    SetB_B22 = "SetB-B22"
    # NeryLab 384_SetB
    SetB_B23 = "SetB-B23"
    # NeryLab 384_SetB
    SetB_B24 = "SetB-B24"
    # NeryLab 384_SetB
    SetB_B3 = "SetB-B3"
    # NeryLab 384_SetB
    SetB_B4 = "SetB-B4"
    # NeryLab 384_SetB
    SetB_B5 = "SetB-B5"
    # NeryLab 384_SetB
    SetB_B6 = "SetB-B6"
    # NeryLab 384_SetB
    SetB_B7 = "SetB-B7"
    # NeryLab 384_SetB
    SetB_B8 = "SetB-B8"
    # NeryLab 384_SetB
    SetB_B9 = "SetB-B9"
    # NeryLab 384_SetB
    SetB_C1 = "SetB-C1"
    # NeryLab 384_SetB
    SetB_C10 = "SetB-C10"
    # NeryLab 384_SetB
    SetB_C11 = "SetB-C11"
    # NeryLab 384_SetB
    SetB_C12 = "SetB-C12"
    # NeryLab 384_SetB
    SetB_C13 = "SetB-C13"
    # NeryLab 384_SetB
    SetB_C14 = "SetB-C14"
    # NeryLab 384_SetB
    SetB_C15 = "SetB-C15"
    # NeryLab 384_SetB
    SetB_C16 = "SetB-C16"
    # NeryLab 384_SetB
    SetB_C17 = "SetB-C17"
    # NeryLab 384_SetB
    SetB_C18 = "SetB-C18"
    # NeryLab 384_SetB
    SetB_C19 = "SetB-C19"
    # NeryLab 384_SetB
    SetB_C2 = "SetB-C2"
    # NeryLab 384_SetB
    SetB_C20 = "SetB-C20"
    # NeryLab 384_SetB
    SetB_C21 = "SetB-C21"
    # NeryLab 384_SetB
    SetB_C22 = "SetB-C22"
    # NeryLab 384_SetB
    SetB_C23 = "SetB-C23"
    # NeryLab 384_SetB
    SetB_C24 = "SetB-C24"
    # NeryLab 384_SetB
    SetB_C3 = "SetB-C3"
    # NeryLab 384_SetB
    SetB_C4 = "SetB-C4"
    # NeryLab 384_SetB
    SetB_C5 = "SetB-C5"
    # NeryLab 384_SetB
    SetB_C6 = "SetB-C6"
    # NeryLab 384_SetB
    SetB_C7 = "SetB-C7"
    # NeryLab 384_SetB
    SetB_C8 = "SetB-C8"
    # NeryLab 384_SetB
    SetB_C9 = "SetB-C9"
    # NeryLab 384_SetB
    SetB_D1 = "SetB-D1"
    # NeryLab 384_SetB
    SetB_D10 = "SetB-D10"
    # NeryLab 384_SetB
    SetB_D11 = "SetB-D11"
    # NeryLab 384_SetB
    SetB_D12 = "SetB-D12"
    # NeryLab 384_SetB
    SetB_D13 = "SetB-D13"
    # NeryLab 384_SetB
    SetB_D14 = "SetB-D14"
    # NeryLab 384_SetB
    SetB_D15 = "SetB-D15"
    # NeryLab 384_SetB
    SetB_D16 = "SetB-D16"
    # NeryLab 384_SetB
    SetB_D17 = "SetB-D17"
    # NeryLab 384_SetB
    SetB_D18 = "SetB-D18"
    # NeryLab 384_SetB
    SetB_D19 = "SetB-D19"
    # NeryLab 384_SetB
    SetB_D2 = "SetB-D2"
    # NeryLab 384_SetB
    SetB_D20 = "SetB-D20"
    # NeryLab 384_SetB
    SetB_D21 = "SetB-D21"
    # NeryLab 384_SetB
    SetB_D22 = "SetB-D22"
    # NeryLab 384_SetB
    SetB_D23 = "SetB-D23"
    # NeryLab 384_SetB
    SetB_D24 = "SetB-D24"
    # NeryLab 384_SetB
    SetB_D3 = "SetB-D3"
    # NeryLab 384_SetB
    SetB_D4 = "SetB-D4"
    # NeryLab 384_SetB
    SetB_D5 = "SetB-D5"
    # NeryLab 384_SetB
    SetB_D6 = "SetB-D6"
    # NeryLab 384_SetB
    SetB_D7 = "SetB-D7"
    # NeryLab 384_SetB
    SetB_D8 = "SetB-D8"
    # NeryLab 384_SetB
    SetB_D9 = "SetB-D9"
    # NeryLab 384_SetB
    SetB_E1 = "SetB-E1"
    # NeryLab 384_SetB
    SetB_E10 = "SetB-E10"
    # NeryLab 384_SetB
    SetB_E11 = "SetB-E11"
    # NeryLab 384_SetB
    SetB_E12 = "SetB-E12"
    # NeryLab 384_SetB
    SetB_E13 = "SetB-E13"
    # NeryLab 384_SetB
    SetB_E14 = "SetB-E14"
    # NeryLab 384_SetB
    SetB_E15 = "SetB-E15"
    # NeryLab 384_SetB
    SetB_E16 = "SetB-E16"
    # NeryLab 384_SetB
    SetB_E17 = "SetB-E17"
    # NeryLab 384_SetB
    SetB_E18 = "SetB-E18"
    # NeryLab 384_SetB
    SetB_E19 = "SetB-E19"
    # NeryLab 384_SetB
    SetB_E2 = "SetB-E2"
    # NeryLab 384_SetB
    SetB_E20 = "SetB-E20"
    # NeryLab 384_SetB
    SetB_E21 = "SetB-E21"
    # NeryLab 384_SetB
    SetB_E22 = "SetB-E22"
    # NeryLab 384_SetB
    SetB_E23 = "SetB-E23"
    # NeryLab 384_SetB
    SetB_E24 = "SetB-E24"
    # NeryLab 384_SetB
    SetB_E3 = "SetB-E3"
    # NeryLab 384_SetB
    SetB_E4 = "SetB-E4"
    # NeryLab 384_SetB
    SetB_E5 = "SetB-E5"
    # NeryLab 384_SetB
    SetB_E6 = "SetB-E6"
    # NeryLab 384_SetB
    SetB_E7 = "SetB-E7"
    # NeryLab 384_SetB
    SetB_E8 = "SetB-E8"
    # NeryLab 384_SetB
    SetB_E9 = "SetB-E9"
    # NeryLab 384_SetB
    SetB_F1 = "SetB-F1"
    # NeryLab 384_SetB
    SetB_F10 = "SetB-F10"
    # NeryLab 384_SetB
    SetB_F11 = "SetB-F11"
    # NeryLab 384_SetB
    SetB_F12 = "SetB-F12"
    # NeryLab 384_SetB
    SetB_F13 = "SetB-F13"
    # NeryLab 384_SetB
    SetB_F14 = "SetB-F14"
    # NeryLab 384_SetB
    SetB_F15 = "SetB-F15"
    # NeryLab 384_SetB
    SetB_F16 = "SetB-F16"
    # NeryLab 384_SetB
    SetB_F17 = "SetB-F17"
    # NeryLab 384_SetB
    SetB_F18 = "SetB-F18"
    # NeryLab 384_SetB
    SetB_F19 = "SetB-F19"
    # NeryLab 384_SetB
    SetB_F2 = "SetB-F2"
    # NeryLab 384_SetB
    SetB_F20 = "SetB-F20"
    # NeryLab 384_SetB
    SetB_F21 = "SetB-F21"
    # NeryLab 384_SetB
    SetB_F22 = "SetB-F22"
    # NeryLab 384_SetB
    SetB_F23 = "SetB-F23"
    # NeryLab 384_SetB
    SetB_F24 = "SetB-F24"
    # NeryLab 384_SetB
    SetB_F3 = "SetB-F3"
    # NeryLab 384_SetB
    SetB_F4 = "SetB-F4"
    # NeryLab 384_SetB
    SetB_F5 = "SetB-F5"
    # NeryLab 384_SetB
    SetB_F6 = "SetB-F6"
    # NeryLab 384_SetB
    SetB_F7 = "SetB-F7"
    # NeryLab 384_SetB
    SetB_F8 = "SetB-F8"
    # NeryLab 384_SetB
    SetB_F9 = "SetB-F9"
    # NeryLab 384_SetB
    SetB_G1 = "SetB-G1"
    # NeryLab 384_SetB
    SetB_G10 = "SetB-G10"
    # NeryLab 384_SetB
    SetB_G11 = "SetB-G11"
    # NeryLab 384_SetB
    SetB_G12 = "SetB-G12"
    # NeryLab 384_SetB
    SetB_G13 = "SetB-G13"
    # NeryLab 384_SetB
    SetB_G14 = "SetB-G14"
    # NeryLab 384_SetB
    SetB_G15 = "SetB-G15"
    # NeryLab 384_SetB
    SetB_G16 = "SetB-G16"
    # NeryLab 384_SetB
    SetB_G17 = "SetB-G17"
    # NeryLab 384_SetB
    SetB_G18 = "SetB-G18"
    # NeryLab 384_SetB
    SetB_G19 = "SetB-G19"
    # NeryLab 384_SetB
    SetB_G2 = "SetB-G2"
    # NeryLab 384_SetB
    SetB_G20 = "SetB-G20"
    # NeryLab 384_SetB
    SetB_G21 = "SetB-G21"
    # NeryLab 384_SetB
    SetB_G22 = "SetB-G22"
    # NeryLab 384_SetB
    SetB_G23 = "SetB-G23"
    # NeryLab 384_SetB
    SetB_G24 = "SetB-G24"
    # NeryLab 384_SetB
    SetB_G3 = "SetB-G3"
    # NeryLab 384_SetB
    SetB_G4 = "SetB-G4"
    # NeryLab 384_SetB
    SetB_G5 = "SetB-G5"
    # NeryLab 384_SetB
    SetB_G6 = "SetB-G6"
    # NeryLab 384_SetB
    SetB_G7 = "SetB-G7"
    # NeryLab 384_SetB
    SetB_G8 = "SetB-G8"
    # NeryLab 384_SetB
    SetB_G9 = "SetB-G9"
    # NeryLab 384_SetB
    SetB_H1 = "SetB-H1"
    # NeryLab 384_SetB
    SetB_H10 = "SetB-H10"
    # NeryLab 384_SetB
    SetB_H11 = "SetB-H11"
    # NeryLab 384_SetB
    SetB_H12 = "SetB-H12"
    # NeryLab 384_SetB
    SetB_H13 = "SetB-H13"
    # NeryLab 384_SetB
    SetB_H14 = "SetB-H14"
    # NeryLab 384_SetB
    SetB_H15 = "SetB-H15"
    # NeryLab 384_SetB
    SetB_H16 = "SetB-H16"
    # NeryLab 384_SetB
    SetB_H17 = "SetB-H17"
    # NeryLab 384_SetB
    SetB_H18 = "SetB-H18"
    # NeryLab 384_SetB
    SetB_H19 = "SetB-H19"
    # NeryLab 384_SetB
    SetB_H2 = "SetB-H2"
    # NeryLab 384_SetB
    SetB_H20 = "SetB-H20"
    # NeryLab 384_SetB
    SetB_H21 = "SetB-H21"
    # NeryLab 384_SetB
    SetB_H22 = "SetB-H22"
    # NeryLab 384_SetB
    SetB_H23 = "SetB-H23"
    # NeryLab 384_SetB
    SetB_H24 = "SetB-H24"
    # NeryLab 384_SetB
    SetB_H3 = "SetB-H3"
    # NeryLab 384_SetB
    SetB_H4 = "SetB-H4"
    # NeryLab 384_SetB
    SetB_H5 = "SetB-H5"
    # NeryLab 384_SetB
    SetB_H6 = "SetB-H6"
    # NeryLab 384_SetB
    SetB_H7 = "SetB-H7"
    # NeryLab 384_SetB
    SetB_H8 = "SetB-H8"
    # NeryLab 384_SetB
    SetB_H9 = "SetB-H9"
    # NeryLab 384_SetB
    SetB_I1 = "SetB-I1"
    # NeryLab 384_SetB
    SetB_I10 = "SetB-I10"
    # NeryLab 384_SetB
    SetB_I11 = "SetB-I11"
    # NeryLab 384_SetB
    SetB_I12 = "SetB-I12"
    # NeryLab 384_SetB
    SetB_I13 = "SetB-I13"
    # NeryLab 384_SetB
    SetB_I14 = "SetB-I14"
    # NeryLab 384_SetB
    SetB_I15 = "SetB-I15"
    # NeryLab 384_SetB
    SetB_I16 = "SetB-I16"
    # NeryLab 384_SetB
    SetB_I17 = "SetB-I17"
    # NeryLab 384_SetB
    SetB_I18 = "SetB-I18"
    # NeryLab 384_SetB
    SetB_I19 = "SetB-I19"
    # NeryLab 384_SetB
    SetB_I2 = "SetB-I2"
    # NeryLab 384_SetB
    SetB_I20 = "SetB-I20"
    # NeryLab 384_SetB
    SetB_I21 = "SetB-I21"
    # NeryLab 384_SetB
    SetB_I22 = "SetB-I22"
    # NeryLab 384_SetB
    SetB_I23 = "SetB-I23"
    # NeryLab 384_SetB
    SetB_I24 = "SetB-I24"
    # NeryLab 384_SetB
    SetB_I3 = "SetB-I3"
    # NeryLab 384_SetB
    SetB_I4 = "SetB-I4"
    # NeryLab 384_SetB
    SetB_I5 = "SetB-I5"
    # NeryLab 384_SetB
    SetB_I6 = "SetB-I6"
    # NeryLab 384_SetB
    SetB_I7 = "SetB-I7"
    # NeryLab 384_SetB/#
    SetB_I8 = "SetB-I8"


class Sex(str, Enum):
    # Male
    number_1 = "1"
    # Female
    number_2 = "2"
    # Other
    number_7 = "7"
    # Unknown
    number_8 = "8"
    # Not Reported
    number_9 = "9"


class AgeAtDeathReferencePoint(str, Enum):
    # birth
    birth = "birth"
    # conception
    conception = "conception"


class AgeAtDeathUnit(str, Enum):
    # days
    days = "days"
    # months
    months = "months"
    # years
    years = "years"


class OntologyClass(ConfiguredBaseModel):
    """
    a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")


class Annotation(ConfiguredBaseModel):
    """
    Biolink Model root class for entity annotations.
    """
    pass


class QuantityValue(Annotation):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value
    """
    has_unit: Optional[str] = Field(None, description="""connects a quantity value to a unit""")
    has_numeric_value: Optional[float] = Field(None, description="""connects a quantity value to a number""")


class Entity(ConfiguredBaseModel):
    """
    Root Biolink Model class for all things and informational relationships, real or imagined.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/Entity","biolink:Entity"]] = Field(["biolink:Entity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")


class NamedThing(Entity):
    """
    a databased entity or concept/class
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/NamedThing","biolink:NamedThing"]] = Field(["biolink:NamedThing"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")


class Attribute(NamedThing, OntologyClass):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    category: List[Literal["https://w3id.org/biolink/vocab/Attribute","biolink:Attribute"]] = Field(["biolink:Attribute"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    attribute_name: Optional[str] = Field(None, description="""The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.""")
    has_attribute_type: str = Field(..., description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    name: Optional[str] = Field(None, description="""The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.""")


class TaxonomicRank(OntologyClass):
    """
    A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")


class OrganismTaxon(NamedThing):
    """
    A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/OrganismTaxon","biolink:OrganismTaxon"]] = Field(["biolink:OrganismTaxon"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    has_taxonomic_rank: Optional[str] = Field(None)


class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some topic of discourse or is used as support.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/InformationContentEntity","biolink:InformationContentEntity"]] = Field(["biolink:InformationContentEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")


class Dataset(InformationContentEntity):
    """
    an item that refers to a collection of data from a data source.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/Dataset","biolink:Dataset"]] = Field(["biolink:Dataset"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")


class PhysicalEssenceOrOccurrent(ConfiguredBaseModel):
    """
    Either a physical or processual entity.
    """
    pass


class PhysicalEssence(PhysicalEssenceOrOccurrent):
    """
    Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge.
    """
    pass


class PhysicalEntity(PhysicalEssence, NamedThing):
    """
    An entity that has material reality (a.k.a. physical essence).
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/PhysicalEntity","biolink:PhysicalEntity"]] = Field(["biolink:PhysicalEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")


class Occurrent(PhysicalEssenceOrOccurrent):
    """
    A processual entity.
    """
    pass


class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """
    pass


class Activity(ActivityAndBehavior, NamedThing):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/Activity","biolink:Activity"]] = Field(["biolink:Activity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")


class Procedure(ActivityAndBehavior, NamedThing):
    """
    A series of actions conducted in a certain order or manner
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/Procedure","biolink:Procedure"]] = Field(["biolink:Procedure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")


class SubjectOfInvestigation(ConfiguredBaseModel):
    """
    An entity that has the role of being studied in an investigation, study, or experiment
    """
    pass


class MaterialSample(SubjectOfInvestigation, PhysicalEntity):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/MaterialSample","biolink:MaterialSample"]] = Field(["biolink:MaterialSample"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")


class ThingWithTaxon(ConfiguredBaseModel):
    """
    A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    in_taxon_label: Optional[str] = Field(None, description="""The human readable scientific name for the taxon of the entity.""")


class BiologicalEntity(ThingWithTaxon, NamedThing):
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/BiologicalEntity","biolink:BiologicalEntity"]] = Field(["biolink:BiologicalEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    in_taxon_label: Optional[str] = Field(None, description="""The human readable scientific name for the taxon of the entity.""")


class GenomicEntity(ConfiguredBaseModel):
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")


class ChemicalEntityOrGeneOrGeneProduct(ConfiguredBaseModel):
    """
    A union of chemical entities and children, and gene or gene product. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities.
    """
    pass


class MacromolecularMachineMixin(ConfiguredBaseModel):
    """
    A union of gene locus, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")


class GeneOrGeneProduct(MacromolecularMachineMixin):
    """
    A union of gene loci or gene products. Frequently an identifier for one will be used as proxy for another
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")


class Gene(GeneOrGeneProduct, ChemicalEntityOrGeneOrGeneProduct, GenomicEntity, BiologicalEntity, PhysicalEssence, OntologyClass):
    """
    A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/Gene","biolink:Gene"]] = Field(["biolink:Gene"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    in_taxon_label: Optional[str] = Field(None, description="""The human readable scientific name for the taxon of the entity.""")
    symbol: Optional[str] = Field(None, description="""Symbol for a particular thing""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")


class Genome(GenomicEntity, BiologicalEntity, PhysicalEssence, OntologyClass):
    """
    A genome is the sum of genetic material within a cell or virion.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/Genome","biolink:Genome"]] = Field(["biolink:Genome"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    in_taxon_label: Optional[str] = Field(None, description="""The human readable scientific name for the taxon of the entity.""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")


class ProvActivity(ConfiguredBaseModel):
    """
    An activity is something that occurs over a period of time and acts upon or with entities;  it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    used: Optional[str] = Field(None, description="""Usage is the beginning of utilizing an entity by an activity. Before usage, the activity had not begun to utilize this entity and could not have been affected by the entity.""")
    was_guided_by: Optional[str] = Field(None, description="""Guidance is the influence of an entity on an activity. This entity is known as an influencer, and the activity is influenced by the influencer.""")


class DissectionRoiDelineation(ProvActivity, Procedure):
    """
    The process of outlining a region of interest on a brain slab image to guide the dissection and generation of a tissue sample.
    """
    used: Optional[str] = Field(None, description="""The brain slab that was annotated by the delineation process.""")
    was_guided_by: Optional[str] = Field(None, description="""Guidance is the influence of an entity on an activity. This entity is known as an influencer, and the activity is influenced by the influencer.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/DissectionRoiDelineation","bican:DissectionRoiDelineation"]] = Field(["bican:DissectionRoiDelineation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class TissueDissection(ProvActivity, Procedure):
    """
    The process of dissecting a tissue sample from a brain slab guided by a dissection region of interest (ROI) delineation.
    """
    was_guided_by: Optional[str] = Field(None, description="""The dissection ROI polygon which was used to guide the tissue dissection.""")
    used: Optional[str] = Field(None, description="""The brain slab from which the tissue sample was dissected from.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/TissueDissection","bican:TissueDissection"]] = Field(["bican:TissueDissection"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class CellDissociation(ProvActivity, Procedure):
    """
    The process of generating dissociated cells from an input tissue sample. This process could also introduce a tissue-source barcode (eg cell hashing), allowing mixing of cell dissociation samples at the cell barcoding step.
    """
    used: Optional[List[str]] = Field(default_factory=list, description="""The input tissue sample(s) from which the dissociated cell sample was derived from.""")
    process_date: Optional[str] = Field(None, description="""Date of cell dissociation process.""")
    was_guided_by: Optional[str] = Field(None, description="""Guidance is the influence of an entity on an activity. This entity is known as an influencer, and the activity is influenced by the influencer.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/CellDissociation","bican:CellDissociation"]] = Field(["bican:CellDissociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class CellEnrichment(ProvActivity, Procedure):
    """
    The process of enriching a dissociated cell sample by including or excluding cells of different types based on an enrichment plan using techniques such as fluorescence-activated cell sorting (FACS). This process could also introduce a tissue-source barcode (eg cell hashing), allowing mixing of cell enriched samples at the cell barcoding step.
    """
    used: Optional[List[str]] = Field(default_factory=list, description="""The input dissociated cell sample(s) from which the enriched cell sample was derived from.""")
    process_date: Optional[str] = Field(None, description="""Date of cell enrichment process.""")
    was_guided_by: Optional[str] = Field(None, description="""Guidance is the influence of an entity on an activity. This entity is known as an influencer, and the activity is influenced by the influencer.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/CellEnrichment","bican:CellEnrichment"]] = Field(["bican:CellEnrichment"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class EnrichedCellSampleSplitting(ProvActivity, Procedure):
    """
    The process of splitting an enriched cell sample into several portions. Each portion may be used by the same or different groups for different scientific studies.
    """
    used: Optional[str] = Field(None, description="""The enrichment cell sample splitting process from which the enriched cell sample was generated by.""")
    was_guided_by: Optional[str] = Field(None, description="""Guidance is the influence of an entity on an activity. This entity is known as an influencer, and the activity is influenced by the influencer.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/EnrichedCellSampleSplitting","bican:EnrichedCellSampleSplitting"]] = Field(["bican:EnrichedCellSampleSplitting"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class CellBarcoding(ProvActivity, Procedure):
    """
    The process of adding a molecular barcode to individual cells in a sample. The input will be either dissociated cell sample or enriched cell sample. Cell barcodes are only guaranteed to be unique within this one collection. One dissociated cell sample or enriched cell sample can lead to multiple barcoded cell samples.
    """
    used: Optional[List[str]] = Field(default_factory=list, description="""The input dissociated or enriched cell sample(s) from which the barcoded cell sample was derived from.""")
    port_well: Optional[str] = Field(None, description="""Specific position of the loaded port of the 10x chip.  An Enriched or Dissociated Cell Sample is loaded into a port on a chip (creating a Barcoded Cell Sample). Can be left null for non-10x methods.""")
    input_quantity: Optional[int] = Field(None, description="""Number of enriched or dissociated cells/nuclei going into the barcoding process.""")
    process_date: Optional[str] = Field(None, description="""Date of cell barcoding process.""")
    method: Optional[BarcodedCellSampleTechnique] = Field(None, description="""Standardized nomenclature to describe the general barcoding method used.  For example: Multiome, ATAC Only, GEX Only or snm3C-seq.""")
    was_guided_by: Optional[str] = Field(None, description="""Guidance is the influence of an entity on an activity. This entity is known as an influencer, and the activity is influenced by the influencer.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/CellBarcoding","bican:CellBarcoding"]] = Field(["bican:CellBarcoding"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class CdnaAmplification(ProvActivity, Procedure):
    """
    The process of creating a collection of cDNA molecules derived and amplified from an input barcoded cell sample.  A large amount of cDNA is needed to have accurate and reliable sequencing detection of gene expression.  This process generates multiple copies of each mRNA transcript (expressed gene) within each cell while retaining the cell's unique barcode from the barcoding step. This is a necessary step for GEX methods but is not used for ATAC methods.
    """
    used: Optional[str] = Field(None, description="""The input barcoded cell sample from which amplified cDNA was derived from.""")
    pcr_cycles: Optional[int] = Field(None, description="""Number of PCR cycles used during cDNA amplification for this cDNA.""")
    process_date: Optional[date] = Field(None, description="""Date of cDNA amplification.""")
    set: Optional[str] = Field(None, description="""cDNA amplification set, containing multiple amplified_cDNA_names that were processed at the same time.""")
    was_guided_by: Optional[str] = Field(None, description="""Guidance is the influence of an entity on an activity. This entity is known as an influencer, and the activity is influenced by the influencer.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/CdnaAmplification","bican:CdnaAmplification"]] = Field(["bican:CdnaAmplification"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class LibraryConstruction(ProvActivity, Procedure):
    """
    The process of constructing a library from input material (such as amplified cDNA or barcoded cell sample) derived from one or more cell samples.  cDNA is fragmented into smaller pieces appropriate for sequencing and at the same time a library index barcode is incorporated to enable identification of library origin, allowing libraries to be pooled together for sequencing.
    """
    used: Optional[str] = Field(None, description="""The input barcoded cell sample or amplified cDNA from which the library was derived from.""")
    method: Optional[LibraryTechnique] = Field(None, description="""Standardized nomenclature to describe the specific library method used.  This specifies the alignment method required for the library.  For example, 10xV3.1 (for RNASeq single assay), 10xMult-GEX (for RNASeq multiome assay), and 10xMult-ATAC (for ATACSeq multiome assay).""")
    process_date: Optional[date] = Field(None, description="""Date of library construction.""")
    input_quantity_ng: Optional[float] = Field(None, description="""Amount of cDNA going into library construction in nanograms.""")
    set: Optional[str] = Field(None, description="""Library set, containing multiple library_names that were processed at the same time.""")
    was_guided_by: Optional[str] = Field(None, description="""Guidance is the influence of an entity on an activity. This entity is known as an influencer, and the activity is influenced by the influencer.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/LibraryConstruction","bican:LibraryConstruction"]] = Field(["bican:LibraryConstruction"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class LibraryPooling(ProvActivity, Procedure):
    """
    The process of constructing of a libray pool by combining library aliquots from a set of input libraries. Each library aliquot in a library pool will have a unique R1/R2 index to allow for sequencing together then separating the sequencing output by originating library aliquot through the process of demultiplexing.
    """
    used: Optional[List[str]] = Field(default_factory=list, description="""The input aliquot(s) from which the library pool was derived from.""")
    process_date: Optional[str] = Field(None, description="""Date of library pooling process.""")
    was_guided_by: Optional[str] = Field(None, description="""Guidance is the influence of an entity on an activity. This entity is known as an influencer, and the activity is influenced by the influencer.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/LibraryPooling","bican:LibraryPooling"]] = Field(["bican:LibraryPooling"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class ProvEntity(ConfiguredBaseModel):
    """
    An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects;  entities may be real or imaginary.
    """
    was_derived_from: Optional[str] = Field(None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.""")
    was_generated_by: Optional[str] = Field(None, description="""Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.""")
    annotates: Optional[str] = Field(None, description="""Annotation is the addition of metadata to an entity""")
    dissection_was_guided_by: Optional[str] = Field(None, description="""Tranformation (dissection) of one entity into another entity.""")


class Donor(ProvEntity, ThingWithTaxon, MaterialSample):
    """
    A person or organism that is the source of a biological sample for scientific study.  Many biological samples are generated from a single donor.
    """
    name: Optional[str] = Field(None, description="""Name of person or organism that is the source of a biological sample for scientific study.  Many biological samples are generated from a single donor.""")
    biological_sex: Optional[Sex] = Field(None, description="""Biological sex of donor at birth""")
    age_at_death_description: Optional[str] = Field(None, description="""Text description of the age of death following typical scientific convention for the species or developmental stage. For example: P56, E11.5""")
    age_at_death_reference_point: Optional[AgeAtDeathReferencePoint] = Field(None, description="""The reference point for an age interval; for example, birth or conception.""")
    age_at_death_unit: Optional[AgeAtDeathUnit] = Field(None, description="""The unit used for representing the donor age from the reference point.""")
    age_at_death_value: Optional[float] = Field(None, description="""The value representing the donor age from the reference point.""")
    species: Optional[str] = Field(None, description="""Species of donor.""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    in_taxon_label: Optional[str] = Field(None, description="""The human readable scientific name for the taxon of the entity.""")
    was_derived_from: Optional[str] = Field(None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.""")
    was_generated_by: Optional[str] = Field(None, description="""Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.""")
    annotates: Optional[str] = Field(None, description="""Annotation is the addition of metadata to an entity""")
    dissection_was_guided_by: Optional[str] = Field(None, description="""Tranformation (dissection) of one entity into another entity.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/Donor","bican:Donor"]] = Field(["bican:Donor"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class BrainSlab(ProvEntity, MaterialSample):
    """
    A thick flat piece of brain tissue obtained by slicing a whole brain, brain hemisphere or subdivision with a blade at regular interval.  When multiple brain slabs are obtained from the slicing process, an ordinal is assigned to provide information about the relative positioning of the slabs.
    """
    was_derived_from: Optional[str] = Field(None, description="""The donor from which the brain slab was derived from.""")
    name: Optional[str] = Field(None, description="""Name of a thick flat piece of brain tissue obtained by slicing a whole brain, brain hemisphere or subdivision with a blade at regular interval.  When multiple brain slabs are obtained from the slicing process, an ordinal is assigned to provide information about the relative positioning of the slabs.""")
    was_generated_by: Optional[str] = Field(None, description="""Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.""")
    annotates: Optional[str] = Field(None, description="""Annotation is the addition of metadata to an entity""")
    dissection_was_guided_by: Optional[str] = Field(None, description="""Tranformation (dissection) of one entity into another entity.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/BrainSlab","bican:BrainSlab"]] = Field(["bican:BrainSlab"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class TissueSample(ProvEntity, MaterialSample):
    """
    The final intact piece of tissue before cell or nuclei prep. This piece of tissue will be used in dissociation and has an region of interest polygon (ROI) associated with it.
    """
    was_derived_from: Optional[str] = Field(None, description="""The donor or brain slab from which the tissue sample was derived from.""")
    was_generated_by: Optional[str] = Field(None, description="""The dissection process from which the tissue sample was generated by.""")
    dissection_was_guided_by: Optional[str] = Field(None, description="""The dissection ROI polygon that was used to guide the dissection.""")
    name: Optional[str] = Field(None, description="""Identifier name for final intact piece of tissue before cell or nuclei prep.  This piece of tissue will be used in dissociation and has an ROI associated with it.""")
    structure: Optional[List[str]] = Field(default_factory=list, description="""Strucure of tissue sample.""")
    annotates: Optional[str] = Field(None, description="""Annotation is the addition of metadata to an entity""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/TissueSample","bican:TissueSample"]] = Field(["bican:TissueSample"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class DissociatedCellSample(ProvEntity, MaterialSample):
    """
    A collection of dissociated cells or nuclei derived from dissociation of a tissue sample.
    """
    was_generated_by: Optional[str] = Field(None, description="""The cell dissociation process from which the dissociated cell sample was generated by.""")
    was_derived_from: Optional[List[str]] = Field(default_factory=list, description="""The input tissue sample(s) from which dissociated cell sample was derived from.""")
    name: Optional[str] = Field(None, description="""Name of a collection of dissociated cells or nuclei derived from dissociation of a tissue sample.""")
    cell_prep_type: Optional[DissociatedCellSampleCellPrepType] = Field(None, description="""The type of cell preparation. For example: Cells, Nuclei. This is a property of dissociated_cell_sample.""")
    cell_source_oligo_name: Optional[DissociatedCellSampleCellLabelBarcode] = Field(None, description="""Name of cell source oligo used in cell plexing.  The oligo molecularly tags all the cells in the dissociated cell sample and allows separate dissociated cell samples to be combined downstream in the barcoded cell sample.  The oligo name is associated with a sequence in a lookup table.  This sequence will be needed during alignment to associate reads with the parent source dissociated cell sample.""")
    annotates: Optional[str] = Field(None, description="""Annotation is the addition of metadata to an entity""")
    dissection_was_guided_by: Optional[str] = Field(None, description="""Tranformation (dissection) of one entity into another entity.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/DissociatedCellSample","bican:DissociatedCellSample"]] = Field(["bican:DissociatedCellSample"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class EnrichedCellSample(ProvEntity, MaterialSample):
    """
    A collection of enriched cells or nuclei after enrichment process, usually via fluorescence-activated cell sorting (FACS) using the enrichment plan, is applied to dissociated cell sample.
    """
    was_generated_by: Optional[str] = Field(None, description="""The cell enrichment or sample splitting process from which the enriched cell sample was generated by.""")
    was_derived_from: Optional[List[str]] = Field(default_factory=list, description="""The dissociated or enriched cell sample(s) from which the enriched cell sample was derived from.""")
    name: Optional[str] = Field(None, description="""Name of collection of enriched cells or nuclei after enrichment process (usually via FACS using the Enrichment Plan) applied to dissociated_cell_sample.""")
    enrichment_population: Optional[str] = Field(None, description="""Actual percentage of cells as a result of using set of fluorescent marker label(s) to enrich dissociated_cell_sample with desired mix of cell populations.  This plan can also be used to describe 'No FACS' where no enrichment was performed.  This is a property of enriched_cell_prep_container.""")
    cell_source_oligo_name: Optional[str] = Field(None, description="""Name of cell source oligo used in cell plexing.  The oligo molecularly tags all the cells in the enriched cell sample and allows separate enriched cell samples to be combined downstream in the barcoded cell sample.  The oligo name is associated with a sequence in a lookup table.  This sequence will be needed during alignment to associate reads with the parent source enriched cell sample.""")
    histone_modification_marker: Optional[str] = Field(None, description="""Histone modification marker antibodies (eg H3K27ac, H3K27me3, H3K9me3) used in conjunction with an Enriched Cell Source Barcode in order to combine multiple Enriched Cell Populations before Barcoded Cell Sample step for 10xMultiome method. Each of the Histone antibodies captures an essential part of the epigenome.""")
    annotates: Optional[str] = Field(None, description="""Annotation is the addition of metadata to an entity""")
    dissection_was_guided_by: Optional[str] = Field(None, description="""Tranformation (dissection) of one entity into another entity.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/EnrichedCellSample","bican:EnrichedCellSample"]] = Field(["bican:EnrichedCellSample"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class BarcodedCellSample(ProvEntity, MaterialSample):
    """
    A collection of molecularly barcoded cells. Input will be either dissociated cell sample or enriched cell sample. Cell barcodes are only guaranteed to be unique within this one collection. One dissociated cell sample or enriched cell sample can lead to multiple barcoded cell samples.  The sequences of the molecular barcodes are revealed during alignment of the resulting fastq files for the barcoded cell sample. The barcoded cell sample name and the cell level molecular barcode together uniquely identify a single cell.
    """
    was_generated_by: Optional[str] = Field(None, description="""The barcoding process from which the barcoded cell sample is generated from.""")
    was_derived_from: Optional[List[str]] = Field(default_factory=list, description="""The input dissociated or enriched cell sample(s) from which the barcoded cell sample was derived from.""")
    name: Optional[str] = Field(None, description="""Name of a collection of barcoded cells.  Input will be either dissociated_cell_sample or enriched_cell_sample.  Cell barcodes are only guaranteed to be unique within this one collection. One dissociated_cell_sample or enriched_cell_sample can lead to multiple barcoded_cell_samples.""")
    number_of_expected_cells: Optional[int] = Field(None, description="""Expected number of cells/nuclei of a barcoded_cell_sample that will be barcoded and available for sequencing.  This is a derived number from 'Barcoded cell input quantity count' that is dependent on the \"capture rate\" of the barcoding method.  It is usually a calculated fraction of the 'Barcoded cell input quantity count' going into the barcoding method.""")
    annotates: Optional[str] = Field(None, description="""Annotation is the addition of metadata to an entity""")
    dissection_was_guided_by: Optional[str] = Field(None, description="""Tranformation (dissection) of one entity into another entity.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/BarcodedCellSample","bican:BarcodedCellSample"]] = Field(["bican:BarcodedCellSample"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class AmplifiedCdna(ProvEntity, MaterialSample):
    """
    A collection of cDNA molecules derived and amplified from an input barcoded cell sample. These cDNA molecules represent the gene expression of each cell, with all cDNA molecules from a given cell retaining that cell's unique barcode from the cell barcoding step. This is a necessary step for GEX methods but is not used for ATAC methods.
    """
    was_generated_by: Optional[str] = Field(None, description="""The cDNA amplification process from which the amplified cDNA was generated by.""")
    was_derived_from: Optional[str] = Field(None, description="""The input barcoded cell sample from which amplified cDNA was derived from.""")
    name: Optional[str] = Field(None, description="""Name of a collection of cDNA molecules derived and amplified from an input barcoded_cell_sample.  These cDNA molecules represent the gene expression of each cell, with all cDNA molecules from a given cell retaining that cell's unique barcode from the cell barcoding step.  This is a necessary step for GEX methods but is not used for ATAC methods.""")
    quantity_ng: Optional[float] = Field(None, description="""Amount of cDNA produced after cDNA amplification measured in nanograms.""")
    pass_fail_result: Optional[AmplifiedCdnaRnaAmplificationPassFail] = Field(None, description="""Pass or Fail result based on qualitative assessment of cDNA yield and size.""")
    percent_cdna_longer_than_400bp: Optional[float] = Field(None, description="""QC metric to measure mRNA degradation of cDNA.  Higher % is higher quality starting material.  Over 400bp is used as a universal cutoff for intact (full length) vs degraded cDNA and is a common output from Bioanalyzer and Fragment Analyzer elecropheragrams.""")
    annotates: Optional[str] = Field(None, description="""Annotation is the addition of metadata to an entity""")
    dissection_was_guided_by: Optional[str] = Field(None, description="""Tranformation (dissection) of one entity into another entity.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/AmplifiedCdna","bican:AmplifiedCdna"]] = Field(["bican:AmplifiedCdna"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class Library(ProvEntity, MaterialSample):
    """
    A collection of fragmented and barcode-indexed DNA molecules for sequencing. An index or barcode is typically introduced to enable identification of library origin to allow libraries to be pooled together for sequencing.
    """
    was_generated_by: Optional[str] = Field(None, description="""The library construction process from which the library was generated by.""")
    was_derived_from: Optional[str] = Field(None, description="""The input barcoded cell sample or amplified cDNA from which the library was derived from.""")
    name: Optional[str] = Field(None, description="""Name of a library, which is a collection of fragmented and barcode-indexed DNA molecules for sequencing.  An index or barcode is typically introduced to enable identification of library origin to allow libraries to be pooled together for sequencing.""")
    average_size_bp: Optional[int] = Field(None, description="""Average size of the library in terms of base pairs.  This is used to calculate the molarity before pooling and sequencing.""")
    concentration_nm: Optional[float] = Field(None, description="""Concentration of library in terms of nM (nMol/L).  Number of molecules is needed for accurate pooling of the libraries and for generating the number of target reads/cell in sequencing.""")
    pass_fail_result: Optional[LibraryPrepPassFail] = Field(None, description="""Pass or Fail result based on qualitative assessment of library yield and size.""")
    quantity_fmol: Optional[float] = Field(None, description="""Amount of library generated in terms of femtomoles""")
    quantity_ng: Optional[float] = Field(None, description="""Amount of library generated in terms of nanograms""")
    r1_r2_index: Optional[LibraryR1R2Index] = Field(None, description="""Name of the pair of library indexes used for sequencing.  Indexes allow libraries to be pooled together for sequencing.  Sequencing output (fastq) are demultiplexed by using the indexes for each library.  The name will be associated with the sequences of i7, i5, and i5as, which are needed by SeqCores for demultiplexing.  The required direction of the sequence (sense or antisense) of the index can differ depending on sequencing instruments.""")
    annotates: Optional[str] = Field(None, description="""Annotation is the addition of metadata to an entity""")
    dissection_was_guided_by: Optional[str] = Field(None, description="""Tranformation (dissection) of one entity into another entity.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/Library","bican:Library"]] = Field(["bican:Library"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class LibraryAliquot(ProvEntity, MaterialSample):
    """
    One library in the library pool. Each library aliquot in a library pool will have a unique R1/R2 index to allow for sequencing together then separating the sequencing output by originating library aliquot through the process of demultiplexing. The resulting demultiplexed fastq files will include the library aliquot name.  A given library may produce multiple library aliquots, which is done in the case of resequencing.  Each library aliquot will produce a set of fastq files.
    """
    was_derived_from: Optional[str] = Field(None, description="""The input library from which the library aliquot was derived from.""")
    name: Optional[str] = Field(None, description="""One library in the library pool.  Each Library_aliquot_name in a library pool will have a unique R1/R2 index to allow for sequencing together then separating the sequencing output by originating library aliquot through the process of demultiplexing.  The resulting demultiplexed fastq files will include the library_aliquot_name.""")
    was_generated_by: Optional[str] = Field(None, description="""Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.""")
    annotates: Optional[str] = Field(None, description="""Annotation is the addition of metadata to an entity""")
    dissection_was_guided_by: Optional[str] = Field(None, description="""Tranformation (dissection) of one entity into another entity.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/LibraryAliquot","bican:LibraryAliquot"]] = Field(["bican:LibraryAliquot"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class LibraryPool(ProvEntity, MaterialSample):
    """
    A library pool is made up of library aliquots from multiple libraries. Each library aliquot in a library pool will have a unique R1/R2 index to allow for sequencing together then separating the sequencing output by originating library aliquot through the process of demultiplexing.
    """
    was_generated_by: Optional[str] = Field(None, description="""The pooling process from which the library pool was generated by.""")
    was_derived_from: Optional[List[str]] = Field(default_factory=list, description="""The input aliquot(s) from which the library pool was derived from.""")
    name: Optional[str] = Field(None, description="""Library lab's library pool name.  For some labs this may be the same as \"Libray pool tube local name\".   Other labs distinguish between the local tube label of the library pool and the library pool name provided to SeqCore for tracking.  Local Pool Name is used to communicate sequencing status between SeqCore and Library Labs.""")
    local_tube_id: Optional[str] = Field(None, description="""Library Pool Tube local name.  Label of the tube containing the library pool, which is made up of multiple library_aliquots.  This is a Library Lab local tube name, before the pool is aliquoted to the Seq Core provided tube 'Library Pool Tube Name'.""")
    annotates: Optional[str] = Field(None, description="""Annotation is the addition of metadata to an entity""")
    dissection_was_guided_by: Optional[str] = Field(None, description="""Tranformation (dissection) of one entity into another entity.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/LibraryPool","bican:LibraryPool"]] = Field(["bican:LibraryPool"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


class DissectionRoiPolygon(ProvEntity, Entity):
    """
    A polygon annotated on a brain slab image delineating a region of interest (ROI) for a tissue sample dissectioning.
    """
    was_generated_by: Optional[str] = Field(None, description="""The delineation process from which the dissection ROI polygon was generated by.""")
    annotates: Optional[str] = Field(None, description="""The brain slab that was annotated by the delineation process.""")
    name: Optional[str] = Field(None, description="""Name of a polygon annotated on a brain slab image delineating a region of interest (ROI) for a tissue sample dissectioning.""")
    was_derived_from: Optional[str] = Field(None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.""")
    dissection_was_guided_by: Optional[str] = Field(None, description="""Tranformation (dissection) of one entity into another entity.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/DissectionRoiPolygon","bican:DissectionRoiPolygon"]] = Field(["bican:DissectionRoiPolygon"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")

    @field_validator('category')
    def pattern_category(cls, v):
        pattern=re.compile(r"^bican:[A-Z][A-Za-z]+$")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid category format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid category format: {v}")
        return v


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
OntologyClass.model_rebuild()
Annotation.model_rebuild()
QuantityValue.model_rebuild()
Entity.model_rebuild()
NamedThing.model_rebuild()
Attribute.model_rebuild()
TaxonomicRank.model_rebuild()
OrganismTaxon.model_rebuild()
InformationContentEntity.model_rebuild()
Dataset.model_rebuild()
PhysicalEssenceOrOccurrent.model_rebuild()
PhysicalEssence.model_rebuild()
PhysicalEntity.model_rebuild()
Occurrent.model_rebuild()
ActivityAndBehavior.model_rebuild()
Activity.model_rebuild()
Procedure.model_rebuild()
SubjectOfInvestigation.model_rebuild()
MaterialSample.model_rebuild()
ThingWithTaxon.model_rebuild()
BiologicalEntity.model_rebuild()
GenomicEntity.model_rebuild()
ChemicalEntityOrGeneOrGeneProduct.model_rebuild()
MacromolecularMachineMixin.model_rebuild()
GeneOrGeneProduct.model_rebuild()
Gene.model_rebuild()
Genome.model_rebuild()
ProvActivity.model_rebuild()
DissectionRoiDelineation.model_rebuild()
TissueDissection.model_rebuild()
CellDissociation.model_rebuild()
CellEnrichment.model_rebuild()
EnrichedCellSampleSplitting.model_rebuild()
CellBarcoding.model_rebuild()
CdnaAmplification.model_rebuild()
LibraryConstruction.model_rebuild()
LibraryPooling.model_rebuild()
ProvEntity.model_rebuild()
Donor.model_rebuild()
BrainSlab.model_rebuild()
TissueSample.model_rebuild()
DissociatedCellSample.model_rebuild()
EnrichedCellSample.model_rebuild()
BarcodedCellSample.model_rebuild()
AmplifiedCdna.model_rebuild()
Library.model_rebuild()
LibraryAliquot.model_rebuild()
LibraryPool.model_rebuild()
DissectionRoiPolygon.model_rebuild()

