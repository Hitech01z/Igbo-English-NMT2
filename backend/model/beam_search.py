import torch
import torch.nn.functional as F


def beam_search(
    model,
    src,
    beam_size,
    max_length,
    bos_id,
    eos_id,
    device,
):

    model.eval()

    beams = [
        (
            torch.tensor([[bos_id]], device=device),
            0.0,
        )
    ]

    with torch.no_grad():

        for _ in range(max_length):

            candidates = []

            for seq, score in beams:

                if seq[0, -1].item() == eos_id:
                    candidates.append((seq, score))
                    continue

                output = model(src, seq)

                logits = output[:, -1]

                log_probs = F.log_softmax(
                    logits,
                    dim=-1,
                )

                values, indices = torch.topk(
                    log_probs,
                    beam_size,
                )

                for k in range(beam_size):

                    token = indices[0, k].item()

                    new_score = (
                        score +
                        values[0, k].item()
                    )

                    new_seq = torch.cat(
                        [
                            seq,
                            torch.tensor(
                                [[token]],
                                device=device,
                            ),
                        ],
                        dim=1,
                    )

                    candidates.append(
                        (
                            new_seq,
                            new_score,
                        )
                    )

            beams = sorted(
                candidates,
                key=lambda x: x[1],
                reverse=True,
            )[:beam_size]

            if all(
                beam[0][0, -1].item() == eos_id
                for beam in beams
            ):
                break

    return beams[0][0]