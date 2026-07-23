history = []


def add_translation(
    source,
    target,
    direction,
):

    history.append({

        "source": source,

        "translation": target,

        "direction": direction,

    })


def get_history():

    return history[-50:]