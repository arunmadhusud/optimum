#  Copyright 2023 The HuggingFace Team. All rights reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

SEQLEN_KEYS_TRANFORMERS = ["max_position_embeddings", "seq_length", "n_positions"]
BLOCK_PATTERNS = [
    "transformer.h",
    "model.decoder.layers",
    "gpt_neox.layers",
    "model.layers",
    "model.language_model.layers",
    # modules loaded by AutoModel vs AutoModelForCausalLM have different prefixes
    "h",
    "decoder.layers",
    "layers",
]

GPTQ_CONFIG = "quantize_config.json"
