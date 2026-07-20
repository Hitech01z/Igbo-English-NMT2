import random
import re

from corpus_generator.source_data.names_data import NAMES
from corpus_generator.source_data.occupations_data import OCCUPATIONS
from corpus_generator.source_data.locations_data import LOCATIONS
from corpus_generator.source_data.common_objects import OBJECTS
from corpus_generator.source_data.common_verbs import VERBS
from corpus_generator.source_data.adjectives_data import ADJECTIVES
from corpus_generator.source_data.adverbs_data import ADVERBS
from corpus_generator.source_data.numbers_data import NUMBERS
from corpus_generator.source_data.time_data import TIMES

from corpus_generator.source_data.foods_data import FOODS
from corpus_generator.source_data.crops_data import CROPS
from corpus_generator.source_data.diseases_data import DISEASES
from corpus_generator.source_data.technology_terms import TECHNOLOGY
from corpus_generator.source_data.education_terms import EDUCATION
from corpus_generator.source_data.government_terms import GOVERNMENT
from corpus_generator.source_data.transportation_terms import TRANSPORTATION
from corpus_generator.source_data.weather_terms import WEATHER

from corpus_generator.templates.general_templates import GENERAL_TEMPLATES
from corpus_generator.templates.education_templates import EDUCATION_TEMPLATES
from corpus_generator.templates.health_templates import HEALTH_TEMPLATES
from corpus_generator.templates.agriculture_templates import AGRICULTURE_TEMPLATES
from corpus_generator.templates.business_templates import BUSINESS_TEMPLATES
from corpus_generator.templates.technology_templates import TECHNOLOGY_TEMPLATES
from corpus_generator.templates.government_templates import GOVERNMENT_TEMPLATES
from corpus_generator.templates.transportation_templates import TRANSPORTATION_TEMPLATES
from corpus_generator.templates.food_templates import FOOD_TEMPLATES
from corpus_generator.templates.weather_templates import WEATHER_TEMPLATES


PLACEHOLDER_PATTERN = re.compile(r"\{(.*?)\}")


RESOURCE_MAP = {
    "name": NAMES,
    "person": NAMES,
    "occupation": OCCUPATIONS,
    "location": LOCATIONS,
    "object": OBJECTS,
    "verb": VERBS,
    "adjective": ADJECTIVES,
    "adverb": ADVERBS,
    "number": NUMBERS,
    "time": TIMES,
    "food": FOODS,
    "crop": CROPS,
    "technology": TECHNOLOGY,
    "education": EDUCATION,
    "government": GOVERNMENT,
    "transport": TRANSPORTATION,
    "weather": WEATHER,
    "disease": DISEASES,
}


DOMAINS = {
    "general": GENERAL_TEMPLATES,
    "education": EDUCATION_TEMPLATES,
    "health": HEALTH_TEMPLATES,
    "agriculture": AGRICULTURE_TEMPLATES,
    "business": BUSINESS_TEMPLATES,
    "technology": TECHNOLOGY_TEMPLATES,
    "government": GOVERNMENT_TEMPLATES,
    "transportation": TRANSPORTATION_TEMPLATES,
    "food": FOOD_TEMPLATES,
    "weather": WEATHER_TEMPLATES,
}


def placeholders(text):
    return PLACEHOLDER_PATTERN.findall(text)


def random_value(resource):
    return random.choice(resource)


def build_mapping(template):

    mapping = {}

    english = template["english"]
    igbo = template["igbo"]

    fields = set(
        placeholders(english)
        + placeholders(igbo)
    )

    for field in fields:

        if field not in RESOURCE_MAP:

            raise ValueError(
                f"Unknown placeholder: {field}"
            )

        mapping[field] = random_value(
            RESOURCE_MAP[field]
        )

    return mapping


def render_sentence(
    text,
    language,
    mapping,
):

    values = {}

    for key, value in mapping.items():

        if isinstance(value, dict):

            values[key] = value[language]

        else:

            values[key] = value

    return text.format(**values)


def generate_pair(domain):

    if domain not in DOMAINS:

        raise ValueError(
            f"Unknown domain: {domain}"
        )

    template = random.choice(
        DOMAINS[domain]
    )

    mapping = build_mapping(template)

    english = render_sentence(
        template["english"],
        "english",
        mapping,
    )

    igbo = render_sentence(
        template["igbo"],
        "igbo",
        mapping,
    )

    return {
        "domain": domain,
        "english": english.strip(),
        "igbo": igbo.strip(),
    }


def generate_dataset(
    domain,
    size,
):

    dataset = []

    for _ in range(size):

        dataset.append(
            generate_pair(domain)
        )

    return dataset


def generate_all(
    domains=None,
    size_per_domain=10000,
):

    if domains is None:

        domains = list(
            DOMAINS.keys()
        )

    dataset = []

    for domain in domains:

        print(
            f"Generating {domain}..."
        )

        dataset.extend(
            generate_dataset(
                domain,
                size_per_domain,
            )
        )

    random.shuffle(dataset)

    return dataset


if __name__ == "__main__":

    sample = generate_pair("general")

    print(sample["english"])

    print(sample["igbo"])