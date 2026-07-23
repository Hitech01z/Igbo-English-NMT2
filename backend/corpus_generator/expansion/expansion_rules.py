"""
Controlled sentence expansion rules.

Every English sentence is generated together with its
corresponding Igbo translation.
"""


EXPANSION_RULES = [

    # =====================================================
    # AGRICULTURE
    # =====================================================

    {
        "domain": "agriculture",

        "base_english": "The farmer planted maize.",
        "base_igbo": "Onye ọrụ ugbo kụrụ ọka.",

        "variants": [

            (
                "The farmer planted maize yesterday.",
                "Onye ọrụ ugbo kụrụ ọka ụnyaahụ.",
            ),

            (
                "The farmer planted maize today.",
                "Onye ọrụ ugbo kụrụ ọka taa.",
            ),

            (
                "The farmer will plant maize tomorrow.",
                "Onye ọrụ ugbo ga-akụ ọka echi.",
            ),

        ],
    },


    {
        "domain": "agriculture",

        "base_english": "The farmer harvested maize.",
        "base_igbo": "Onye ọrụ ugbo wetara ọka.",

        "variants": [

            (
                "The farmer harvested maize yesterday.",
                "Onye ọrụ ugbo wetara ọka ụnyaahụ.",
            ),

            (
                "The farmer harvested maize today.",
                "Onye ọrụ ugbo wetara ọka taa.",
            ),

        ],
    },


    {
        "domain": "agriculture",

        "base_english": "The farmer planted yam.",
        "base_igbo": "Onye ọrụ ugbo kụrụ ji.",

        "variants": [

            (
                "The farmer planted yam yesterday.",
                "Onye ọrụ ugbo kụrụ ji ụnyaahụ.",
            ),

            (
                "The farmer planted yam today.",
                "Onye ọrụ ugbo kụrụ ji taa.",
            ),

            (
                "The farmer will plant yam tomorrow.",
                "Onye ọrụ ugbo ga-akụ ji echi.",
            ),

        ],
    },


    {
        "domain": "agriculture",

        "base_english": "The farmer went to the farm.",
        "base_igbo": "Onye ọrụ ugbo gara n'ubi.",

        "variants": [

            (
                "The farmer went to the farm yesterday.",
                "Onye ọrụ ugbo gara n'ubi ụnyaahụ.",
            ),

            (
                "The farmer went to the farm today.",
                "Onye ọrụ ugbo gara n'ubi taa.",
            ),

            (
                "The farmer will go to the farm tomorrow.",
                "Onye ọrụ ugbo ga-aga n'ubi echi.",
            ),

        ],
    },


    {
        "domain": "agriculture",

        "base_english": "The crops are growing well.",
        "base_igbo": "Ihe ọkụkụ na-eto nke ọma.",

        "variants": [

            (
                "The crops are growing well today.",
                "Ihe ọkụkụ na-eto nke ọma taa.",
            ),

            (
                "The crops grew well yesterday.",
                "Ihe ọkụkụ toro nke ọma ụnyaahụ.",
            ),

        ],
    },


    # =====================================================
    # FOOD
    # =====================================================

    {
        "domain": "food",

        "base_english": "Mary ate beans.",
        "base_igbo": "Mary riri agwa.",

        "variants": [

            (
                "Mary ate beans yesterday.",
                "Mary riri agwa ụnyaahụ.",
            ),

            (
                "Mary ate beans today.",
                "Mary riri agwa taa.",
            ),

        ],
    },


    {
        "domain": "food",

        "base_english": "Peter ate rice.",
        "base_igbo": "Peter riri osikapa.",

        "variants": [

            (
                "Peter ate rice yesterday.",
                "Peter riri osikapa ụnyaahụ.",
            ),

            (
                "Peter ate rice today.",
                "Peter riri osikapa taa.",
            ),

        ],
    },


    {
        "domain": "food",

        "base_english": "Grace cooked garri.",
        "base_igbo": "Grace siri garri.",

        "variants": [

            (
                "Grace cooked garri yesterday.",
                "Grace siri garri ụnyaahụ.",
            ),

            (
                "Grace cooked garri today.",
                "Grace siri garri taa.",
            ),

        ],
    },


    {
        "domain": "food",

        "base_english": "Garri tastes good.",
        "base_igbo": "Garri na-atọ ụtọ.",

        "variants": [

            (
                "Garri tastes good today.",
                "Garri na-atọ ụtọ taa.",
            ),

        ],
    },


    # =====================================================
    # BUSINESS
    # =====================================================

    {
        "domain": "business",

        "base_english": "Grace bought yam.",
        "base_igbo": "Grace zụtara ji.",

        "variants": [

            (
                "Grace bought yam yesterday.",
                "Grace zụtara ji ụnyaahụ.",
            ),

            (
                "Grace bought yam today.",
                "Grace zụtara ji taa.",
            ),

        ],
    },


    {
        "domain": "business",

        "base_english": "Chioma sold the phone.",
        "base_igbo": "Chioma rere ekwentị.",

        "variants": [

            (
                "Chioma sold the phone yesterday.",
                "Chioma rere ekwentị ụnyaahụ.",
            ),

            (
                "Chioma sold the phone today.",
                "Chioma rere ekwentị taa.",
            ),

        ],
    },


    {
        "domain": "business",

        "base_english": "The trader visited Kano.",
        "base_igbo": "Onye ahịa gara Kano.",

        "variants": [

            (
                "The trader visited Kano yesterday.",
                "Onye ahịa gara Kano ụnyaahụ.",
            ),

            (
                "The trader visited Kano today.",
                "Onye ahịa gara Kano taa.",
            ),

        ],
    },


    # =====================================================
    # TRANSPORTATION
    # =====================================================

    {
        "domain": "transportation",

        "base_english": "The car arrived early.",
        "base_igbo": "Ụgbọala rutere n'oge.",

        "variants": [

            (
                "The car arrived early yesterday.",
                "Ụgbọala rutere n'oge ụnyaahụ.",
            ),

            (
                "The car arrived early today.",
                "Ụgbọala rutere n'oge taa.",
            ),

        ],
    },


    {
        "domain": "transportation",

        "base_english": "The airport arrived early.",
        "base_igbo": "Ọdụ ụgbọ elu rutere n'oge.",

        "variants": [

            (
                "The airport arrived early yesterday.",
                "Ọdụ ụgbọ elu rutere n'oge ụnyaahụ.",
            ),

        ],
    },


    # =====================================================
    # WEATHER
    # =====================================================

    {
        "domain": "weather",

        "base_english": "Mary likes the storm.",
        "base_igbo": "Mary hụrụ oke ifufe n'anya.",

        "variants": [

            (
                "Mary likes the storm today.",
                "Mary hụrụ oke ifufe n'anya taa.",
            ),

        ],
    },


    {
        "domain": "weather",

        "base_english": "The wind is changing.",
        "base_igbo": "Ifufe na-agbanwe.",

        "variants": [

            (
                "The wind is changing today.",
                "Ifufe na-agbanwe taa.",
            ),

        ],
    },


    # =====================================================
    # HEALTH
    # =====================================================

    {
        "domain": "health",

        "base_english": "The doctor treated diabetes.",
        "base_igbo": "Dọkịta gwọrọ shuga.",

        "variants": [

            (
                "The doctor treated diabetes yesterday.",
                "Dọkịta gwọrọ shuga ụnyaahụ.",
            ),

        ],
    },


    {
        "domain": "health",

        "base_english": "The doctor treated typhoid.",
        "base_igbo": "Dọkịta gwọrọ taịfọd.",

        "variants": [

            (
                "The doctor treated typhoid yesterday.",
                "Dọkịta gwọrọ taịfọd ụnyaahụ.",
            ),

        ],
    },

]