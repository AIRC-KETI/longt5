# Copyright 2022 san kim
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import seqio
DEFAULT_SPM_PATH = "gs://tpu-lm-bucket/vocab/ko_en/spiece.model"
DEFAULT_EXTRA_IDS = 100

DEFAULT_VOCAB = seqio.SentencePieceVocabulary(
    DEFAULT_SPM_PATH, DEFAULT_EXTRA_IDS)