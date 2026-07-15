import api from "./api";

export async function translateText(
  text,
  source,
  target
) {

  const response =
    await api.post(
      "/translate",
      {
        text,
        source,
        target,
      }
    );

  return response.data;

}