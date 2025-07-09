from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
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




class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'bican',
     'default_range': 'string',
     'description': 'The Library Generation schema is designed to represent types '
                    'and relationships of samples and digital data assets '
                    'generated during processes that generate multimodal genomic '
                    'data.',
     'id': 'https://identifiers.org/brain-bican/library-generation-schema',
     'imports': ['bican_biolink', 'bican_core', 'bican_prov', 'linkml:types'],
     'name': 'library-generation-schema',
     'prefixes': {'NIMP': {'prefix_prefix': 'NIMP',
                           'prefix_reference': 'http://example.org/NIMP/'},
                  'bican': {'prefix_prefix': 'bican',
                            'prefix_reference': 'https://identifiers.org/brain-bican/vocab/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'ncbi': {'prefix_prefix': 'ncbi',
                           'prefix_reference': 'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'spdx': {'prefix_prefix': 'spdx',
                           'prefix_reference': 'http://spdx.org/rdf/terms#'}},
     'source_file': 'library_generation.yaml',
     'subsets': {'alignment': {'description': 'A subset of slots/attributes that '
                                              'are required for alignment.',
                               'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
                               'name': 'alignment'},
                 'analysis': {'description': 'A subset of slots/attributes that '
                                             'are required for analysis.',
                              'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
                              'name': 'analysis'},
                 'bican': {'description': 'A subset of classes that are associated '
                                          'with BICAN.',
                           'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
                           'name': 'bican'},
                 'library_generation': {'description': 'A subset of classes that '
                                                       'are associated with '
                                                       'library generation.',
                                        'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
                                        'name': 'library_generation'},
                 'processing_elements': {'description': 'A subset of classes that '
                                                        'are associated with '
                                                        'processing.',
                                         'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
                                         'name': 'processing_elements'},
                 'sequencing_elements': {'description': 'A subset of classes that '
                                                        'are associated with '
                                                        'sequencing.',
                                         'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
                                         'name': 'sequencing_elements'},
                 'tissue_specimen': {'description': 'A subset of classes that are '
                                                    'associated with tissue '
                                                    'specimens.',
                                     'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
                                     'name': 'tissue_specimen'},
                 'tracking': {'description': 'A subset of slots/attributes that '
                                             'are required for tracking.',
                              'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
                              'name': 'tracking'}},
     'title': 'Library Generation Schema'} )

class DigestType(str, Enum):
    SHA1 = "spdx:checksumAlgorithm_sha1"
    MD5 = "spdx:checksumAlgorithm_md5"
    SHA256 = "spdx:checksumAlgorithm_sha256"


class AmplifiedCdnaRnaAmplificationPassFail(str, Enum):
    Pass = "Pass"
    """
    The RNA amplification passed the QA/QC
    """
    Fail = "Fail"
    """
    The RNA amplification failed the QA/QC
    """
    Low_QC = "Low QC"
    """
    The RNA amplification low passed the QA/QC
    """
    Not_evaluated = "Not evaluated"
    """
    Library Prep not evaluated for QA/QC
    """


class BarcodedCellSampleTechnique(str, Enum):
    Multiome = "Multiome"
    """
    Multiome
    """
    ATACOnly = "ATACOnly"
    """
    ATACOnly
    """
    GEXOnly = "GEXOnly"
    """
    GEXOnly
    """
    snm3C_seq = "snm3C-seq"
    """
    snm3C-seq
    """


class DissociatedCellSampleCellPrepType(str, Enum):
    Nuclei = "Nuclei"
    """
    isolated nuclei
    """
    Cells = "Cells"
    """
    isolated whole cells
    """


class DissociatedCellSampleCellLabelBarcode(str, Enum):
    CMO301 = "CMO301"
    """
    10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    """
    CMO302 = "CMO302"
    """
    10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    """
    CMO303 = "CMO303"
    """
    10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    """
    CMO304 = "CMO304"
    """
    10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    """
    CMO305 = "CMO305"
    """
    10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    """
    CMO306 = "CMO306"
    """
    10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    """
    CMO307 = "CMO307"
    """
    10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    """
    CMO308 = "CMO308"
    """
    10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    """
    CMO309 = "CMO309"
    """
    10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    """
    CMO310 = "CMO310"
    """
    10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    """
    CMO311 = "CMO311"
    """
    10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    """
    CMO312 = "CMO312"
    """
    10x Cell Plex oligo tag for multiplexing tissue sources into a single 10x load.
    """
    number_2nt_001 = "2nt-001"
    """
    Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    """
    number_2nt_002 = "2nt-002"
    """
    Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    """
    number_2nt_003 = "2nt-003"
    """
    Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    """
    number_2nt_004 = "2nt-004"
    """
    Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    """
    number_3nt_001 = "3nt-001"
    """
    Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    """
    number_3nt_002 = "3nt-002"
    """
    Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    """
    number_3nt_003 = "3nt-003"
    """
    Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    """
    number_3nt_004 = "3nt-004"
    """
    Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    """
    number_3nt_005 = "3nt-005"
    """
    Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    """
    number_3nt_006 = "3nt-006"
    """
    Used in conjunction with Histone antibody to capture and tag separate subcomponents of the epigenome. Allows for pooling of enriched cell samples into a single 10x load.
    """


class LibraryTechnique(str, Enum):
    SMARTSeqSC = "SMARTSeqSC"
    """
    SMARTSeqSC
    """
    SmartSeq3 = "SmartSeq3"
    """
    SmartSeq3
    """
    number_10xV3FULL_STOP1 = "10xV3.1"
    """
    10xV3.1
    """
    number_10xV3FULL_STOP1_HT = "10xV3.1_HT"
    """
    10xV3.1_HT
    """
    number_10xMultiomeSEMICOLONGEX = "10xMultiome;GEX"
    """
    10xMultiome;GEX
    """
    number_10xMultiomeSEMICOLONATAC = "10xMultiome;ATAC"
    """
    10xMultiome;ATAC
    """
    number_10xATAC_V2FULL_STOP0 = "10xATAC_V2.0"
    """
    10xATAC_V2.0
    """
    number_10XMultiome_CellHashingSEMICOLONGEX = "10XMultiome-CellHashing;GEX"
    """
    10XMultiome-CellHashing;GEX
    """
    number_10XMultiome_CellHashingSEMICOLONATAC = "10XMultiome-CellHashing;ATAC"
    """
    10XMultiome-CellHashing;ATAC
    """
    number_10XMultiome_Cell_HashingSEMICOLONBarcode = "10XMultiome-Cell Hashing;Barcode"
    """
    10XMultiome-Cell Hashing;Barcode
    """
    number_10xV3FULL_STOP1_CellPlexSEMICOLONGEX = "10xV3.1_CellPlex;GEX"
    """
    10xV3.1_CellPlex;GEX
    """
    number_10xV3FULL_STOP1_CellPlexSEMICOLONBarcode = "10xV3.1_CellPlex;Barcode"
    """
    10xV3.1_CellPlex;Barcode
    """
    number_10xV3FULL_STOP1_HT_CellPlexSEMICOLONGEX = "10xV3.1_HT_CellPlex;GEX"
    """
    10xV3.1_HT_CellPlex;GEX
    """
    number_10xV3FULL_STOP1_HT_CellPlexSEMICOLONBarcode = "10xV3.1_HT_CellPlex;Barcode"
    """
    10xV3.1_HT_CellPlex;Barcode
    """
    MethylC_Seq = "MethylC-Seq"
    """
    MethylC-Seq
    """
    snm3C_seq = "snm3C-seq"
    """
    snm3C-seq
    """
    snmCT_seq = "snmCT-seq"
    """
    snmCT-seq
    """
    scATAC_seq = "scATAC-seq"
    """
    scATAC-seq
    """
    MERFISH = "MERFISH"
    """
    MERFISH
    """
    Slide_seq_MERFISH = "Slide-seq MERFISH"
    """
    Slide-seq MERFISH
    """
    whole_brain_MERFISH = "whole brain MERFISH"
    """
    whole brain MERFISH
    """
    DBiT_RNA_seq = "DBiT RNA-seq"
    """
    DBiT RNA-seq
    """
    DBiT_ATAC_seq = "DBiT ATAC-seq"
    """
    DBiT ATAC-seq
    """


class LibraryPrepPassFail(str, Enum):
    Pass = "Pass"
    """
    Library Prep passed the QA/QC
    """
    Fail = "Fail"
    """
    Library Prep failed the QA/QC
    """
    Low_QC = "Low QC"
    """
    Library Prep low passed the QA/QC
    """
    Not_evaluated = "Not evaluated"
    """
    Library Prep not evaluated for QA/QC
    """


class LibraryR1R2Index(str, Enum):
    SI_TT_A1 = "SI-TT-A1"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_A2 = "SI-TT-A2"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_A3 = "SI-TT-A3"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_A4 = "SI-TT-A4"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_A5 = "SI-TT-A5"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_A6 = "SI-TT-A6"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_A7 = "SI-TT-A7"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_A8 = "SI-TT-A8"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_A9 = "SI-TT-A9"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_A10 = "SI-TT-A10"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_A11 = "SI-TT-A11"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_A12 = "SI-TT-A12"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_B1 = "SI-TT-B1"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_B2 = "SI-TT-B2"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_B3 = "SI-TT-B3"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_B4 = "SI-TT-B4"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_B5 = "SI-TT-B5"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_B6 = "SI-TT-B6"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_B7 = "SI-TT-B7"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_B8 = "SI-TT-B8"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_B9 = "SI-TT-B9"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_B10 = "SI-TT-B10"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_B11 = "SI-TT-B11"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_B12 = "SI-TT-B12"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_C1 = "SI-TT-C1"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_C2 = "SI-TT-C2"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_C3 = "SI-TT-C3"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_C4 = "SI-TT-C4"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_C5 = "SI-TT-C5"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_C6 = "SI-TT-C6"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_C7 = "SI-TT-C7"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_C8 = "SI-TT-C8"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_C9 = "SI-TT-C9"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_C10 = "SI-TT-C10"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_C11 = "SI-TT-C11"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_C12 = "SI-TT-C12"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_D1 = "SI-TT-D1"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_D2 = "SI-TT-D2"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_D3 = "SI-TT-D3"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_D4 = "SI-TT-D4"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_D5 = "SI-TT-D5"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_D6 = "SI-TT-D6"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_D7 = "SI-TT-D7"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_D8 = "SI-TT-D8"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_D9 = "SI-TT-D9"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_D10 = "SI-TT-D10"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_D11 = "SI-TT-D11"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_D12 = "SI-TT-D12"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_E1 = "SI-TT-E1"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_E2 = "SI-TT-E2"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_E3 = "SI-TT-E3"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_E4 = "SI-TT-E4"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_E5 = "SI-TT-E5"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_E6 = "SI-TT-E6"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_E7 = "SI-TT-E7"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_E8 = "SI-TT-E8"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_E9 = "SI-TT-E9"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_E10 = "SI-TT-E10"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_E11 = "SI-TT-E11"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_E12 = "SI-TT-E12"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_F1 = "SI-TT-F1"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_F2 = "SI-TT-F2"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_F3 = "SI-TT-F3"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_F4 = "SI-TT-F4"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_F5 = "SI-TT-F5"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_F6 = "SI-TT-F6"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_F7 = "SI-TT-F7"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_F8 = "SI-TT-F8"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_F9 = "SI-TT-F9"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_F10 = "SI-TT-F10"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_F11 = "SI-TT-F11"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_F12 = "SI-TT-F12"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_G1 = "SI-TT-G1"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_G2 = "SI-TT-G2"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_G3 = "SI-TT-G3"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_G4 = "SI-TT-G4"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_G5 = "SI-TT-G5"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_G6 = "SI-TT-G6"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_G7 = "SI-TT-G7"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_G8 = "SI-TT-G8"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_G9 = "SI-TT-G9"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_G10 = "SI-TT-G10"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_G11 = "SI-TT-G11"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_G12 = "SI-TT-G12"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_H1 = "SI-TT-H1"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_H2 = "SI-TT-H2"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_H3 = "SI-TT-H3"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_H4 = "SI-TT-H4"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_H5 = "SI-TT-H5"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_H6 = "SI-TT-H6"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_H7 = "SI-TT-H7"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_H8 = "SI-TT-H8"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_H9 = "SI-TT-H9"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_H10 = "SI-TT-H10"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_H11 = "SI-TT-H11"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_TT_H12 = "SI-TT-H12"
    """
    10x Dual Index TT Set A. Used with 10xV3.1, 10xV3.1_HT, and 10xMultiome;GEX
    """
    SI_NN_A1 = "SI-NN-A1"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_A2 = "SI-NN-A2"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_A3 = "SI-NN-A3"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_A4 = "SI-NN-A4"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_A5 = "SI-NN-A5"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_A6 = "SI-NN-A6"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_A7 = "SI-NN-A7"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_A8 = "SI-NN-A8"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_A9 = "SI-NN-A9"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_A10 = "SI-NN-A10"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_A11 = "SI-NN-A11"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_A12 = "SI-NN-A12"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_B1 = "SI-NN-B1"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_B2 = "SI-NN-B2"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_B3 = "SI-NN-B3"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_B4 = "SI-NN-B4"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_B5 = "SI-NN-B5"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_B6 = "SI-NN-B6"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_B7 = "SI-NN-B7"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_B8 = "SI-NN-B8"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_B9 = "SI-NN-B9"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_B10 = "SI-NN-B10"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_B11 = "SI-NN-B11"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_B12 = "SI-NN-B12"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_C1 = "SI-NN-C1"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_C2 = "SI-NN-C2"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_C3 = "SI-NN-C3"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_C4 = "SI-NN-C4"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_C5 = "SI-NN-C5"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_C6 = "SI-NN-C6"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_C7 = "SI-NN-C7"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_C8 = "SI-NN-C8"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_C9 = "SI-NN-C9"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_C10 = "SI-NN-C10"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_C11 = "SI-NN-C11"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_C12 = "SI-NN-C12"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_D1 = "SI-NN-D1"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_D2 = "SI-NN-D2"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_D3 = "SI-NN-D3"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_D4 = "SI-NN-D4"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_D5 = "SI-NN-D5"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_D6 = "SI-NN-D6"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_D7 = "SI-NN-D7"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_D8 = "SI-NN-D8"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_D9 = "SI-NN-D9"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_D10 = "SI-NN-D10"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_D11 = "SI-NN-D11"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_D12 = "SI-NN-D12"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_E1 = "SI-NN-E1"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_E2 = "SI-NN-E2"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_E3 = "SI-NN-E3"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_E4 = "SI-NN-E4"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_E5 = "SI-NN-E5"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_E6 = "SI-NN-E6"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_E7 = "SI-NN-E7"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_E8 = "SI-NN-E8"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_E9 = "SI-NN-E9"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_E10 = "SI-NN-E10"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_E11 = "SI-NN-E11"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_E12 = "SI-NN-E12"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_F1 = "SI-NN-F1"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_F2 = "SI-NN-F2"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_F3 = "SI-NN-F3"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_F4 = "SI-NN-F4"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_F5 = "SI-NN-F5"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_F6 = "SI-NN-F6"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_F7 = "SI-NN-F7"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_F8 = "SI-NN-F8"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_F9 = "SI-NN-F9"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_F10 = "SI-NN-F10"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_F11 = "SI-NN-F11"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_F12 = "SI-NN-F12"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_G1 = "SI-NN-G1"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_G2 = "SI-NN-G2"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_G3 = "SI-NN-G3"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_G4 = "SI-NN-G4"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_G5 = "SI-NN-G5"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_G6 = "SI-NN-G6"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_G7 = "SI-NN-G7"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_G8 = "SI-NN-G8"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_G9 = "SI-NN-G9"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_G10 = "SI-NN-G10"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_G11 = "SI-NN-G11"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_G12 = "SI-NN-G12"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_H1 = "SI-NN-H1"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_H2 = "SI-NN-H2"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_H3 = "SI-NN-H3"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_H4 = "SI-NN-H4"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_H5 = "SI-NN-H5"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_H6 = "SI-NN-H6"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_H7 = "SI-NN-H7"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_H8 = "SI-NN-H8"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_H9 = "SI-NN-H9"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_H10 = "SI-NN-H10"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_H11 = "SI-NN-H11"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NN_H12 = "SI-NN-H12"
    """
    10x Dual Index NN Set A. Used with 10xV3.1_CellPlex;GEX and 10xV3.1-HT_CellPlex;GEX
    """
    SI_NA_A1 = "SI-NA-A1"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_B1 = "SI-NA-B1"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_C1 = "SI-NA-C1"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_D1 = "SI-NA-D1"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_E1 = "SI-NA-E1"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_F1 = "SI-NA-F1"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_G1 = "SI-NA-G1"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_H1 = "SI-NA-H1"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_A2 = "SI-NA-A2"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_B2 = "SI-NA-B2"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_C2 = "SI-NA-C2"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_D2 = "SI-NA-D2"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_E2 = "SI-NA-E2"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_F2 = "SI-NA-F2"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_G2 = "SI-NA-G2"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_H2 = "SI-NA-H2"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_A3 = "SI-NA-A3"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_B3 = "SI-NA-B3"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_C3 = "SI-NA-C3"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_D3 = "SI-NA-D3"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_E3 = "SI-NA-E3"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_F3 = "SI-NA-F3"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_G3 = "SI-NA-G3"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_H3 = "SI-NA-H3"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_A4 = "SI-NA-A4"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_B4 = "SI-NA-B4"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_C4 = "SI-NA-C4"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_D4 = "SI-NA-D4"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_E4 = "SI-NA-E4"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_F4 = "SI-NA-F4"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_G4 = "SI-NA-G4"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_H4 = "SI-NA-H4"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_A5 = "SI-NA-A5"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_B5 = "SI-NA-B5"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_C5 = "SI-NA-C5"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_D5 = "SI-NA-D5"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_E5 = "SI-NA-E5"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_F5 = "SI-NA-F5"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_G5 = "SI-NA-G5"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_H5 = "SI-NA-H5"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_A6 = "SI-NA-A6"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_B6 = "SI-NA-B6"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_C6 = "SI-NA-C6"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_D6 = "SI-NA-D6"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_E6 = "SI-NA-E6"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_F6 = "SI-NA-F6"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_G6 = "SI-NA-G6"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_H6 = "SI-NA-H6"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_A7 = "SI-NA-A7"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_B7 = "SI-NA-B7"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_C7 = "SI-NA-C7"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_D7 = "SI-NA-D7"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_E7 = "SI-NA-E7"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_F7 = "SI-NA-F7"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_G7 = "SI-NA-G7"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_H7 = "SI-NA-H7"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_A8 = "SI-NA-A8"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_B8 = "SI-NA-B8"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_C8 = "SI-NA-C8"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_D8 = "SI-NA-D8"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_E8 = "SI-NA-E8"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_F8 = "SI-NA-F8"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_G8 = "SI-NA-G8"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_H8 = "SI-NA-H8"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_A9 = "SI-NA-A9"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_B9 = "SI-NA-B9"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_C9 = "SI-NA-C9"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_D9 = "SI-NA-D9"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_E9 = "SI-NA-E9"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_F9 = "SI-NA-F9"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_G9 = "SI-NA-G9"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_H9 = "SI-NA-H9"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_A10 = "SI-NA-A10"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_B10 = "SI-NA-B10"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_C10 = "SI-NA-C10"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_D10 = "SI-NA-D10"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_E10 = "SI-NA-E10"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_F10 = "SI-NA-F10"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_G10 = "SI-NA-G10"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_H10 = "SI-NA-H10"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_A11 = "SI-NA-A11"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_B11 = "SI-NA-B11"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_C11 = "SI-NA-C11"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_D11 = "SI-NA-D11"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_E11 = "SI-NA-E11"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_F11 = "SI-NA-F11"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_G11 = "SI-NA-G11"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_H11 = "SI-NA-H11"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_A12 = "SI-NA-A12"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_B12 = "SI-NA-B12"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_C12 = "SI-NA-C12"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_D12 = "SI-NA-D12"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_E12 = "SI-NA-E12"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_F12 = "SI-NA-F12"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_G12 = "SI-NA-G12"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SI_NA_H12 = "SI-NA-H12"
    """
    10x Single Index N Set A. Used with 10xATAC_v2.0 and 10xMultiome;ATAC
    """
    SetB_A1 = "SetB-A1"
    """
    NeryLab 384_SetB
    """
    SetB_A10 = "SetB-A10"
    """
    NeryLab 384_SetB
    """
    SetB_A11 = "SetB-A11"
    """
    NeryLab 384_SetB
    """
    SetB_A12 = "SetB-A12"
    """
    NeryLab 384_SetB
    """
    SetB_A13 = "SetB-A13"
    """
    NeryLab 384_SetB
    """
    SetB_A14 = "SetB-A14"
    """
    NeryLab 384_SetB
    """
    SetB_A15 = "SetB-A15"
    """
    NeryLab 384_SetB
    """
    SetB_A16 = "SetB-A16"
    """
    NeryLab 384_SetB
    """
    SetB_A17 = "SetB-A17"
    """
    NeryLab 384_SetB
    """
    SetB_A18 = "SetB-A18"
    """
    NeryLab 384_SetB
    """
    SetB_A19 = "SetB-A19"
    """
    NeryLab 384_SetB
    """
    SetB_A2 = "SetB-A2"
    """
    NeryLab 384_SetB
    """
    SetB_A20 = "SetB-A20"
    """
    NeryLab 384_SetB
    """
    SetB_A21 = "SetB-A21"
    """
    NeryLab 384_SetB
    """
    SetB_A22 = "SetB-A22"
    """
    NeryLab 384_SetB
    """
    SetB_A23 = "SetB-A23"
    """
    NeryLab 384_SetB
    """
    SetB_A24 = "SetB-A24"
    """
    NeryLab 384_SetB
    """
    SetB_A3 = "SetB-A3"
    """
    NeryLab 384_SetB
    """
    SetB_A4 = "SetB-A4"
    """
    NeryLab 384_SetB
    """
    SetB_A5 = "SetB-A5"
    """
    NeryLab 384_SetB
    """
    SetB_A6 = "SetB-A6"
    """
    NeryLab 384_SetB
    """
    SetB_A7 = "SetB-A7"
    """
    NeryLab 384_SetB
    """
    SetB_A8 = "SetB-A8"
    """
    NeryLab 384_SetB
    """
    SetB_A9 = "SetB-A9"
    """
    NeryLab 384_SetB
    """
    SetB_B1 = "SetB-B1"
    """
    NeryLab 384_SetB
    """
    SetB_B10 = "SetB-B10"
    """
    NeryLab 384_SetB
    """
    SetB_B11 = "SetB-B11"
    """
    NeryLab 384_SetB
    """
    SetB_B12 = "SetB-B12"
    """
    NeryLab 384_SetB
    """
    SetB_B13 = "SetB-B13"
    """
    NeryLab 384_SetB
    """
    SetB_B14 = "SetB-B14"
    """
    NeryLab 384_SetB
    """
    SetB_B15 = "SetB-B15"
    """
    NeryLab 384_SetB
    """
    SetB_B16 = "SetB-B16"
    """
    NeryLab 384_SetB
    """
    SetB_B17 = "SetB-B17"
    """
    NeryLab 384_SetB
    """
    SetB_B18 = "SetB-B18"
    """
    NeryLab 384_SetB
    """
    SetB_B19 = "SetB-B19"
    """
    NeryLab 384_SetB
    """
    SetB_B2 = "SetB-B2"
    """
    NeryLab 384_SetB
    """
    SetB_B20 = "SetB-B20"
    """
    NeryLab 384_SetB
    """
    SetB_B21 = "SetB-B21"
    """
    NeryLab 384_SetB
    """
    SetB_B22 = "SetB-B22"
    """
    NeryLab 384_SetB
    """
    SetB_B23 = "SetB-B23"
    """
    NeryLab 384_SetB
    """
    SetB_B24 = "SetB-B24"
    """
    NeryLab 384_SetB
    """
    SetB_B3 = "SetB-B3"
    """
    NeryLab 384_SetB
    """
    SetB_B4 = "SetB-B4"
    """
    NeryLab 384_SetB
    """
    SetB_B5 = "SetB-B5"
    """
    NeryLab 384_SetB
    """
    SetB_B6 = "SetB-B6"
    """
    NeryLab 384_SetB
    """
    SetB_B7 = "SetB-B7"
    """
    NeryLab 384_SetB
    """
    SetB_B8 = "SetB-B8"
    """
    NeryLab 384_SetB
    """
    SetB_B9 = "SetB-B9"
    """
    NeryLab 384_SetB
    """
    SetB_C1 = "SetB-C1"
    """
    NeryLab 384_SetB
    """
    SetB_C10 = "SetB-C10"
    """
    NeryLab 384_SetB
    """
    SetB_C11 = "SetB-C11"
    """
    NeryLab 384_SetB
    """
    SetB_C12 = "SetB-C12"
    """
    NeryLab 384_SetB
    """
    SetB_C13 = "SetB-C13"
    """
    NeryLab 384_SetB
    """
    SetB_C14 = "SetB-C14"
    """
    NeryLab 384_SetB
    """
    SetB_C15 = "SetB-C15"
    """
    NeryLab 384_SetB
    """
    SetB_C16 = "SetB-C16"
    """
    NeryLab 384_SetB
    """
    SetB_C17 = "SetB-C17"
    """
    NeryLab 384_SetB
    """
    SetB_C18 = "SetB-C18"
    """
    NeryLab 384_SetB
    """
    SetB_C19 = "SetB-C19"
    """
    NeryLab 384_SetB
    """
    SetB_C2 = "SetB-C2"
    """
    NeryLab 384_SetB
    """
    SetB_C20 = "SetB-C20"
    """
    NeryLab 384_SetB
    """
    SetB_C21 = "SetB-C21"
    """
    NeryLab 384_SetB
    """
    SetB_C22 = "SetB-C22"
    """
    NeryLab 384_SetB
    """
    SetB_C23 = "SetB-C23"
    """
    NeryLab 384_SetB
    """
    SetB_C24 = "SetB-C24"
    """
    NeryLab 384_SetB
    """
    SetB_C3 = "SetB-C3"
    """
    NeryLab 384_SetB
    """
    SetB_C4 = "SetB-C4"
    """
    NeryLab 384_SetB
    """
    SetB_C5 = "SetB-C5"
    """
    NeryLab 384_SetB
    """
    SetB_C6 = "SetB-C6"
    """
    NeryLab 384_SetB
    """
    SetB_C7 = "SetB-C7"
    """
    NeryLab 384_SetB
    """
    SetB_C8 = "SetB-C8"
    """
    NeryLab 384_SetB
    """
    SetB_C9 = "SetB-C9"
    """
    NeryLab 384_SetB
    """
    SetB_D1 = "SetB-D1"
    """
    NeryLab 384_SetB
    """
    SetB_D10 = "SetB-D10"
    """
    NeryLab 384_SetB
    """
    SetB_D11 = "SetB-D11"
    """
    NeryLab 384_SetB
    """
    SetB_D12 = "SetB-D12"
    """
    NeryLab 384_SetB
    """
    SetB_D13 = "SetB-D13"
    """
    NeryLab 384_SetB
    """
    SetB_D14 = "SetB-D14"
    """
    NeryLab 384_SetB
    """
    SetB_D15 = "SetB-D15"
    """
    NeryLab 384_SetB
    """
    SetB_D16 = "SetB-D16"
    """
    NeryLab 384_SetB
    """
    SetB_D17 = "SetB-D17"
    """
    NeryLab 384_SetB
    """
    SetB_D18 = "SetB-D18"
    """
    NeryLab 384_SetB
    """
    SetB_D19 = "SetB-D19"
    """
    NeryLab 384_SetB
    """
    SetB_D2 = "SetB-D2"
    """
    NeryLab 384_SetB
    """
    SetB_D20 = "SetB-D20"
    """
    NeryLab 384_SetB
    """
    SetB_D21 = "SetB-D21"
    """
    NeryLab 384_SetB
    """
    SetB_D22 = "SetB-D22"
    """
    NeryLab 384_SetB
    """
    SetB_D23 = "SetB-D23"
    """
    NeryLab 384_SetB
    """
    SetB_D24 = "SetB-D24"
    """
    NeryLab 384_SetB
    """
    SetB_D3 = "SetB-D3"
    """
    NeryLab 384_SetB
    """
    SetB_D4 = "SetB-D4"
    """
    NeryLab 384_SetB
    """
    SetB_D5 = "SetB-D5"
    """
    NeryLab 384_SetB
    """
    SetB_D6 = "SetB-D6"
    """
    NeryLab 384_SetB
    """
    SetB_D7 = "SetB-D7"
    """
    NeryLab 384_SetB
    """
    SetB_D8 = "SetB-D8"
    """
    NeryLab 384_SetB
    """
    SetB_D9 = "SetB-D9"
    """
    NeryLab 384_SetB
    """
    SetB_E1 = "SetB-E1"
    """
    NeryLab 384_SetB
    """
    SetB_E10 = "SetB-E10"
    """
    NeryLab 384_SetB
    """
    SetB_E11 = "SetB-E11"
    """
    NeryLab 384_SetB
    """
    SetB_E12 = "SetB-E12"
    """
    NeryLab 384_SetB
    """
    SetB_E13 = "SetB-E13"
    """
    NeryLab 384_SetB
    """
    SetB_E14 = "SetB-E14"
    """
    NeryLab 384_SetB
    """
    SetB_E15 = "SetB-E15"
    """
    NeryLab 384_SetB
    """
    SetB_E16 = "SetB-E16"
    """
    NeryLab 384_SetB
    """
    SetB_E17 = "SetB-E17"
    """
    NeryLab 384_SetB
    """
    SetB_E18 = "SetB-E18"
    """
    NeryLab 384_SetB
    """
    SetB_E19 = "SetB-E19"
    """
    NeryLab 384_SetB
    """
    SetB_E2 = "SetB-E2"
    """
    NeryLab 384_SetB
    """
    SetB_E20 = "SetB-E20"
    """
    NeryLab 384_SetB
    """
    SetB_E21 = "SetB-E21"
    """
    NeryLab 384_SetB
    """
    SetB_E22 = "SetB-E22"
    """
    NeryLab 384_SetB
    """
    SetB_E23 = "SetB-E23"
    """
    NeryLab 384_SetB
    """
    SetB_E24 = "SetB-E24"
    """
    NeryLab 384_SetB
    """
    SetB_E3 = "SetB-E3"
    """
    NeryLab 384_SetB
    """
    SetB_E4 = "SetB-E4"
    """
    NeryLab 384_SetB
    """
    SetB_E5 = "SetB-E5"
    """
    NeryLab 384_SetB
    """
    SetB_E6 = "SetB-E6"
    """
    NeryLab 384_SetB
    """
    SetB_E7 = "SetB-E7"
    """
    NeryLab 384_SetB
    """
    SetB_E8 = "SetB-E8"
    """
    NeryLab 384_SetB
    """
    SetB_E9 = "SetB-E9"
    """
    NeryLab 384_SetB
    """
    SetB_F1 = "SetB-F1"
    """
    NeryLab 384_SetB
    """
    SetB_F10 = "SetB-F10"
    """
    NeryLab 384_SetB
    """
    SetB_F11 = "SetB-F11"
    """
    NeryLab 384_SetB
    """
    SetB_F12 = "SetB-F12"
    """
    NeryLab 384_SetB
    """
    SetB_F13 = "SetB-F13"
    """
    NeryLab 384_SetB
    """
    SetB_F14 = "SetB-F14"
    """
    NeryLab 384_SetB
    """
    SetB_F15 = "SetB-F15"
    """
    NeryLab 384_SetB
    """
    SetB_F16 = "SetB-F16"
    """
    NeryLab 384_SetB
    """
    SetB_F17 = "SetB-F17"
    """
    NeryLab 384_SetB
    """
    SetB_F18 = "SetB-F18"
    """
    NeryLab 384_SetB
    """
    SetB_F19 = "SetB-F19"
    """
    NeryLab 384_SetB
    """
    SetB_F2 = "SetB-F2"
    """
    NeryLab 384_SetB
    """
    SetB_F20 = "SetB-F20"
    """
    NeryLab 384_SetB
    """
    SetB_F21 = "SetB-F21"
    """
    NeryLab 384_SetB
    """
    SetB_F22 = "SetB-F22"
    """
    NeryLab 384_SetB
    """
    SetB_F23 = "SetB-F23"
    """
    NeryLab 384_SetB
    """
    SetB_F24 = "SetB-F24"
    """
    NeryLab 384_SetB
    """
    SetB_F3 = "SetB-F3"
    """
    NeryLab 384_SetB
    """
    SetB_F4 = "SetB-F4"
    """
    NeryLab 384_SetB
    """
    SetB_F5 = "SetB-F5"
    """
    NeryLab 384_SetB
    """
    SetB_F6 = "SetB-F6"
    """
    NeryLab 384_SetB
    """
    SetB_F7 = "SetB-F7"
    """
    NeryLab 384_SetB
    """
    SetB_F8 = "SetB-F8"
    """
    NeryLab 384_SetB
    """
    SetB_F9 = "SetB-F9"
    """
    NeryLab 384_SetB
    """
    SetB_G1 = "SetB-G1"
    """
    NeryLab 384_SetB
    """
    SetB_G10 = "SetB-G10"
    """
    NeryLab 384_SetB
    """
    SetB_G11 = "SetB-G11"
    """
    NeryLab 384_SetB
    """
    SetB_G12 = "SetB-G12"
    """
    NeryLab 384_SetB
    """
    SetB_G13 = "SetB-G13"
    """
    NeryLab 384_SetB
    """
    SetB_G14 = "SetB-G14"
    """
    NeryLab 384_SetB
    """
    SetB_G15 = "SetB-G15"
    """
    NeryLab 384_SetB
    """
    SetB_G16 = "SetB-G16"
    """
    NeryLab 384_SetB
    """
    SetB_G17 = "SetB-G17"
    """
    NeryLab 384_SetB
    """
    SetB_G18 = "SetB-G18"
    """
    NeryLab 384_SetB
    """
    SetB_G19 = "SetB-G19"
    """
    NeryLab 384_SetB
    """
    SetB_G2 = "SetB-G2"
    """
    NeryLab 384_SetB
    """
    SetB_G20 = "SetB-G20"
    """
    NeryLab 384_SetB
    """
    SetB_G21 = "SetB-G21"
    """
    NeryLab 384_SetB
    """
    SetB_G22 = "SetB-G22"
    """
    NeryLab 384_SetB
    """
    SetB_G23 = "SetB-G23"
    """
    NeryLab 384_SetB
    """
    SetB_G24 = "SetB-G24"
    """
    NeryLab 384_SetB
    """
    SetB_G3 = "SetB-G3"
    """
    NeryLab 384_SetB
    """
    SetB_G4 = "SetB-G4"
    """
    NeryLab 384_SetB
    """
    SetB_G5 = "SetB-G5"
    """
    NeryLab 384_SetB
    """
    SetB_G6 = "SetB-G6"
    """
    NeryLab 384_SetB
    """
    SetB_G7 = "SetB-G7"
    """
    NeryLab 384_SetB
    """
    SetB_G8 = "SetB-G8"
    """
    NeryLab 384_SetB
    """
    SetB_G9 = "SetB-G9"
    """
    NeryLab 384_SetB
    """
    SetB_H1 = "SetB-H1"
    """
    NeryLab 384_SetB
    """
    SetB_H10 = "SetB-H10"
    """
    NeryLab 384_SetB
    """
    SetB_H11 = "SetB-H11"
    """
    NeryLab 384_SetB
    """
    SetB_H12 = "SetB-H12"
    """
    NeryLab 384_SetB
    """
    SetB_H13 = "SetB-H13"
    """
    NeryLab 384_SetB
    """
    SetB_H14 = "SetB-H14"
    """
    NeryLab 384_SetB
    """
    SetB_H15 = "SetB-H15"
    """
    NeryLab 384_SetB
    """
    SetB_H16 = "SetB-H16"
    """
    NeryLab 384_SetB
    """
    SetB_H17 = "SetB-H17"
    """
    NeryLab 384_SetB
    """
    SetB_H18 = "SetB-H18"
    """
    NeryLab 384_SetB
    """
    SetB_H19 = "SetB-H19"
    """
    NeryLab 384_SetB
    """
    SetB_H2 = "SetB-H2"
    """
    NeryLab 384_SetB
    """
    SetB_H20 = "SetB-H20"
    """
    NeryLab 384_SetB
    """
    SetB_H21 = "SetB-H21"
    """
    NeryLab 384_SetB
    """
    SetB_H22 = "SetB-H22"
    """
    NeryLab 384_SetB
    """
    SetB_H23 = "SetB-H23"
    """
    NeryLab 384_SetB
    """
    SetB_H24 = "SetB-H24"
    """
    NeryLab 384_SetB
    """
    SetB_H3 = "SetB-H3"
    """
    NeryLab 384_SetB
    """
    SetB_H4 = "SetB-H4"
    """
    NeryLab 384_SetB
    """
    SetB_H5 = "SetB-H5"
    """
    NeryLab 384_SetB
    """
    SetB_H6 = "SetB-H6"
    """
    NeryLab 384_SetB
    """
    SetB_H7 = "SetB-H7"
    """
    NeryLab 384_SetB
    """
    SetB_H8 = "SetB-H8"
    """
    NeryLab 384_SetB
    """
    SetB_H9 = "SetB-H9"
    """
    NeryLab 384_SetB
    """
    SetB_I1 = "SetB-I1"
    """
    NeryLab 384_SetB
    """
    SetB_I10 = "SetB-I10"
    """
    NeryLab 384_SetB
    """
    SetB_I11 = "SetB-I11"
    """
    NeryLab 384_SetB
    """
    SetB_I12 = "SetB-I12"
    """
    NeryLab 384_SetB
    """
    SetB_I13 = "SetB-I13"
    """
    NeryLab 384_SetB
    """
    SetB_I14 = "SetB-I14"
    """
    NeryLab 384_SetB
    """
    SetB_I15 = "SetB-I15"
    """
    NeryLab 384_SetB
    """
    SetB_I16 = "SetB-I16"
    """
    NeryLab 384_SetB
    """
    SetB_I17 = "SetB-I17"
    """
    NeryLab 384_SetB
    """
    SetB_I18 = "SetB-I18"
    """
    NeryLab 384_SetB
    """
    SetB_I19 = "SetB-I19"
    """
    NeryLab 384_SetB
    """
    SetB_I2 = "SetB-I2"
    """
    NeryLab 384_SetB
    """
    SetB_I20 = "SetB-I20"
    """
    NeryLab 384_SetB
    """
    SetB_I21 = "SetB-I21"
    """
    NeryLab 384_SetB
    """
    SetB_I22 = "SetB-I22"
    """
    NeryLab 384_SetB
    """
    SetB_I23 = "SetB-I23"
    """
    NeryLab 384_SetB
    """
    SetB_I24 = "SetB-I24"
    """
    NeryLab 384_SetB
    """
    SetB_I3 = "SetB-I3"
    """
    NeryLab 384_SetB
    """
    SetB_I4 = "SetB-I4"
    """
    NeryLab 384_SetB
    """
    SetB_I5 = "SetB-I5"
    """
    NeryLab 384_SetB
    """
    SetB_I6 = "SetB-I6"
    """
    NeryLab 384_SetB
    """
    SetB_I7 = "SetB-I7"
    """
    NeryLab 384_SetB
    """
    SetB_I8 = "SetB-I8"
    """
    NeryLab 384_SetB/#
    """


class Sex(str, Enum):
    number_1 = "1"
    """
    Male
    """
    number_2 = "2"
    """
    Female
    """
    number_7 = "7"
    """
    Other
    """
    number_8 = "8"
    """
    Unknown
    """
    number_9 = "9"
    """
    Not Reported
    """


class AgeAtDeathReferencePoint(str, Enum):
    birth = "birth"
    """
    birth
    """
    conception = "conception"
    """
    conception
    """


class AgeAtDeathUnit(str, Enum):
    days = "days"
    """
    days
    """
    months = "months"
    """
    months
    """
    years = "years"
    """
    years
    """



class OntologyClass(ConfiguredBaseModel):
    """
    a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:OntologyClass',
         'comments': ["This is modeled as a mixin. 'ontology class' should not be the "
                      'primary type of a node in the KG. Instead you should use an '
                      'informative bioloink category, such as AnatomicalEntity (for '
                      'Uberon classes), ChemicalSubstance (for CHEBI or CHEMBL), etc',
                      'Note that formally this is a metaclass. Instances of this class '
                      "are instances in the graph, but can be the object of 'type' "
                      'edges. For example, if we had a node in the graph representing '
                      'a specific brain of a specific patient (e.g brain001), this '
                      'could have a category of bl:Sample, and by typed more '
                      'specifically with an ontology class UBERON:nnn, which has as '
                      'category bl:AnatomicalEntity'],
         'definition_uri': 'https://w3id.org/biolink/vocab/OntologyClass',
         'exact_mappings': ['owl:Class', 'schema:Class'],
         'examples': [{'description': "the class 'brain' from the Uberon anatomy "
                                      'ontology',
                       'value': 'UBERON:0000955'}],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['MESH', 'UMLS', 'KEGG.BRITE'],
         'mixin': True,
         'see_also': ['https://github.com/biolink/biolink-model/issues/486']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })


class Annotation(ConfiguredBaseModel):
    """
    Biolink Model root class for entity annotations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'biolink:Annotation',
         'definition_uri': 'https://w3id.org/biolink/vocab/Annotation',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema'})

    pass


class QuantityValue(Annotation):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:QuantityValue',
         'definition_uri': 'https://w3id.org/biolink/vocab/QuantityValue',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema'})

    has_unit: Optional[str] = Field(default=None, description="""connects a quantity value to a unit""", json_schema_extra = { "linkml_meta": {'alias': 'has_unit',
         'close_mappings': ['EFO:0001697', 'UO-PROPERTY:is_unit_of'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_unit',
         'domain': 'quantity value',
         'domain_of': ['quantity value'],
         'exact_mappings': ['qud:unit', 'IAO:0000039'],
         'in_subset': ['samples'],
         'narrow_mappings': ['SNOMED:has_concentration_strength_denominator_unit',
                             'SNOMED:has_concentration_strength_numerator_unit',
                             'SNOMED:has_presentation_strength_denominator_unit',
                             'SNOMED:has_presentation_strength_numerator_unit',
                             'SNOMED:has_unit_of_presentation'],
         'slot_uri': 'biolink:has_unit'} })
    has_numeric_value: Optional[float] = Field(default=None, description="""connects a quantity value to a number""", json_schema_extra = { "linkml_meta": {'alias': 'has_numeric_value',
         'definition_uri': 'https://w3id.org/biolink/vocab/has_numeric_value',
         'domain': 'quantity value',
         'domain_of': ['quantity value'],
         'exact_mappings': ['qud:quantityValue'],
         'in_subset': ['samples'],
         'slot_uri': 'biolink:has_numeric_value'} })


class Entity(ConfiguredBaseModel):
    """
    Root Biolink Model class for all things and informational relationships, real or imagined.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'biolink:Entity',
         'definition_uri': 'https://w3id.org/biolink/vocab/Entity',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema'})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://w3id.org/biolink/vocab/Entity","biolink:Entity"]] = Field(default=["biolink:Entity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })


class NamedThing(Entity):
    """
    a databased entity or concept/class
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:NamedThing',
         'definition_uri': 'https://w3id.org/biolink/vocab/NamedThing',
         'exact_mappings': ['BFO:0000001',
                            'WIKIDATA:Q35120',
                            'UMLSSG:OBJC',
                            'STY:T071',
                            'dcid:Thing'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema'})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://w3id.org/biolink/vocab/NamedThing","biolink:NamedThing"]] = Field(default=["biolink:NamedThing"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class Attribute(NamedThing, OntologyClass):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Attribute',
         'definition_uri': 'https://w3id.org/biolink/vocab/Attribute',
         'exact_mappings': ['SIO:000614'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['EDAM-DATA', 'EDAM-FORMAT', 'EDAM-OPERATION', 'EDAM-TOPIC'],
         'in_subset': ['samples'],
         'mixins': ['ontology class'],
         'slot_usage': {'name': {'description': "The human-readable 'attribute name' "
                                                'can be set to a string which reflects '
                                                'its context of interpretation, e.g. '
                                                'SEPIO evidence/provenance/confidence '
                                                'annotation or it can default to the '
                                                "name associated with the 'has "
                                                "attribute type' slot ontology term.",
                                 'name': 'name'}}})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    category: list[Literal["https://w3id.org/biolink/vocab/Attribute","biolink:Attribute"]] = Field(default=["biolink:Attribute"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    name: Optional[str] = Field(default=None, description="""The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    has_attribute_type: str = Field(default=..., description="""connects an attribute to a class that describes it""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute_type',
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute_type',
         'domain': 'attribute',
         'domain_of': ['attribute'],
         'in_subset': ['samples'],
         'narrow_mappings': ['LOINC:has_modality_type', 'LOINC:has_view_type'],
         'slot_uri': 'biolink:has_attribute_type'} })
    has_quantitative_value: Optional[list[QuantityValue]] = Field(default=None, description="""connects an attribute to a value""", json_schema_extra = { "linkml_meta": {'alias': 'has_quantitative_value',
         'definition_uri': 'https://w3id.org/biolink/vocab/has_quantitative_value',
         'domain': 'attribute',
         'domain_of': ['attribute'],
         'exact_mappings': ['qud:quantityValue'],
         'in_subset': ['samples'],
         'narrow_mappings': ['SNOMED:has_concentration_strength_numerator_value',
                             'SNOMED:has_presentation_strength_denominator_value',
                             'SNOMED:has_presentation_strength_numerator_value'],
         'slot_uri': 'biolink:has_quantitative_value'} })
    has_qualitative_value: Optional[str] = Field(default=None, description="""connects an attribute to a value""", json_schema_extra = { "linkml_meta": {'alias': 'has_qualitative_value',
         'definition_uri': 'https://w3id.org/biolink/vocab/has_qualitative_value',
         'domain': 'attribute',
         'domain_of': ['attribute'],
         'in_subset': ['samples'],
         'slot_uri': 'biolink:has_qualitative_value'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })


class TaxonomicRank(OntologyClass):
    """
    A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:TaxonomicRank',
         'definition_uri': 'https://w3id.org/biolink/vocab/TaxonomicRank',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['TAXRANK'],
         'mappings': ['WIKIDATA:Q427626']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })


class OrganismTaxon(NamedThing):
    """
    A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['taxon', 'taxonomic classification'],
         'class_uri': 'biolink:OrganismTaxon',
         'definition_uri': 'https://w3id.org/biolink/vocab/OrganismTaxon',
         'exact_mappings': ['WIKIDATA:Q16521', 'STY:T001', 'bioschemas:Taxon'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['NCBITaxon', 'MESH', 'UMLS'],
         'in_subset': ['model_organism_database'],
         'narrow_mappings': ['dcid:BiologicalSpecies'],
         'values_from': ['NCBITaxon']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://w3id.org/biolink/vocab/OrganismTaxon","biolink:OrganismTaxon"]] = Field(default=["biolink:OrganismTaxon"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    has_taxonomic_rank: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_taxonomic_rank',
         'definition_uri': 'https://w3id.org/biolink/vocab/has_taxonomic_rank',
         'domain': 'named thing',
         'domain_of': ['organism taxon'],
         'is_a': 'node property',
         'mappings': ['WIKIDATA:P105'],
         'slot_uri': 'biolink:has_taxonomic_rank'} })


class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some topic of discourse or is used as support.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'aliases': ['information', 'information artefact', 'information entity'],
         'class_uri': 'biolink:InformationContentEntity',
         'definition_uri': 'https://w3id.org/biolink/vocab/InformationContentEntity',
         'exact_mappings': ['IAO:0000030'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['doi'],
         'narrow_mappings': ['UMLSSG:CONC',
                             'STY:T077',
                             'STY:T078',
                             'STY:T079',
                             'STY:T080',
                             'STY:T081',
                             'STY:T082',
                             'STY:T089',
                             'STY:T102',
                             'STY:T169',
                             'STY:T171',
                             'STY:T185']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://w3id.org/biolink/vocab/InformationContentEntity","biolink:InformationContentEntity"]] = Field(default=["biolink:InformationContentEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    license: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'license',
         'definition_uri': 'https://w3id.org/biolink/vocab/license',
         'domain': 'information content entity',
         'domain_of': ['information content entity', 'dataset'],
         'exact_mappings': ['dct:license'],
         'is_a': 'node property',
         'narrow_mappings': ['WIKIDATA_PROPERTY:P275'],
         'slot_uri': 'biolink:license'} })
    rights: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'rights',
         'definition_uri': 'https://w3id.org/biolink/vocab/rights',
         'domain': 'information content entity',
         'domain_of': ['information content entity', 'dataset'],
         'exact_mappings': ['dct:rights'],
         'is_a': 'node property',
         'slot_uri': 'biolink:rights'} })
    format: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'format',
         'definition_uri': 'https://w3id.org/biolink/vocab/format',
         'domain': 'information content entity',
         'domain_of': ['information content entity', 'dataset'],
         'exact_mappings': ['dct:format', 'WIKIDATA_PROPERTY:P2701'],
         'is_a': 'node property',
         'slot_uri': 'biolink:format'} })
    creation_date: Optional[date] = Field(default=None, description="""date on which an entity was created. This can be applied to nodes or edges""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date',
         'aliases': ['publication date'],
         'definition_uri': 'https://w3id.org/biolink/vocab/creation_date',
         'domain': 'named thing',
         'domain_of': ['information content entity', 'dataset'],
         'exact_mappings': ['dct:createdOn', 'WIKIDATA_PROPERTY:P577'],
         'is_a': 'node property',
         'slot_uri': 'biolink:creation_date'} })


class Dataset(InformationContentEntity):
    """
    an item that refers to a collection of data from a data source.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Dataset',
         'definition_uri': 'https://w3id.org/biolink/vocab/Dataset',
         'exact_mappings': ['IAO:0000100',
                            'dctypes:Dataset',
                            'schema:dataset',
                            'dcid:Dataset'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema'})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://w3id.org/biolink/vocab/Dataset","biolink:Dataset"]] = Field(default=["biolink:Dataset"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    license: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'license',
         'definition_uri': 'https://w3id.org/biolink/vocab/license',
         'domain': 'information content entity',
         'domain_of': ['information content entity', 'dataset'],
         'exact_mappings': ['dct:license'],
         'is_a': 'node property',
         'narrow_mappings': ['WIKIDATA_PROPERTY:P275'],
         'slot_uri': 'biolink:license'} })
    rights: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'rights',
         'definition_uri': 'https://w3id.org/biolink/vocab/rights',
         'domain': 'information content entity',
         'domain_of': ['information content entity', 'dataset'],
         'exact_mappings': ['dct:rights'],
         'is_a': 'node property',
         'slot_uri': 'biolink:rights'} })
    format: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'format',
         'definition_uri': 'https://w3id.org/biolink/vocab/format',
         'domain': 'information content entity',
         'domain_of': ['information content entity', 'dataset'],
         'exact_mappings': ['dct:format', 'WIKIDATA_PROPERTY:P2701'],
         'is_a': 'node property',
         'slot_uri': 'biolink:format'} })
    creation_date: Optional[date] = Field(default=None, description="""date on which an entity was created. This can be applied to nodes or edges""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date',
         'aliases': ['publication date'],
         'definition_uri': 'https://w3id.org/biolink/vocab/creation_date',
         'domain': 'named thing',
         'domain_of': ['information content entity', 'dataset'],
         'exact_mappings': ['dct:createdOn', 'WIKIDATA_PROPERTY:P577'],
         'is_a': 'node property',
         'slot_uri': 'biolink:creation_date'} })


class PhysicalEssenceOrOccurrent(ConfiguredBaseModel):
    """
    Either a physical or processual entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:PhysicalEssenceOrOccurrent',
         'definition_uri': 'https://w3id.org/biolink/vocab/PhysicalEssenceOrOccurrent',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixin': True})

    pass


class PhysicalEssence(PhysicalEssenceOrOccurrent):
    """
    Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:PhysicalEssence',
         'definition_uri': 'https://w3id.org/biolink/vocab/PhysicalEssence',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixin': True})

    pass


class PhysicalEntity(PhysicalEssence, NamedThing):
    """
    An entity that has material reality (a.k.a. physical essence).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:PhysicalEntity',
         'definition_uri': 'https://w3id.org/biolink/vocab/PhysicalEntity',
         'exact_mappings': ['STY:T072'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixins': ['physical essence'],
         'narrow_mappings': ['STY:T073']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://w3id.org/biolink/vocab/PhysicalEntity","biolink:PhysicalEntity"]] = Field(default=["biolink:PhysicalEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class Occurrent(PhysicalEssenceOrOccurrent):
    """
    A processual entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Occurrent',
         'definition_uri': 'https://w3id.org/biolink/vocab/Occurrent',
         'exact_mappings': ['BFO:0000003'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixin': True})

    pass


class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:ActivityAndBehavior',
         'definition_uri': 'https://w3id.org/biolink/vocab/ActivityAndBehavior',
         'exact_mappings': ['UMLSSG:ACTI'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixin': True})

    pass


class Activity(ActivityAndBehavior, NamedThing):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Activity',
         'definition_uri': 'https://w3id.org/biolink/vocab/Activity',
         'exact_mappings': ['prov:Activity', 'NCIT:C43431', 'STY:T052'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixins': ['activity and behavior'],
         'narrow_mappings': ['STY:T056',
                             'STY:T057',
                             'STY:T064',
                             'STY:T066',
                             'STY:T062',
                             'STY:T065',
                             'STY:T058']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://w3id.org/biolink/vocab/Activity","biolink:Activity"]] = Field(default=["biolink:Activity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class Procedure(ActivityAndBehavior, NamedThing):
    """
    A series of actions conducted in a certain order or manner
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Procedure',
         'definition_uri': 'https://w3id.org/biolink/vocab/Procedure',
         'exact_mappings': ['UMLSSG:PROC', 'dcid:MedicalProcedure'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['CPT'],
         'mixins': ['activity and behavior'],
         'narrow_mappings': ['STY:T059', 'STY:T060', 'STY:T061', 'STY:T063']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://w3id.org/biolink/vocab/Procedure","biolink:Procedure"]] = Field(default=["biolink:Procedure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class SubjectOfInvestigation(ConfiguredBaseModel):
    """
    An entity that has the role of being studied in an investigation, study, or experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:SubjectOfInvestigation',
         'definition_uri': 'https://w3id.org/biolink/vocab/SubjectOfInvestigation',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixin': True})

    pass


class MaterialSample(SubjectOfInvestigation, PhysicalEntity):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['biospecimen', 'sample', 'biosample', 'physical sample'],
         'class_uri': 'biolink:MaterialSample',
         'definition_uri': 'https://w3id.org/biolink/vocab/MaterialSample',
         'exact_mappings': ['OBI:0000747', 'SIO:001050'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['BIOSAMPLE', 'GOLD.META'],
         'mixins': ['subject of investigation']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://w3id.org/biolink/vocab/MaterialSample","biolink:MaterialSample"]] = Field(default=["biolink:MaterialSample"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class ThingWithTaxon(ConfiguredBaseModel):
    """
    A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:ThingWithTaxon',
         'definition_uri': 'https://w3id.org/biolink/vocab/ThingWithTaxon',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixin': True})

    in_taxon: Optional[list[str]] = Field(default=None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""", json_schema_extra = { "linkml_meta": {'alias': 'in_taxon',
         'aliases': ['instance of',
                     'is organism source of gene product',
                     'organism has gene',
                     'gene found in organism',
                     'gene product has organism source'],
         'annotations': {'canonical_predicate': {'tag': 'canonical_predicate',
                                                 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['RO:0002162', 'WIKIDATA_PROPERTY:P703'],
         'in_subset': ['translator_minimal'],
         'inherited': True,
         'is_a': 'related to at instance level',
         'narrow_mappings': ['RO:0002160'],
         'slot_uri': 'biolink:in_taxon'} })
    in_taxon_label: Optional[str] = Field(default=None, description="""The human readable scientific name for the taxon of the entity.""", json_schema_extra = { "linkml_meta": {'alias': 'in_taxon_label',
         'annotations': {'denormalized': {'tag': 'denormalized', 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon_label',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P225'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'slot_uri': 'biolink:in_taxon_label'} })


class BiologicalEntity(ThingWithTaxon, NamedThing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'aliases': ['bioentity'],
         'class_uri': 'biolink:BiologicalEntity',
         'definition_uri': 'https://w3id.org/biolink/vocab/BiologicalEntity',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixins': ['thing with taxon'],
         'narrow_mappings': ['WIKIDATA:Q28845870',
                             'STY:T050',
                             'SIO:010046',
                             'STY:T129']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://w3id.org/biolink/vocab/BiologicalEntity","biolink:BiologicalEntity"]] = Field(default=["biolink:BiologicalEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    in_taxon: Optional[list[str]] = Field(default=None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""", json_schema_extra = { "linkml_meta": {'alias': 'in_taxon',
         'aliases': ['instance of',
                     'is organism source of gene product',
                     'organism has gene',
                     'gene found in organism',
                     'gene product has organism source'],
         'annotations': {'canonical_predicate': {'tag': 'canonical_predicate',
                                                 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['RO:0002162', 'WIKIDATA_PROPERTY:P703'],
         'in_subset': ['translator_minimal'],
         'inherited': True,
         'is_a': 'related to at instance level',
         'narrow_mappings': ['RO:0002160'],
         'slot_uri': 'biolink:in_taxon'} })
    in_taxon_label: Optional[str] = Field(default=None, description="""The human readable scientific name for the taxon of the entity.""", json_schema_extra = { "linkml_meta": {'alias': 'in_taxon_label',
         'annotations': {'denormalized': {'tag': 'denormalized', 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon_label',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P225'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'slot_uri': 'biolink:in_taxon_label'} })


class GenomicEntity(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:GenomicEntity',
         'definition_uri': 'https://w3id.org/biolink/vocab/GenomicEntity',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'in_subset': ['translator_minimal'],
         'mixin': True,
         'narrow_mappings': ['STY:T028', 'GENO:0000897']})

    has_biological_sequence: Optional[str] = Field(default=None, description="""connects a genomic feature to its sequence""", json_schema_extra = { "linkml_meta": {'alias': 'has_biological_sequence',
         'definition_uri': 'https://w3id.org/biolink/vocab/has_biological_sequence',
         'domain': 'named thing',
         'domain_of': ['genomic entity', 'gene', 'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:has_biological_sequence'} })


class ChemicalEntityOrGeneOrGeneProduct(ConfiguredBaseModel):
    """
    A union of chemical entities and children, and gene or gene product. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:ChemicalEntityOrGeneOrGeneProduct',
         'definition_uri': 'https://w3id.org/biolink/vocab/ChemicalEntityOrGeneOrGeneProduct',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixin': True})

    pass


class MacromolecularMachineMixin(ConfiguredBaseModel):
    """
    A union of gene locus, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:MacromolecularMachineMixin',
         'definition_uri': 'https://w3id.org/biolink/vocab/MacromolecularMachineMixin',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixin': True})

    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })


class GeneOrGeneProduct(MacromolecularMachineMixin):
    """
    A union of gene loci or gene products. Frequently an identifier for one will be used as proxy for another
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:GeneOrGeneProduct',
         'definition_uri': 'https://w3id.org/biolink/vocab/GeneOrGeneProduct',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['CHEMBL.TARGET', 'IUPHAR.FAMILY'],
         'mixin': True})

    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })


class Gene(GeneOrGeneProduct, ChemicalEntityOrGeneOrGeneProduct, GenomicEntity, BiologicalEntity, PhysicalEssence, OntologyClass):
    """
    A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['NCIT:C45822'],
         'class_uri': 'biolink:Gene',
         'definition_uri': 'https://w3id.org/biolink/vocab/Gene',
         'exact_mappings': ['SO:0000704', 'SIO:010035', 'WIKIDATA:Q7187', 'dcid:Gene'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['NCBIGene',
                         'ENSEMBL',
                         'HGNC',
                         'MGI',
                         'ZFIN',
                         'dictyBase',
                         'WB',
                         'WormBase',
                         'FB',
                         'RGD',
                         'SGD',
                         'PomBase',
                         'OMIM',
                         'KEGG.GENES',
                         'UMLS',
                         'Xenbase',
                         'AspGD',
                         'PHARMGKB.GENE'],
         'in_subset': ['translator_minimal', 'model_organism_database'],
         'mixins': ['gene or gene product',
                    'genomic entity',
                    'chemical entity or gene or gene product',
                    'physical essence',
                    'ontology class'],
         'narrow_mappings': ['bioschemas:gene']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://w3id.org/biolink/vocab/Gene","biolink:Gene"]] = Field(default=["biolink:Gene"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    in_taxon: Optional[list[str]] = Field(default=None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""", json_schema_extra = { "linkml_meta": {'alias': 'in_taxon',
         'aliases': ['instance of',
                     'is organism source of gene product',
                     'organism has gene',
                     'gene found in organism',
                     'gene product has organism source'],
         'annotations': {'canonical_predicate': {'tag': 'canonical_predicate',
                                                 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['RO:0002162', 'WIKIDATA_PROPERTY:P703'],
         'in_subset': ['translator_minimal'],
         'inherited': True,
         'is_a': 'related to at instance level',
         'narrow_mappings': ['RO:0002160'],
         'slot_uri': 'biolink:in_taxon'} })
    in_taxon_label: Optional[str] = Field(default=None, description="""The human readable scientific name for the taxon of the entity.""", json_schema_extra = { "linkml_meta": {'alias': 'in_taxon_label',
         'annotations': {'denormalized': {'tag': 'denormalized', 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon_label',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P225'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'slot_uri': 'biolink:in_taxon_label'} })
    symbol: Optional[str] = Field(default=None, description="""Symbol for a particular thing""", json_schema_extra = { "linkml_meta": {'alias': 'symbol',
         'definition_uri': 'https://w3id.org/biolink/vocab/symbol',
         'domain': 'named thing',
         'domain_of': ['gene'],
         'exact_mappings': ['AGRKB:symbol', 'gpi:DB_Object_Symbol'],
         'is_a': 'node property',
         'slot_uri': 'biolink:symbol'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    has_biological_sequence: Optional[str] = Field(default=None, description="""connects a genomic feature to its sequence""", json_schema_extra = { "linkml_meta": {'alias': 'has_biological_sequence',
         'definition_uri': 'https://w3id.org/biolink/vocab/has_biological_sequence',
         'domain': 'named thing',
         'domain_of': ['genomic entity', 'gene', 'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:has_biological_sequence'} })


class Genome(GenomicEntity, BiologicalEntity, PhysicalEssence, OntologyClass):
    """
    A genome is the sum of genetic material within a cell or virion.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Genome',
         'close_mappings': ['dcid:GenomeAssemblyUnit'],
         'definition_uri': 'https://w3id.org/biolink/vocab/Genome',
         'exact_mappings': ['SO:0001026', 'SIO:000984', 'WIKIDATA:Q7020'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'in_subset': ['model_organism_database'],
         'mixins': ['genomic entity', 'physical essence', 'ontology class']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://w3id.org/biolink/vocab/Genome","biolink:Genome"]] = Field(default=["biolink:Genome"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    in_taxon: Optional[list[str]] = Field(default=None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""", json_schema_extra = { "linkml_meta": {'alias': 'in_taxon',
         'aliases': ['instance of',
                     'is organism source of gene product',
                     'organism has gene',
                     'gene found in organism',
                     'gene product has organism source'],
         'annotations': {'canonical_predicate': {'tag': 'canonical_predicate',
                                                 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['RO:0002162', 'WIKIDATA_PROPERTY:P703'],
         'in_subset': ['translator_minimal'],
         'inherited': True,
         'is_a': 'related to at instance level',
         'narrow_mappings': ['RO:0002160'],
         'slot_uri': 'biolink:in_taxon'} })
    in_taxon_label: Optional[str] = Field(default=None, description="""The human readable scientific name for the taxon of the entity.""", json_schema_extra = { "linkml_meta": {'alias': 'in_taxon_label',
         'annotations': {'denormalized': {'tag': 'denormalized', 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon_label',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P225'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'slot_uri': 'biolink:in_taxon_label'} })
    has_biological_sequence: Optional[str] = Field(default=None, description="""connects a genomic feature to its sequence""", json_schema_extra = { "linkml_meta": {'alias': 'has_biological_sequence',
         'definition_uri': 'https://w3id.org/biolink/vocab/has_biological_sequence',
         'domain': 'named thing',
         'domain_of': ['genomic entity', 'gene', 'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:has_biological_sequence'} })


class VersionedNamedThing(NamedThing):
    """
    An iteration of the biolink:NamedThing class that stores metadata about the object's version.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://identifiers.org/brain-bican/bican-core-schema',
         'slot_usage': {'version': {'name': 'version', 'required': True}}})

    version: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'version',
         'broad_mappings': ['pav:version', 'owl:versionInfo'],
         'definition_uri': 'https://w3id.org/biolink/vocab/version',
         'domain': 'dataset',
         'domain_of': ['VersionedNamedThing'],
         'is_a': 'node property',
         'slot_uri': 'biolink:version'} })
    revision_of: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'revision_of', 'domain_of': ['VersionedNamedThing']} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/VersionedNamedThing","bican:VersionedNamedThing"]] = Field(default=["bican:VersionedNamedThing"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class Checksum(Entity):
    """
    Checksum values associated with digital entities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://identifiers.org/brain-bican/bican-core-schema'})

    checksum_algorithm: Optional[DigestType] = Field(default=None, description="""The type of cryptographic hash function used to calculate the checksum value.""", json_schema_extra = { "linkml_meta": {'alias': 'checksum_algorithm', 'domain_of': ['checksum']} })
    value: Optional[str] = Field(default=None, description="""The checksum value obtained from a specific cryotographic hash function.""", json_schema_extra = { "linkml_meta": {'alias': 'value', 'domain_of': ['checksum']} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/Checksum","bican:Checksum"]] = Field(default=["bican:Checksum"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })


class ProvActivity(ConfiguredBaseModel):
    """
    An activity is something that occurs over a period of time and acts upon or with entities;  it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Activity',
         'from_schema': 'https://identifiers.org/brain-bican/bican-prov-schema',
         'mixin': True})

    used: Optional[str] = Field(default=None, description="""Usage is the beginning of utilizing an entity by an activity. Before usage, the activity had not begun to utilize this entity and could not have been affected by the entity.""", json_schema_extra = { "linkml_meta": {'alias': 'used',
         'domain_of': ['ProvActivity',
                       'DissectionRoiDelineation',
                       'TissueDissection',
                       'CellDissociation',
                       'CellEnrichment',
                       'EnrichedCellSampleSplitting',
                       'CellBarcoding',
                       'CdnaAmplification',
                       'LibraryConstruction',
                       'LibraryPooling'],
         'slot_uri': 'prov:used'} })


class ProvEntity(ConfiguredBaseModel):
    """
    An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects;  entities may be real or imaginary.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Entity',
         'from_schema': 'https://identifiers.org/brain-bican/bican-prov-schema',
         'mixin': True})

    was_derived_from: Optional[str] = Field(default=None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'domain_of': ['ProvEntity',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DigitalAsset'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    was_generated_by: Optional[str] = Field(default=None, description="""Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['ProvEntity',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'slot_uri': 'prov:wasGeneratedBy'} })


class Donor(ProvEntity, ThingWithTaxon, PhysicalEntity):
    """
    A person or organism that is the source of a biological sample for scientific study.  Many biological samples are generated from a single donor.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['NIMP:Donor'],
         'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'mixins': ['thing with taxon', 'ProvEntity'],
         'slot_usage': {'name': {'description': 'Name of person or organism that is '
                                                'the source of a biological sample for '
                                                'scientific study.  Many biological '
                                                'samples are generated from a single '
                                                'donor.',
                                 'from_schema': 'bican_biolink',
                                 'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                                          'local_name_value': 'donor_local_id'}},
                                 'name': 'name'}}})

    name: Optional[str] = Field(default=None, description="""Name of person or organism that is the source of a biological sample for scientific study.  Many biological samples are generated from a single donor.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'donor_local_id'}},
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    biological_sex: Optional[Sex] = Field(default=None, description="""Biological sex of donor at birth""", json_schema_extra = { "linkml_meta": {'alias': 'biological_sex',
         'domain_of': ['Donor'],
         'exact_mappings': ['NIMP:PD-LXUBTM45'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'sex'}},
         'slot_uri': 'bican:632d3d3f-f85b-4efc-a1ab-010fe417ae81'} })
    age_at_death_description: Optional[str] = Field(default=None, description="""Text description of the age of death following typical scientific convention for the species or developmental stage. For example: P56, E11.5""", json_schema_extra = { "linkml_meta": {'alias': 'age_at_death_description',
         'domain_of': ['Donor'],
         'exact_mappings': ['NIMP:PD-ZJZJLE33'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'age_at_death_description'}},
         'slot_uri': 'bican:0630a265-4a63-48f4-8853-66b929002306'} })
    age_at_death_reference_point: Optional[AgeAtDeathReferencePoint] = Field(default=None, description="""The reference point for an age interval; for example, birth or conception.""", json_schema_extra = { "linkml_meta": {'alias': 'age_at_death_reference_point',
         'domain_of': ['Donor'],
         'exact_mappings': ['NIMP:PD-RARAGG39'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'age_at_death_reference_point'}},
         'slot_uri': 'bican:3bed1f94-9d82-4ed7-afdf-79d896b24dbb'} })
    age_at_death_unit: Optional[AgeAtDeathUnit] = Field(default=None, description="""The unit used for representing the donor age from the reference point.""", json_schema_extra = { "linkml_meta": {'alias': 'age_at_death_unit',
         'domain_of': ['Donor'],
         'exact_mappings': ['NIMP:PD-AVAVEV39'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'age_at_death_unit'}},
         'slot_uri': 'bican:b5436e99-f0a7-4c30-825d-56b88ee2ac1d'} })
    age_at_death_value: Optional[float] = Field(default=None, description="""The value representing the donor age from the reference point.""", json_schema_extra = { "linkml_meta": {'alias': 'age_at_death_value',
         'domain_of': ['Donor'],
         'exact_mappings': ['NIMP:PD-FTFTCP24'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'age_at_death'}},
         'slot_uri': 'bican:57e24d3c-c9c7-4ef3-9809-a35802d563ec'} })
    donor_species: Optional[str] = Field(default=None, description="""Species of donor.""", json_schema_extra = { "linkml_meta": {'alias': 'donor_species',
         'domain_of': ['Donor'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'donor_species'}},
         'slot_uri': 'bican:6837cb02-6bd7-4fb8-838c-9062ead96ba4'} })
    in_taxon: Optional[list[str]] = Field(default=None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""", json_schema_extra = { "linkml_meta": {'alias': 'in_taxon',
         'aliases': ['instance of',
                     'is organism source of gene product',
                     'organism has gene',
                     'gene found in organism',
                     'gene product has organism source'],
         'annotations': {'canonical_predicate': {'tag': 'canonical_predicate',
                                                 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['RO:0002162', 'WIKIDATA_PROPERTY:P703'],
         'in_subset': ['translator_minimal'],
         'inherited': True,
         'is_a': 'related to at instance level',
         'narrow_mappings': ['RO:0002160'],
         'slot_uri': 'biolink:in_taxon'} })
    in_taxon_label: Optional[str] = Field(default=None, description="""The human readable scientific name for the taxon of the entity.""", json_schema_extra = { "linkml_meta": {'alias': 'in_taxon_label',
         'annotations': {'denormalized': {'tag': 'denormalized', 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon_label',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P225'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'slot_uri': 'biolink:in_taxon_label'} })
    was_derived_from: Optional[str] = Field(default=None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'domain_of': ['ProvEntity',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DigitalAsset'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    was_generated_by: Optional[str] = Field(default=None, description="""Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['ProvEntity',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/Donor","bican:Donor"]] = Field(default=["bican:Donor"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class BrainSlab(ProvEntity, MaterialSample):
    """
    A thick flat piece of brain tissue obtained by slicing a whole brain, brain hemisphere or subdivision with a blade at regular interval.  When multiple brain slabs are obtained from the slicing process, an ordinal is assigned to provide information about the relative positioning of the slabs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['NIMP:Slab'],
         'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'tissue_specimen'],
         'mixins': ['ProvEntity'],
         'slot_usage': {'name': {'description': 'Name of a thick flat piece of brain '
                                                'tissue obtained by slicing a whole '
                                                'brain, brain hemisphere or '
                                                'subdivision with a blade at regular '
                                                'interval.  When multiple brain slabs '
                                                'are obtained from the slicing '
                                                'process, an ordinal is assigned to '
                                                'provide information about the '
                                                'relative positioning of the slabs.',
                                 'from_schema': 'bican_biolink',
                                 'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                                          'local_name_value': 'local_name'}},
                                 'name': 'name'},
                        'was_derived_from': {'any_of': [{'range': 'Donor'},
                                                        {'range': 'BrainSlab'}],
                                             'description': 'The donor from which the '
                                                            'brain slab was derived '
                                                            'from.',
                                             'exact_mappings': ['NIMP:has_parent'],
                                             'from_schema': 'bican_prov',
                                             'name': 'was_derived_from'}}})

    was_derived_from: Optional[str] = Field(default=None, description="""The donor from which the brain slab was derived from.""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'any_of': [{'range': 'Donor'}, {'range': 'BrainSlab'}],
         'domain_of': ['ProvEntity',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DigitalAsset'],
         'exact_mappings': ['NIMP:has_parent'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    name: Optional[str] = Field(default=None, description="""Name of a thick flat piece of brain tissue obtained by slicing a whole brain, brain hemisphere or subdivision with a blade at regular interval.  When multiple brain slabs are obtained from the slicing process, an ordinal is assigned to provide information about the relative positioning of the slabs.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'local_name'}},
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    was_generated_by: Optional[str] = Field(default=None, description="""Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['ProvEntity',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/BrainSlab","bican:BrainSlab"]] = Field(default=["bican:BrainSlab"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class TissueSample(ProvEntity, MaterialSample):
    """
    The final intact piece of tissue before cell or nuclei prep. This piece of tissue will be used in dissociation and has an region of interest polygon (ROI) associated with it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['NIMP:Tissue'],
         'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'library_generation'],
         'mixins': ['ProvEntity'],
         'slot_usage': {'name': {'description': 'Identifier name for final intact '
                                                'piece of tissue before cell or nuclei '
                                                'prep.  This piece of tissue will be '
                                                'used in dissociation and has an ROI '
                                                'associated with it.',
                                 'exact_mappings': ['NIMP:PD-LJCRCC35'],
                                 'from_schema': 'bican_biolink',
                                 'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                                          'local_name_value': 'tissue_sample_local_name'}},
                                 'name': 'name',
                                 'slot_uri': 'bican:2e4ca2fc-2d77-4d19-af45-d0fb7bbc2269'},
                        'was_derived_from': {'description': 'The donor or brain slab '
                                                            'from which the tissue '
                                                            'sample was derived from.',
                                             'exact_mappings': ['NIMP:has_parent'],
                                             'from_schema': 'bican_prov',
                                             'name': 'was_derived_from',
                                             'range': 'Donor'},
                        'was_generated_by': {'description': 'The dissection process '
                                                            'from which the tissue '
                                                            'sample was generated by.',
                                             'from_schema': 'bican_prov',
                                             'name': 'was_generated_by',
                                             'range': 'TissueDissection'}}})

    was_derived_from: Optional[str] = Field(default=None, description="""The donor or brain slab from which the tissue sample was derived from.""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'domain_of': ['ProvEntity',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DigitalAsset'],
         'exact_mappings': ['NIMP:has_parent'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    was_generated_by: Optional[str] = Field(default=None, description="""The dissection process from which the tissue sample was generated by.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['ProvEntity',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    name: Optional[str] = Field(default=None, description="""Identifier name for final intact piece of tissue before cell or nuclei prep.  This piece of tissue will be used in dissociation and has an ROI associated with it.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['NIMP:PD-LJCRCC35'],
         'in_subset': ['translator_minimal', 'samples'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'tissue_sample_local_name'}},
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'bican:2e4ca2fc-2d77-4d19-af45-d0fb7bbc2269'} })
    dissection_was_guided_by: Optional[str] = Field(default=None, description="""The dissection ROI polygon that was used to guide the dissection.""", json_schema_extra = { "linkml_meta": {'alias': 'dissection_was_guided_by',
         'domain_of': ['TissueSample'],
         'exact_mappings': ['NIMP:has_parent']} })
    tissue_sample_structure: Optional[list[str]] = Field(default=None, description="""Structure of tissue sample.""", json_schema_extra = { "linkml_meta": {'alias': 'tissue_sample_structure',
         'domain_of': ['TissueSample'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'structure'}}} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/TissueSample","bican:TissueSample"]] = Field(default=["bican:TissueSample"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class DissociatedCellSample(ProvEntity, MaterialSample):
    """
    A collection of dissociated cells or nuclei derived from dissociation of a tissue sample.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['NIMP:Dissociated%20Cell%20Sample'],
         'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'library_generation'],
         'mixins': ['ProvEntity'],
         'slot_usage': {'name': {'description': 'Name of a collection of dissociated '
                                                'cells or nuclei derived from '
                                                'dissociation of a tissue sample.',
                                 'exact_mappings': ['NIMP:PD-RQRWHS40'],
                                 'from_schema': 'bican_biolink',
                                 'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                                          'local_name_value': 'dissociated_cell_sample_local_name'}},
                                 'name': 'name',
                                 'slot_uri': 'bican:65e2c7da-9eb4-45b2-8ccb-d69ef9785ee2'},
                        'was_derived_from': {'description': 'The input tissue '
                                                            'sample(s) from which '
                                                            'dissociated cell sample '
                                                            'was derived from.',
                                             'exact_mappings': ['NIMP:has_parent'],
                                             'from_schema': 'bican_prov',
                                             'multivalued': True,
                                             'name': 'was_derived_from',
                                             'range': 'TissueSample'},
                        'was_generated_by': {'description': 'The cell dissociation '
                                                            'process from which the '
                                                            'dissociated cell sample '
                                                            'was generated by.',
                                             'from_schema': 'bican_prov',
                                             'name': 'was_generated_by',
                                             'range': 'CellDissociation'}}})

    was_generated_by: Optional[str] = Field(default=None, description="""The cell dissociation process from which the dissociated cell sample was generated by.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['ProvEntity',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    was_derived_from: Optional[list[str]] = Field(default=None, description="""The input tissue sample(s) from which dissociated cell sample was derived from.""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'domain_of': ['ProvEntity',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DigitalAsset'],
         'exact_mappings': ['NIMP:has_parent'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    name: Optional[str] = Field(default=None, description="""Name of a collection of dissociated cells or nuclei derived from dissociation of a tissue sample.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['NIMP:PD-RQRWHS40'],
         'in_subset': ['translator_minimal', 'samples'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'dissociated_cell_sample_local_name'}},
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'bican:65e2c7da-9eb4-45b2-8ccb-d69ef9785ee2'} })
    dissociated_cell_sample_cell_prep_type: Optional[DissociatedCellSampleCellPrepType] = Field(default=None, description="""The type of cell preparation. For example: Cells, Nuclei. This is a property of dissociated_cell_sample.""", json_schema_extra = { "linkml_meta": {'alias': 'dissociated cell sample cell prep type',
         'domain_of': ['DissociatedCellSample'],
         'exact_mappings': ['NIMP:PD-RELLGO26'],
         'in_subset': ['analysis', 'tracking'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'dissociated_cell_sample_cell_prep_type'}},
         'slot_uri': 'bican:baae4ac3-f959-4594-b943-3a82ec19bd34'} })
    dissociated_cell_oligo_tag_name: Optional[DissociatedCellSampleCellLabelBarcode] = Field(default=None, description="""Name of cell source oligo used in cell plexing.  The oligo molecularly tags all the cells in the dissociated cell sample and allows separate dissociated cell samples to be combined downstream in the barcoded cell sample.  The oligo name is associated with a sequence in a lookup table.  This sequence will be needed during alignment to associate reads with the parent source dissociated cell sample.""", json_schema_extra = { "linkml_meta": {'alias': 'dissociated cell oligo tag name',
         'domain_of': ['DissociatedCellSample', 'EnrichedCellSample'],
         'exact_mappings': ['NIMP:PD-CFCFPS27'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'dissociated_cell_sample_cell_label_barcode'}},
         'slot_uri': 'bican:184abbaf-baff-4b5f-b51e-dd38de6006af'} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/DissociatedCellSample","bican:DissociatedCellSample"]] = Field(default=["bican:DissociatedCellSample"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class EnrichedCellSample(ProvEntity, MaterialSample):
    """
    A collection of enriched cells or nuclei after enrichment process, usually via fluorescence-activated cell sorting (FACS) using the enrichment plan, is applied to dissociated cell sample.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['NIMP:Enriched%20Cell%20Sample'],
         'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'library_generation'],
         'mixins': ['ProvEntity'],
         'slot_usage': {'name': {'description': 'Name of collection of enriched cells '
                                                'or nuclei after enrichment process '
                                                '(usually via FACS using the '
                                                'Enrichment Plan) applied to '
                                                'dissociated_cell_sample.',
                                 'exact_mappings': ['NIMP:PD-BERWTM41'],
                                 'from_schema': 'bican_biolink',
                                 'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                                          'local_name_value': 'enriched_cell_sample_local_name'}},
                                 'name': 'name',
                                 'slot_uri': 'bican:bb3fc701-23a7-45c1-890d-7471730e0ec1'},
                        'was_derived_from': {'description': 'The dissociated or '
                                                            'enriched cell sample(s) '
                                                            'from which the enriched '
                                                            'cell sample was derived '
                                                            'from.',
                                             'exact_mappings': ['NIMP:has_parent'],
                                             'exactly_one_of': [{'range': 'DissociatedCellSample'},
                                                                {'range': 'EnrichedCellSample'}],
                                             'from_schema': 'bican_prov',
                                             'multivalued': True,
                                             'name': 'was_derived_from'},
                        'was_generated_by': {'any_of': [{'range': 'CellEnrichment'},
                                                        {'range': 'EnrichedCellSampleSplitting'}],
                                             'description': 'The cell enrichment or '
                                                            'sample splitting process '
                                                            'from which the enriched '
                                                            'cell sample was generated '
                                                            'by.',
                                             'from_schema': 'bican_prov',
                                             'name': 'was_generated_by'}}})

    was_generated_by: Optional[str] = Field(default=None, description="""The cell enrichment or sample splitting process from which the enriched cell sample was generated by.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'any_of': [{'range': 'CellEnrichment'},
                    {'range': 'EnrichedCellSampleSplitting'}],
         'domain_of': ['ProvEntity',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    was_derived_from: Optional[list[str]] = Field(default=None, description="""The dissociated or enriched cell sample(s) from which the enriched cell sample was derived from.""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'domain_of': ['ProvEntity',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DigitalAsset'],
         'exact_mappings': ['NIMP:has_parent'],
         'exactly_one_of': [{'range': 'DissociatedCellSample'},
                            {'range': 'EnrichedCellSample'}],
         'slot_uri': 'prov:wasDerivedFrom'} })
    name: Optional[str] = Field(default=None, description="""Name of collection of enriched cells or nuclei after enrichment process (usually via FACS using the Enrichment Plan) applied to dissociated_cell_sample.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['NIMP:PD-BERWTM41'],
         'in_subset': ['translator_minimal', 'samples'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'enriched_cell_sample_local_name'}},
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'bican:bb3fc701-23a7-45c1-890d-7471730e0ec1'} })
    enrichment_population: Optional[str] = Field(default=None, description="""Actual percentage of cells as a result of using set of fluorescent marker label(s) to enrich dissociated_cell_sample with desired mix of cell populations.  This plan can also be used to describe 'No FACS' where no enrichment was performed.  This is a property of enriched_cell_prep_container.""", json_schema_extra = { "linkml_meta": {'alias': 'enrichment population',
         'domain_of': ['EnrichedCellSample'],
         'exact_mappings': ['NIMP:PD-TZTZPI37'],
         'in_subset': ['analysis'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'enrichment_population'}},
         'slot_uri': 'bican:875f1c70-f5aa-45e3-94b9-5e482f6c4830'} })
    cell_source_oligo_name: Optional[str] = Field(default=None, description="""Name of cell source oligo used in cell plexing.  The oligo molecularly tags all the cells in the enriched cell sample and allows separate enriched cell samples to be combined downstream in the barcoded cell sample.  The oligo name is associated with a sequence in a lookup table.  This sequence will be needed during alignment to associate reads with the parent source enriched cell sample.""", json_schema_extra = { "linkml_meta": {'alias': 'cell_source_oligo_name',
         'domain_of': ['DissociatedCellSample', 'EnrichedCellSample'],
         'exact_mappings': ['NIMP:PD-CFCFPS27'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'enriched_cell_sample_cell_label_barcode'}}} })
    histone_modification_marker: Optional[str] = Field(default=None, description="""Histone modification marker antibodies (eg H3K27ac, H3K27me3, H3K9me3) used in conjunction with an Enriched Cell Source Barcode in order to combine multiple Enriched Cell Populations before Barcoded Cell Sample step for 10xMultiome method. Each of the Histone antibodies captures an essential part of the epigenome.""", json_schema_extra = { "linkml_meta": {'alias': 'histone_modification_marker',
         'domain_of': ['EnrichedCellSample'],
         'exact_mappings': ['NIMP:PD-ESESLW44'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'histone_modification_marker'}}} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/EnrichedCellSample","bican:EnrichedCellSample"]] = Field(default=["bican:EnrichedCellSample"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class BarcodedCellSample(ProvEntity, MaterialSample):
    """
    A collection of molecularly barcoded cells. Input will be either dissociated cell sample or enriched cell sample. Cell barcodes are only guaranteed to be unique within this one collection. One dissociated cell sample or enriched cell sample can lead to multiple barcoded cell samples.  The sequences of the molecular barcodes are revealed during alignment of the resulting fastq files for the barcoded cell sample. The barcoded cell sample name and the cell level molecular barcode together uniquely identify a single cell.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['NIMP:Barcoded%20Cell%20Sample'],
         'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'library_generation'],
         'mixins': ['ProvEntity'],
         'slot_usage': {'name': {'description': 'Name of a collection of barcoded '
                                                'cells.  Input will be either '
                                                'dissociated_cell_sample or '
                                                'enriched_cell_sample.  Cell barcodes '
                                                'are only guaranteed to be unique '
                                                'within this one collection. One '
                                                'dissociated_cell_sample or '
                                                'enriched_cell_sample can lead to '
                                                'multiple barcoded_cell_samples.',
                                 'exact_mappings': ['NIMP:PD-XEMDJF38'],
                                 'from_schema': 'bican_biolink',
                                 'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                                          'local_name_value': 'barcoded_cell_sample_local_name'}},
                                 'name': 'name',
                                 'slot_uri': 'bican:4c0e6380-e53f-4173-a474-d41e836fefe3'},
                        'was_derived_from': {'description': 'The input dissociated or '
                                                            'enriched cell sample(s) '
                                                            'from which the barcoded '
                                                            'cell sample was derived '
                                                            'from.',
                                             'exact_mappings': ['NIMP:has_parent'],
                                             'exactly_one_of': [{'range': 'DissociatedCellSample'},
                                                                {'range': 'EnrichedCellSample'}],
                                             'from_schema': 'bican_prov',
                                             'multivalued': True,
                                             'name': 'was_derived_from'},
                        'was_generated_by': {'description': 'The barcoding process '
                                                            'from which the barcoded '
                                                            'cell sample is generated '
                                                            'from.',
                                             'from_schema': 'bican_prov',
                                             'name': 'was_generated_by',
                                             'range': 'CellBarcoding'}}})

    was_generated_by: Optional[str] = Field(default=None, description="""The barcoding process from which the barcoded cell sample is generated from.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['ProvEntity',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    was_derived_from: Optional[list[str]] = Field(default=None, description="""The input dissociated or enriched cell sample(s) from which the barcoded cell sample was derived from.""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'domain_of': ['ProvEntity',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DigitalAsset'],
         'exact_mappings': ['NIMP:has_parent'],
         'exactly_one_of': [{'range': 'DissociatedCellSample'},
                            {'range': 'EnrichedCellSample'}],
         'slot_uri': 'prov:wasDerivedFrom'} })
    name: Optional[str] = Field(default=None, description="""Name of a collection of barcoded cells.  Input will be either dissociated_cell_sample or enriched_cell_sample.  Cell barcodes are only guaranteed to be unique within this one collection. One dissociated_cell_sample or enriched_cell_sample can lead to multiple barcoded_cell_samples.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['NIMP:PD-XEMDJF38'],
         'in_subset': ['translator_minimal', 'samples'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'barcoded_cell_sample_local_name'}},
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'bican:4c0e6380-e53f-4173-a474-d41e836fefe3'} })
    expected_cell_capture: Optional[int] = Field(default=None, description="""Expected number of cells/nuclei of a barcoded_cell_sample that will be barcoded and available for sequencing.  This is a derived number from 'Barcoded cell input quantity count' that is dependent on the \"capture rate\" of the barcoding method.  It is usually a calculated fraction of the 'Barcoded cell input quantity count' going into the barcoding method.""", json_schema_extra = { "linkml_meta": {'alias': 'expected cell capture',
         'domain_of': ['BarcodedCellSample'],
         'exact_mappings': ['NIMP:PD-ONONEV39'],
         'in_subset': ['analysis'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'barcoded_cell_sample_number_of_expected_cells'}},
         'slot_uri': 'bican:f10e928d-5a2b-4943-af18-d8fe5d05528d'} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/BarcodedCellSample","bican:BarcodedCellSample"]] = Field(default=["bican:BarcodedCellSample"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class AmplifiedCdna(ProvEntity, MaterialSample):
    """
    A collection of cDNA molecules derived and amplified from an input barcoded cell sample. These cDNA molecules represent the gene expression of each cell, with all cDNA molecules from a given cell retaining that cell's unique barcode from the cell barcoding step. This is a necessary step for GEX methods but is not used for ATAC methods.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['NIMP:Amplified%20cDNA'],
         'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'library_generation'],
         'mixins': ['ProvEntity'],
         'slot_usage': {'name': {'description': 'Name of a collection of cDNA '
                                                'molecules derived and amplified from '
                                                'an input barcoded_cell_sample.  These '
                                                'cDNA molecules represent the gene '
                                                'expression of each cell, with all '
                                                'cDNA molecules from a given cell '
                                                "retaining that cell's unique barcode "
                                                'from the cell barcoding step.  This '
                                                'is a necessary step for GEX methods '
                                                'but is not used for ATAC methods.',
                                 'exact_mappings': ['NIMP:PD-YAAGGG39'],
                                 'from_schema': 'bican_biolink',
                                 'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                                          'local_name_value': 'amplified_cdna_local_name'}},
                                 'name': 'name',
                                 'slot_uri': 'bican:e2606a11-114e-472f-9e05-33f9b6fc3089'},
                        'was_derived_from': {'description': 'The input barcoded cell '
                                                            'sample from which '
                                                            'amplified cDNA was '
                                                            'derived from.',
                                             'exact_mappings': ['NIMP:has_parent'],
                                             'from_schema': 'bican_prov',
                                             'name': 'was_derived_from',
                                             'range': 'BarcodedCellSample'},
                        'was_generated_by': {'description': 'The cDNA amplification '
                                                            'process from which the '
                                                            'amplified cDNA was '
                                                            'generated by.',
                                             'from_schema': 'bican_prov',
                                             'name': 'was_generated_by',
                                             'range': 'CdnaAmplification'}}})

    was_generated_by: Optional[str] = Field(default=None, description="""The cDNA amplification process from which the amplified cDNA was generated by.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['ProvEntity',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    was_derived_from: Optional[str] = Field(default=None, description="""The input barcoded cell sample from which amplified cDNA was derived from.""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'domain_of': ['ProvEntity',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DigitalAsset'],
         'exact_mappings': ['NIMP:has_parent'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    name: Optional[str] = Field(default=None, description="""Name of a collection of cDNA molecules derived and amplified from an input barcoded_cell_sample.  These cDNA molecules represent the gene expression of each cell, with all cDNA molecules from a given cell retaining that cell's unique barcode from the cell barcoding step.  This is a necessary step for GEX methods but is not used for ATAC methods.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['NIMP:PD-YAAGGG39'],
         'in_subset': ['translator_minimal', 'samples'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'amplified_cdna_local_name'}},
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'bican:e2606a11-114e-472f-9e05-33f9b6fc3089'} })
    amplified_cDNA_amplified_quantity_ng: Optional[float] = Field(default=None, description="""Amount of cDNA produced after cDNA amplification measured in nanograms.""", json_schema_extra = { "linkml_meta": {'alias': 'amplified cDNA amplified quantity ng',
         'domain_of': ['AmplifiedCdna', 'Library'],
         'exact_mappings': ['NIMP:PD-TITIIC26'],
         'in_subset': ['analysis'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'amplified_cdna_amplified_quantity_ng'}},
         'slot_uri': 'bican:0db79d05-8612-4896-b9d3-eb1558841449'} })
    amplified_cDNA_RNA_amplification_pass_fail: Optional[AmplifiedCdnaRnaAmplificationPassFail] = Field(default=None, description="""Pass or Fail result based on qualitative assessment of cDNA yield and size.""", json_schema_extra = { "linkml_meta": {'alias': 'amplified cDNA RNA amplification pass-fail',
         'domain_of': ['AmplifiedCdna', 'Library'],
         'exact_mappings': ['NIMP:PD-XXXXFQ31'],
         'in_subset': ['analysis'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'amplified_cdna_rna_amplification_pass_fail'}},
         'slot_uri': 'bican:bc62bdb2-7dc8-4404-bb84-ce0bbcae59e5'} })
    amplified_cDNA_percent_cDNA_longer_than_400bp: Optional[float] = Field(default=None, description="""QC metric to measure mRNA degradation of cDNA.  Higher % is higher quality starting material.  Over 400bp is used as a universal cutoff for intact (full length) vs degraded cDNA and is a common output from Bioanalyzer and Fragment Analyzer elecropheragrams.""", json_schema_extra = { "linkml_meta": {'alias': 'amplified cDNA percent cDNA longer than 400bp',
         'domain_of': ['AmplifiedCdna'],
         'exact_mappings': ['NIMP:PD-JJJJWD35'],
         'in_subset': ['analysis'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'amplified_cdna_percent_cdna_longer_than_400bp'}},
         'slot_uri': 'bican:8d150467-f69e-461c-b54c-bcfd22f581e5'} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/AmplifiedCdna","bican:AmplifiedCdna"]] = Field(default=["bican:AmplifiedCdna"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class Library(ProvEntity, MaterialSample):
    """
    A collection of fragmented and barcode-indexed DNA molecules for sequencing. An index or barcode is typically introduced to enable identification of library origin to allow libraries to be pooled together for sequencing.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['NIMP:Library'],
         'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'library_generation'],
         'mixins': ['ProvEntity'],
         'slot_usage': {'name': {'description': 'Name of a library, which is a '
                                                'collection of fragmented and '
                                                'barcode-indexed DNA molecules for '
                                                'sequencing.  An index or barcode is '
                                                'typically introduced to enable '
                                                'identification of library origin to '
                                                'allow libraries to be pooled together '
                                                'for sequencing.',
                                 'exact_mappings': ['NIMP:PD-AJJUCC35'],
                                 'from_schema': 'bican_biolink',
                                 'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                                          'local_name_value': 'library_local_name'}},
                                 'name': 'name',
                                 'slot_uri': 'bican:f717e254-3630-4342-be7b-4d56376e7afe'},
                        'was_derived_from': {'any_of': [{'range': 'BarcodedCellSample'},
                                                        {'range': 'AmplifiedCdna'}],
                                             'description': 'The input barcoded cell '
                                                            'sample or amplified cDNA '
                                                            'from which the library '
                                                            'was derived from.',
                                             'exact_mappings': ['NIMP:has_parent'],
                                             'from_schema': 'bican_prov',
                                             'name': 'was_derived_from'},
                        'was_generated_by': {'description': 'The library construction '
                                                            'process from which the '
                                                            'library was generated by.',
                                             'from_schema': 'bican_prov',
                                             'name': 'was_generated_by',
                                             'range': 'LibraryConstruction'}}})

    was_generated_by: Optional[str] = Field(default=None, description="""The library construction process from which the library was generated by.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['ProvEntity',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    was_derived_from: Optional[str] = Field(default=None, description="""The input barcoded cell sample or amplified cDNA from which the library was derived from.""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'any_of': [{'range': 'BarcodedCellSample'}, {'range': 'AmplifiedCdna'}],
         'domain_of': ['ProvEntity',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DigitalAsset'],
         'exact_mappings': ['NIMP:has_parent'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    name: Optional[str] = Field(default=None, description="""Name of a library, which is a collection of fragmented and barcode-indexed DNA molecules for sequencing.  An index or barcode is typically introduced to enable identification of library origin to allow libraries to be pooled together for sequencing.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['NIMP:PD-AJJUCC35'],
         'in_subset': ['translator_minimal', 'samples'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'library_local_name'}},
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'bican:f717e254-3630-4342-be7b-4d56376e7afe'} })
    library_avg_size_bp: Optional[int] = Field(default=None, description="""Average size of the library in terms of base pairs.  This is used to calculate the molarity before pooling and sequencing.""", json_schema_extra = { "linkml_meta": {'alias': 'library avg size bp',
         'domain_of': ['Library'],
         'exact_mappings': ['NIMP:PD-VJVJLC46'],
         'in_subset': ['analysis'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'library_avg_size_bp'}},
         'slot_uri': 'bican:f851eba9-56d1-4472-9d0c-d7f8bc33000a'} })
    library_concentration_nm: Optional[float] = Field(default=None, description="""Concentration of library in terms of nM (nMol/L).  Number of molecules is needed for accurate pooling of the libraries and for generating the number of target reads/cell in sequencing.""", json_schema_extra = { "linkml_meta": {'alias': 'library concentration nm',
         'domain_of': ['Library'],
         'exact_mappings': ['NIMP:PD-DCDCLD43'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'library_concentration_nm'}},
         'slot_uri': 'bican:90805b3f-f380-4f23-b159-e7eaa0c8f052'} })
    library_prep_pass_fail: Optional[LibraryPrepPassFail] = Field(default=None, description="""Pass or Fail result based on qualitative assessment of library yield and size.""", json_schema_extra = { "linkml_meta": {'alias': 'library prep pass-fail',
         'domain_of': ['AmplifiedCdna', 'Library'],
         'exact_mappings': ['NIMP:PD-QHQHQB42'],
         'in_subset': ['analysis'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'library_prep_pass_fail'}},
         'slot_uri': 'bican:6817ede2-7ead-402d-9dbc-131aca627c6c'} })
    library_quantification_fmol: Optional[float] = Field(default=None, description="""Amount of library generated in terms of femtomoles""", json_schema_extra = { "linkml_meta": {'alias': 'library quantification fmol',
         'domain_of': ['Library'],
         'exact_mappings': ['NIMP:PD-JYJYDK42'],
         'in_subset': ['analysis'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'library_quantification_fmol'}},
         'slot_uri': 'bican:4c09ada7-c116-48bc-8fb1-0dcf5c4b939a'} })
    library_quantification_ng: Optional[float] = Field(default=None, description="""Amount of library generated in terms of nanograms""", json_schema_extra = { "linkml_meta": {'alias': 'library quantification ng',
         'domain_of': ['AmplifiedCdna', 'Library'],
         'exact_mappings': ['NIMP:PD-TNTNXP37'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'library_quantification_ng'}},
         'slot_uri': 'bican:318b2d3a-dae7-4c63-bfbb-93862b92f63e'} })
    R1_R2_index_name: Optional[LibraryR1R2Index] = Field(default=None, description="""Name of the pair of library indexes used for sequencing.  Indexes allow libraries to be pooled together for sequencing.  Sequencing output (fastq) are demultiplexed by using the indexes for each library.  The name will be associated with the sequences of i7, i5, and i5as, which are needed by SeqCores for demultiplexing.  The required direction of the sequence (sense or antisense) of the index can differ depending on sequencing instruments.""", json_schema_extra = { "linkml_meta": {'alias': 'R1_R2 index name',
         'domain_of': ['Library'],
         'exact_mappings': ['NIMP:PD-VLLMWZ60'],
         'in_subset': ['analysis', 'tracking'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'library_r1_r2_index'}},
         'slot_uri': 'bican:c94b5d8a-e92d-47af-8c0e-ea3b58be4d06'} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/Library","bican:Library"]] = Field(default=["bican:Library"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class LibraryAliquot(ProvEntity, MaterialSample):
    """
    One library in the library pool. Each library aliquot in a library pool will have a unique R1/R2 index to allow for sequencing together then separating the sequencing output by originating library aliquot through the process of demultiplexing. The resulting demultiplexed fastq files will include the library aliquot name.  A given library may produce multiple library aliquots, which is done in the case of resequencing.  Each library aliquot will produce a set of fastq files.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['NIMP:Library%20Aliquot'],
         'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'library_generation'],
         'mixins': ['ProvEntity'],
         'slot_usage': {'name': {'description': 'One library in the library pool.  '
                                                'Each Library_aliquot_name in a '
                                                'library pool will have a unique R1/R2 '
                                                'index to allow for sequencing '
                                                'together then separating the '
                                                'sequencing output by originating '
                                                'library aliquot through the process '
                                                'of demultiplexing.  The resulting '
                                                'demultiplexed fastq files will '
                                                'include the library_aliquot_name.',
                                 'exact_mappings': ['NIMP:PD-XCXCCC35'],
                                 'from_schema': 'bican_biolink',
                                 'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                                          'local_name_value': 'library_aliquot_local_name'}},
                                 'name': 'name',
                                 'slot_uri': 'bican:34191bad-d167-4335-8224-ade897d3728e'},
                        'was_derived_from': {'description': 'The input library from '
                                                            'which the library aliquot '
                                                            'was derived from.',
                                             'exact_mappings': ['NIMP:has_parent'],
                                             'from_schema': 'bican_prov',
                                             'name': 'was_derived_from',
                                             'range': 'Library'}}})

    was_derived_from: Optional[str] = Field(default=None, description="""The input library from which the library aliquot was derived from.""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'domain_of': ['ProvEntity',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DigitalAsset'],
         'exact_mappings': ['NIMP:has_parent'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    name: Optional[str] = Field(default=None, description="""One library in the library pool.  Each Library_aliquot_name in a library pool will have a unique R1/R2 index to allow for sequencing together then separating the sequencing output by originating library aliquot through the process of demultiplexing.  The resulting demultiplexed fastq files will include the library_aliquot_name.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['NIMP:PD-XCXCCC35'],
         'in_subset': ['translator_minimal', 'samples'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'library_aliquot_local_name'}},
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'bican:34191bad-d167-4335-8224-ade897d3728e'} })
    was_generated_by: Optional[str] = Field(default=None, description="""Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['ProvEntity',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/LibraryAliquot","bican:LibraryAliquot"]] = Field(default=["bican:LibraryAliquot"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class LibraryPool(ProvEntity, MaterialSample):
    """
    A library pool is made up of library aliquots from multiple libraries. Each library aliquot in a library pool will have a unique R1/R2 index to allow for sequencing together then separating the sequencing output by originating library aliquot through the process of demultiplexing.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['NIMP:Library%20Pool'],
         'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'library_generation'],
         'mixins': ['ProvEntity'],
         'slot_usage': {'name': {'description': "Library lab's library pool name.  For "
                                                'some labs this may be the same as '
                                                '"Libray pool tube local name".   '
                                                'Other labs distinguish between the '
                                                'local tube label of the library pool '
                                                'and the library pool name provided to '
                                                'SeqCore for tracking.  Local Pool '
                                                'Name is used to communicate '
                                                'sequencing status between SeqCore and '
                                                'Library Labs.',
                                 'exact_mappings': ['NIMP:PD-KKIAPA48'],
                                 'from_schema': 'bican_biolink',
                                 'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                                          'local_name_value': 'library_pool_local_name'}},
                                 'name': 'name',
                                 'slot_uri': 'bican:29e0578b-6427-4c93-b29b-bde27fbadeec'},
                        'was_derived_from': {'description': 'The input aliquot(s) from '
                                                            'which the library pool '
                                                            'was derived from.',
                                             'exact_mappings': ['NIMP:has_parent'],
                                             'from_schema': 'bican_prov',
                                             'multivalued': True,
                                             'name': 'was_derived_from',
                                             'range': 'LibraryAliquot'},
                        'was_generated_by': {'description': 'The pooling process from '
                                                            'which the library pool '
                                                            'was generated by.',
                                             'from_schema': 'bican_prov',
                                             'name': 'was_generated_by',
                                             'range': 'LibraryPooling'}}})

    was_generated_by: Optional[str] = Field(default=None, description="""The pooling process from which the library pool was generated by.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['ProvEntity',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    was_derived_from: Optional[list[str]] = Field(default=None, description="""The input aliquot(s) from which the library pool was derived from.""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'domain_of': ['ProvEntity',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DigitalAsset'],
         'exact_mappings': ['NIMP:has_parent'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    name: Optional[str] = Field(default=None, description="""Library lab's library pool name.  For some labs this may be the same as \"Libray pool tube local name\".   Other labs distinguish between the local tube label of the library pool and the library pool name provided to SeqCore for tracking.  Local Pool Name is used to communicate sequencing status between SeqCore and Library Labs.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['NIMP:PD-KKIAPA48'],
         'in_subset': ['translator_minimal', 'samples'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'library_pool_local_name'}},
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'bican:29e0578b-6427-4c93-b29b-bde27fbadeec'} })
    library_pool_tube_internal_label: Optional[str] = Field(default=None, description="""Library Pool Tube local name.  Label of the tube containing the library pool, which is made up of multiple library_aliquots.  This is a Library Lab local tube name, before the pool is aliquoted to the Seq Core provided tube 'Library Pool Tube Name'.""", json_schema_extra = { "linkml_meta": {'alias': 'library_pool_tube_internal_label',
         'domain_of': ['LibraryPool'],
         'exact_mappings': ['NIMP:PD-WNYWPA48'],
         'in_subset': ['analysis', 'tracking'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'library_pool_local_tube_id'}},
         'slot_uri': 'bican:f1fdea98-7849-4def-a62f-a04cbbf98922'} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/LibraryPool","bican:LibraryPool"]] = Field(default=["bican:LibraryPool"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class DissectionRoiDelineation(ProvActivity, Procedure):
    """
    The process of outlining a region of interest on a brain slab image to guide the dissection and generation of a tissue sample.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'library_generation'],
         'mixins': ['ProvActivity'],
         'slot_usage': {'used': {'description': 'The brain slab that was annotated by '
                                                'the delineation process.',
                                 'from_schema': 'bican_prov',
                                 'name': 'used',
                                 'range': 'BrainSlab'}}})

    used: Optional[str] = Field(default=None, description="""The brain slab that was annotated by the delineation process.""", json_schema_extra = { "linkml_meta": {'alias': 'used',
         'domain_of': ['ProvActivity',
                       'DissectionRoiDelineation',
                       'TissueDissection',
                       'CellDissociation',
                       'CellEnrichment',
                       'EnrichedCellSampleSplitting',
                       'CellBarcoding',
                       'CdnaAmplification',
                       'LibraryConstruction',
                       'LibraryPooling'],
         'slot_uri': 'prov:used'} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/DissectionRoiDelineation","bican:DissectionRoiDelineation"]] = Field(default=["bican:DissectionRoiDelineation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class TissueDissection(ProvActivity, Procedure):
    """
    The process of dissecting a tissue sample from a brain slab guided by a dissection region of interest (ROI) delineation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'library_generation'],
         'mixins': ['ProvActivity'],
         'slot_usage': {'used': {'description': 'The brain slab from which the tissue '
                                                'sample was dissected from.',
                                 'from_schema': 'bican_prov',
                                 'name': 'used',
                                 'range': 'BrainSlab'}}})

    used: Optional[str] = Field(default=None, description="""The brain slab from which the tissue sample was dissected from.""", json_schema_extra = { "linkml_meta": {'alias': 'used',
         'domain_of': ['ProvActivity',
                       'DissectionRoiDelineation',
                       'TissueDissection',
                       'CellDissociation',
                       'CellEnrichment',
                       'EnrichedCellSampleSplitting',
                       'CellBarcoding',
                       'CdnaAmplification',
                       'LibraryConstruction',
                       'LibraryPooling'],
         'slot_uri': 'prov:used'} })
    was_guided_by: Optional[str] = Field(default=None, description="""The dissection ROI polygon which was used to guide the tissue dissection.""", json_schema_extra = { "linkml_meta": {'alias': 'was_guided_by', 'domain_of': ['TissueDissection']} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/TissueDissection","bican:TissueDissection"]] = Field(default=["bican:TissueDissection"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class CellDissociation(ProvActivity, Procedure):
    """
    The process of generating dissociated cells from an input tissue sample. This process could also introduce a tissue-source barcode (eg cell hashing), allowing mixing of cell dissociation samples at the cell barcoding step.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'library_generation'],
         'mixins': ['ProvActivity'],
         'slot_usage': {'used': {'description': 'The input tissue sample(s) from which '
                                                'the dissociated cell sample was '
                                                'derived from.',
                                 'from_schema': 'bican_prov',
                                 'multivalued': True,
                                 'name': 'used',
                                 'range': 'TissueSample'}}})

    used: Optional[list[str]] = Field(default=None, description="""The input tissue sample(s) from which the dissociated cell sample was derived from.""", json_schema_extra = { "linkml_meta": {'alias': 'used',
         'domain_of': ['ProvActivity',
                       'DissectionRoiDelineation',
                       'TissueDissection',
                       'CellDissociation',
                       'CellEnrichment',
                       'EnrichedCellSampleSplitting',
                       'CellBarcoding',
                       'CdnaAmplification',
                       'LibraryConstruction',
                       'LibraryPooling'],
         'slot_uri': 'prov:used'} })
    process_date: Optional[str] = Field(default=None, description="""Date of cell dissociation process.""", json_schema_extra = { "linkml_meta": {'alias': 'process_date',
         'domain_of': ['CellDissociation',
                       'CellEnrichment',
                       'CellBarcoding',
                       'CdnaAmplification',
                       'LibraryConstruction',
                       'LibraryPooling'],
         'exact_mappings': ['NIMP:PD-BUBUFE27'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'dissociated_cell_sample_preparation_date'}}} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/CellDissociation","bican:CellDissociation"]] = Field(default=["bican:CellDissociation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class CellEnrichment(ProvActivity, Procedure):
    """
    The process of enriching a dissociated cell sample by including or excluding cells of different types based on an enrichment plan using techniques such as fluorescence-activated cell sorting (FACS). This process could also introduce a tissue-source barcode (eg cell hashing), allowing mixing of cell enriched samples at the cell barcoding step.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'library_generation'],
         'mixins': ['ProvActivity'],
         'slot_usage': {'used': {'description': 'The input dissociated cell sample(s) '
                                                'from which the enriched cell sample '
                                                'was derived from.',
                                 'from_schema': 'bican_prov',
                                 'multivalued': True,
                                 'name': 'used',
                                 'range': 'DissociatedCellSample'}}})

    used: Optional[list[str]] = Field(default=None, description="""The input dissociated cell sample(s) from which the enriched cell sample was derived from.""", json_schema_extra = { "linkml_meta": {'alias': 'used',
         'domain_of': ['ProvActivity',
                       'DissectionRoiDelineation',
                       'TissueDissection',
                       'CellDissociation',
                       'CellEnrichment',
                       'EnrichedCellSampleSplitting',
                       'CellBarcoding',
                       'CdnaAmplification',
                       'LibraryConstruction',
                       'LibraryPooling'],
         'slot_uri': 'prov:used'} })
    process_date: Optional[str] = Field(default=None, description="""Date of cell enrichment process.""", json_schema_extra = { "linkml_meta": {'alias': 'process_date',
         'domain_of': ['CellDissociation',
                       'CellEnrichment',
                       'CellBarcoding',
                       'CdnaAmplification',
                       'LibraryConstruction',
                       'LibraryPooling'],
         'exact_mappings': ['NIMP:PD-PFPFFC28'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'enriched_cell_sample_preparation_date'}}} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/CellEnrichment","bican:CellEnrichment"]] = Field(default=["bican:CellEnrichment"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class EnrichedCellSampleSplitting(ProvActivity, Procedure):
    """
    The process of splitting an enriched cell sample into several portions. Each portion may be used by the same or different groups for different scientific studies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'library_generation'],
         'mixins': ['ProvActivity'],
         'slot_usage': {'used': {'description': 'The enrichment cell sample splitting '
                                                'process from which the enriched cell '
                                                'sample was generated by.',
                                 'from_schema': 'bican_prov',
                                 'name': 'used',
                                 'range': 'EnrichedCellSample'}}})

    used: Optional[str] = Field(default=None, description="""The enrichment cell sample splitting process from which the enriched cell sample was generated by.""", json_schema_extra = { "linkml_meta": {'alias': 'used',
         'domain_of': ['ProvActivity',
                       'DissectionRoiDelineation',
                       'TissueDissection',
                       'CellDissociation',
                       'CellEnrichment',
                       'EnrichedCellSampleSplitting',
                       'CellBarcoding',
                       'CdnaAmplification',
                       'LibraryConstruction',
                       'LibraryPooling'],
         'slot_uri': 'prov:used'} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/EnrichedCellSampleSplitting","bican:EnrichedCellSampleSplitting"]] = Field(default=["bican:EnrichedCellSampleSplitting"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class CellBarcoding(ProvActivity, Procedure):
    """
    The process of adding a molecular barcode to individual cells in a sample. The input will be either dissociated cell sample or enriched cell sample. Cell barcodes are only guaranteed to be unique within this one collection. One dissociated cell sample or enriched cell sample can lead to multiple barcoded cell samples.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'library_generation'],
         'mixins': ['ProvActivity'],
         'slot_usage': {'used': {'description': 'The input dissociated or enriched '
                                                'cell sample(s) from which the '
                                                'barcoded cell sample was derived '
                                                'from.',
                                 'exactly_one_of': [{'range': 'DissociatedCellSample'},
                                                    {'range': 'EnrichedCellSample'}],
                                 'from_schema': 'bican_prov',
                                 'multivalued': True,
                                 'name': 'used'}}})

    used: Optional[list[str]] = Field(default=None, description="""The input dissociated or enriched cell sample(s) from which the barcoded cell sample was derived from.""", json_schema_extra = { "linkml_meta": {'alias': 'used',
         'domain_of': ['ProvActivity',
                       'DissectionRoiDelineation',
                       'TissueDissection',
                       'CellDissociation',
                       'CellEnrichment',
                       'EnrichedCellSampleSplitting',
                       'CellBarcoding',
                       'CdnaAmplification',
                       'LibraryConstruction',
                       'LibraryPooling'],
         'exactly_one_of': [{'range': 'DissociatedCellSample'},
                            {'range': 'EnrichedCellSample'}],
         'slot_uri': 'prov:used'} })
    barcoded_cell_sample_port_well: Optional[str] = Field(default=None, description="""Specific position of the loaded port of the 10x chip.  An Enriched or Dissociated Cell Sample is loaded into a port on a chip (creating a Barcoded Cell Sample). Can be left null for non-10x methods.""", json_schema_extra = { "linkml_meta": {'alias': 'barcoded cell sample port well',
         'domain_of': ['CellBarcoding'],
         'exact_mappings': ['NIMP:PD-KJKJZK32'],
         'in_subset': ['analysis'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'barcoded_cell_sample_port_well'}},
         'slot_uri': 'bican:aca38100-d245-4be4-9be3-ba27192779fe'} })
    barcoded_cell_input_quantity_count: Optional[int] = Field(default=None, description="""Number of enriched or dissociated cells/nuclei going into the barcoding process.""", json_schema_extra = { "linkml_meta": {'alias': 'barcoded cell input quantity count',
         'domain_of': ['CellBarcoding'],
         'exact_mappings': ['NIMP:PD-ZZZZWQ40'],
         'in_subset': ['analysis'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'barcoded_cell_input_quantity_count'}},
         'slot_uri': 'bican:aa534269-7c9b-4b63-b990-eea8cda56d0e'} })
    process_date: Optional[str] = Field(default=None, description="""Date of cell barcoding process.""", json_schema_extra = { "linkml_meta": {'alias': 'process_date',
         'domain_of': ['CellDissociation',
                       'CellEnrichment',
                       'CellBarcoding',
                       'CdnaAmplification',
                       'LibraryConstruction',
                       'LibraryPooling'],
         'exact_mappings': ['NIMP:PD-SHSHZS25'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'barcoded_cell_sample_preparation_date'}}} })
    method: Optional[BarcodedCellSampleTechnique] = Field(default=None, description="""Standardized nomenclature to describe the general barcoding method used.  For example: Multiome, ATAC Only, GEX Only or snm3C-seq.""", json_schema_extra = { "linkml_meta": {'alias': 'method',
         'domain_of': ['CellBarcoding', 'LibraryConstruction'],
         'exact_mappings': ['NIMP:PD-TDTDDF25'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'barcoded_cell_sample_technique'}}} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/CellBarcoding","bican:CellBarcoding"]] = Field(default=["bican:CellBarcoding"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class CdnaAmplification(ProvActivity, Procedure):
    """
    The process of creating a collection of cDNA molecules derived and amplified from an input barcoded cell sample.  A large amount of cDNA is needed to have accurate and reliable sequencing detection of gene expression.  This process generates multiple copies of each mRNA transcript (expressed gene) within each cell while retaining the cell's unique barcode from the barcoding step. This is a necessary step for GEX methods but is not used for ATAC methods.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'library_generation'],
         'mixins': ['ProvActivity'],
         'slot_usage': {'used': {'description': 'The input barcoded cell sample from '
                                                'which amplified cDNA was derived '
                                                'from.',
                                 'from_schema': 'bican_prov',
                                 'name': 'used',
                                 'range': 'BarcodedCellSample'}}})

    used: Optional[str] = Field(default=None, description="""The input barcoded cell sample from which amplified cDNA was derived from.""", json_schema_extra = { "linkml_meta": {'alias': 'used',
         'domain_of': ['ProvActivity',
                       'DissectionRoiDelineation',
                       'TissueDissection',
                       'CellDissociation',
                       'CellEnrichment',
                       'EnrichedCellSampleSplitting',
                       'CellBarcoding',
                       'CdnaAmplification',
                       'LibraryConstruction',
                       'LibraryPooling'],
         'slot_uri': 'prov:used'} })
    amplified_cDNA_PCR_cycles: Optional[int] = Field(default=None, description="""Number of PCR cycles used during cDNA amplification for this cDNA.""", json_schema_extra = { "linkml_meta": {'alias': 'amplified cDNA PCR cycles',
         'domain_of': ['CdnaAmplification'],
         'exact_mappings': ['NIMP:PD-OKOKQD38'],
         'in_subset': ['analysis'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'amplified_cdna_pcr_cycles'}},
         'slot_uri': 'bican:3827634c-3f8f-4760-b358-86ce4b030238'} })
    cDNA_amplification_process_date: Optional[date] = Field(default=None, description="""Date of cDNA amplification.""", json_schema_extra = { "linkml_meta": {'alias': 'cDNA amplification process date',
         'domain_of': ['CellDissociation',
                       'CellEnrichment',
                       'CellBarcoding',
                       'CdnaAmplification',
                       'LibraryConstruction',
                       'LibraryPooling'],
         'exact_mappings': ['NIMP:PD-BYBYBY24'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'amplified_cdna_preparation_date'}},
         'slot_uri': 'bican:6cc333e7-9b98-497f-b7b1-eae904db2400'} })
    cDNA_amplification_set: Optional[str] = Field(default=None, description="""cDNA amplification set, containing multiple amplified_cDNA_names that were processed at the same time.""", json_schema_extra = { "linkml_meta": {'alias': 'cDNA amplification set',
         'domain_of': ['CdnaAmplification', 'LibraryConstruction'],
         'exact_mappings': ['NIMP:PD-SCSCTM41'],
         'in_subset': ['analysis'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'cdna_amplification_set'}},
         'slot_uri': 'bican:42e98a88-50b3-4ea2-871b-2142f6a0dfdd'} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/CdnaAmplification","bican:CdnaAmplification"]] = Field(default=["bican:CdnaAmplification"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class LibraryConstruction(ProvActivity, Procedure):
    """
    The process of constructing a library from input material (such as amplified cDNA or barcoded cell sample) derived from one or more cell samples.  cDNA is fragmented into smaller pieces appropriate for sequencing and at the same time a library index barcode is incorporated to enable identification of library origin, allowing libraries to be pooled together for sequencing.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'library_generation'],
         'mixins': ['ProvActivity'],
         'slot_usage': {'used': {'any_of': [{'range': 'BarcodedCellSample'},
                                            {'range': 'AmplifiedCdna'}],
                                 'description': 'The input barcoded cell sample or '
                                                'amplified cDNA from which the library '
                                                'was derived from.',
                                 'from_schema': 'bican_prov',
                                 'name': 'used'}}})

    used: Optional[str] = Field(default=None, description="""The input barcoded cell sample or amplified cDNA from which the library was derived from.""", json_schema_extra = { "linkml_meta": {'alias': 'used',
         'any_of': [{'range': 'BarcodedCellSample'}, {'range': 'AmplifiedCdna'}],
         'domain_of': ['ProvActivity',
                       'DissectionRoiDelineation',
                       'TissueDissection',
                       'CellDissociation',
                       'CellEnrichment',
                       'EnrichedCellSampleSplitting',
                       'CellBarcoding',
                       'CdnaAmplification',
                       'LibraryConstruction',
                       'LibraryPooling'],
         'slot_uri': 'prov:used'} })
    library_method: Optional[LibraryTechnique] = Field(default=None, description="""Standardized nomenclature to describe the specific library method used.  This specifies the alignment method required for the library.  For example, 10xV3.1 (for RNASeq single assay), 10xMult-GEX (for RNASeq multiome assay), and 10xMult-ATAC (for ATACSeq multiome assay).""", json_schema_extra = { "linkml_meta": {'alias': 'library method',
         'domain_of': ['CellBarcoding', 'LibraryConstruction'],
         'exact_mappings': ['NIMP:PD-AJAJCN35'],
         'in_subset': ['analysis', 'tracking', 'alignment'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'library_technique'}},
         'slot_uri': 'bican:7b60d59e-fdd7-4b27-a2d4-cae9b69103a6'} })
    library_creation_date: Optional[date] = Field(default=None, description="""Date of library construction.""", json_schema_extra = { "linkml_meta": {'alias': 'library creation date',
         'domain_of': ['CellDissociation',
                       'CellEnrichment',
                       'CellBarcoding',
                       'CdnaAmplification',
                       'LibraryConstruction',
                       'LibraryPooling'],
         'exact_mappings': ['NIMP:PD-JCJCNM35'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'library_preparation_date'}},
         'slot_uri': 'bican:9c2f575d-1b64-451d-894f-656861afe07a'} })
    library_input_ng: Optional[float] = Field(default=None, description="""Amount of cDNA going into library construction in nanograms.""", json_schema_extra = { "linkml_meta": {'alias': 'library input ng',
         'domain_of': ['LibraryConstruction'],
         'exact_mappings': ['NIMP:PD-AFAFXP37'],
         'in_subset': ['analysis'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'library_input_ng'}},
         'slot_uri': 'bican:e4d31d97-722d-4771-a0e4-e6062190f2c1'} })
    library_prep_set: Optional[str] = Field(default=None, description="""Library set, containing multiple library_names that were processed at the same time.""", json_schema_extra = { "linkml_meta": {'alias': 'library prep set',
         'domain_of': ['CdnaAmplification', 'LibraryConstruction'],
         'exact_mappings': ['NIMP:PD-PCPCVR50'],
         'in_subset': ['analysis'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'library_prep_set'}},
         'slot_uri': 'bican:b124ffa9-9134-4a61-a30d-bb191b2fc7fa'} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/LibraryConstruction","bican:LibraryConstruction"]] = Field(default=["bican:LibraryConstruction"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class LibraryPooling(ProvActivity, Procedure):
    """
    The process of constructing of a libray pool by combining library aliquots from a set of input libraries. Each library aliquot in a library pool will have a unique R1/R2 index to allow for sequencing together then separating the sequencing output by originating library aliquot through the process of demultiplexing.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'library_generation'],
         'mixins': ['ProvActivity'],
         'slot_usage': {'used': {'description': 'The input aliquot(s) from which the '
                                                'library pool was derived from.',
                                 'from_schema': 'bican_prov',
                                 'multivalued': True,
                                 'name': 'used',
                                 'range': 'LibraryAliquot'}}})

    used: Optional[list[str]] = Field(default=None, description="""The input aliquot(s) from which the library pool was derived from.""", json_schema_extra = { "linkml_meta": {'alias': 'used',
         'domain_of': ['ProvActivity',
                       'DissectionRoiDelineation',
                       'TissueDissection',
                       'CellDissociation',
                       'CellEnrichment',
                       'EnrichedCellSampleSplitting',
                       'CellBarcoding',
                       'CdnaAmplification',
                       'LibraryConstruction',
                       'LibraryPooling'],
         'slot_uri': 'prov:used'} })
    process_date: Optional[str] = Field(default=None, description="""Date of library pooling process.""", json_schema_extra = { "linkml_meta": {'alias': 'process_date',
         'domain_of': ['CellDissociation',
                       'CellEnrichment',
                       'CellBarcoding',
                       'CdnaAmplification',
                       'LibraryConstruction',
                       'LibraryPooling'],
         'exact_mappings': ['NIMP:PD-XUXUNM35'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'library_pool_preparation_date'}}} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/LibraryPooling","bican:LibraryPooling"]] = Field(default=["bican:LibraryPooling"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })


class DissectionRoiPolygon(ProvEntity, Entity):
    """
    A polygon annotated on a brain slab image delineating a region of interest (ROI) for a tissue sample dissectioning.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['NIMP:Specimen%20Dissected%20ROI'],
         'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'in_subset': ['bican', 'tissue_specimen'],
         'mixins': ['ProvEntity'],
         'slot_usage': {'name': {'description': 'Name of a polygon annotated on a '
                                                'brain slab image delineating a region '
                                                'of interest (ROI) for a tissue sample '
                                                'dissectioning.',
                                 'from_schema': 'bican_biolink',
                                 'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                                          'local_name_value': 'local_name'}},
                                 'name': 'name'},
                        'was_generated_by': {'description': 'The delineation process '
                                                            'from which the dissection '
                                                            'ROI polygon was generated '
                                                            'by.',
                                             'from_schema': 'bican_prov',
                                             'name': 'was_generated_by',
                                             'range': 'DissectionRoiDelineation'}}})

    was_generated_by: Optional[str] = Field(default=None, description="""The delineation process from which the dissection ROI polygon was generated by.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['ProvEntity',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    name: Optional[str] = Field(default=None, description="""Name of a polygon annotated on a brain slab image delineating a region of interest (ROI) for a tissue sample dissectioning.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'local_names': {'NIMP': {'local_name_source': 'NIMP',
                                  'local_name_value': 'local_name'}},
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    annotates: Optional[str] = Field(default=None, description="""The brain slab that was annotated by the delineation process.""", json_schema_extra = { "linkml_meta": {'alias': 'annotates',
         'domain_of': ['DissectionRoiPolygon'],
         'exact_mappings': ['NIMP:has_parent']} })
    was_derived_from: Optional[str] = Field(default=None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'domain_of': ['ProvEntity',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DigitalAsset'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/DissectionRoiPolygon","bican:DissectionRoiPolygon"]] = Field(default=["bican:DissectionRoiPolygon"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })


class DigitalAsset(ProvEntity, Dataset):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://identifiers.org/brain-bican/library-generation-schema',
         'mixins': ['ProvEntity'],
         'slot_usage': {'content_url': {'from_schema': 'bican_core',
                                        'name': 'content_url'},
                        'digest': {'from_schema': 'bican_core', 'name': 'digest'},
                        'was_derived_from': {'from_schema': 'bican_prov',
                                             'name': 'was_derived_from',
                                             'range': 'LibraryPool'}}})

    was_derived_from: Optional[str] = Field(default=None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'domain_of': ['ProvEntity',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DigitalAsset'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    digest: Optional[list[Union[Checksum, str]]] = Field(default=None, description="""Stores checksum information.""", json_schema_extra = { "linkml_meta": {'alias': 'digest',
         'any_of': [{'range': 'checksum'}, {'range': 'string'}],
         'domain_of': ['DigitalAsset'],
         'slot_uri': 'bican:digest'} })
    content_url: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'content_url',
         'domain_of': ['DigitalAsset'],
         'slot_uri': 'schema:url'} })
    data_type: Optional[str] = Field(default=None, description="""The type of data in the file.""", json_schema_extra = { "linkml_meta": {'alias': 'data_type', 'domain_of': ['DigitalAsset']} })
    was_generated_by: Optional[str] = Field(default=None, description="""Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['ProvEntity',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'alias': 'iri',
         'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/DigitalAsset","bican:DigitalAsset"]] = Field(default=["bican:DigitalAsset"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}.""", json_schema_extra = { "linkml_meta": {'alias': 'category',
         'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'type',
         'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene or gene product',
                       'gene',
                       'genome',
                       'Donor',
                       'BrainSlab',
                       'TissueSample',
                       'DissociatedCellSample',
                       'EnrichedCellSample',
                       'BarcodedCellSample',
                       'AmplifiedCdna',
                       'Library',
                       'LibraryAliquot',
                       'LibraryPool',
                       'DissectionRoiPolygon'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'alias': 'has_attribute',
         'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'OMIM:has_inheritance_type',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'alias': 'provided_by',
         'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'alias': 'xref',
         'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'full_name',
         'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'synonym',
         'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    license: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'license',
         'definition_uri': 'https://w3id.org/biolink/vocab/license',
         'domain': 'information content entity',
         'domain_of': ['information content entity', 'dataset'],
         'exact_mappings': ['dct:license'],
         'is_a': 'node property',
         'narrow_mappings': ['WIKIDATA_PROPERTY:P275'],
         'slot_uri': 'biolink:license'} })
    rights: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'rights',
         'definition_uri': 'https://w3id.org/biolink/vocab/rights',
         'domain': 'information content entity',
         'domain_of': ['information content entity', 'dataset'],
         'exact_mappings': ['dct:rights'],
         'is_a': 'node property',
         'slot_uri': 'biolink:rights'} })
    format: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'format',
         'definition_uri': 'https://w3id.org/biolink/vocab/format',
         'domain': 'information content entity',
         'domain_of': ['information content entity', 'dataset'],
         'exact_mappings': ['dct:format', 'WIKIDATA_PROPERTY:P2701'],
         'is_a': 'node property',
         'slot_uri': 'biolink:format'} })
    creation_date: Optional[date] = Field(default=None, description="""date on which an entity was created. This can be applied to nodes or edges""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date',
         'aliases': ['publication date'],
         'definition_uri': 'https://w3id.org/biolink/vocab/creation_date',
         'domain': 'named thing',
         'domain_of': ['information content entity', 'dataset'],
         'exact_mappings': ['dct:createdOn', 'WIKIDATA_PROPERTY:P577'],
         'is_a': 'node property',
         'slot_uri': 'biolink:creation_date'} })


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
VersionedNamedThing.model_rebuild()
Checksum.model_rebuild()
ProvActivity.model_rebuild()
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
DissectionRoiDelineation.model_rebuild()
TissueDissection.model_rebuild()
CellDissociation.model_rebuild()
CellEnrichment.model_rebuild()
EnrichedCellSampleSplitting.model_rebuild()
CellBarcoding.model_rebuild()
CdnaAmplification.model_rebuild()
LibraryConstruction.model_rebuild()
LibraryPooling.model_rebuild()
DissectionRoiPolygon.model_rebuild()
DigitalAsset.model_rebuild()

