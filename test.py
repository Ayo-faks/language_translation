from os import environ

from google.cloud import translate


def batch_translate_text(
    input_uri="gs://trainayo2020/test.txt",
    output_uri="gs://resultsayo2021/",
    project_id = "mywebsite-325009",
    timeout=180,
):
    """Translates a batch of texts on GCS and stores the result in a GCS location."""

    client = translate.TranslationServiceClient()

    location = "us-central1"
    # Supported file types: https://cloud.google.com/translate/docs/supported-formats
    gcs_source = {"input_uri": input_uri}

    input_configs_element = {
    "gcs_source": gcs_source,
    "mime_type": "text/plain", # Can be "text/plain" or "text/html".
    }
    gcs_destination = {"output_uri_prefix": output_uri}
    output_config = {"gcs_destination": gcs_destination}
    parent = f"projects/{project_id}/locations/{location}"

    # Supported language codes: https://cloud.google.com/translate/docs/languages
    operation = client.batch_translate_text(
    request={
    "parent": parent,
    "source_language_code": "en",
    "target_language_codes": ["yo"], # Up to 10 language codes here.
    "input_configs": [input_configs_element],
    "output_config": output_config,
    }
    )

    print("Waiting for operation to complete...")
    response = operation.result(timeout)

    print("Total Characters: {}".format(response.total_characters))
    print("Translated Characters: {}".format(response.translated_characters))

if __name__ == "__main__":
    batch_translate_text(
    input_uri="gs://trainayo2020/metadata.tsv",
    output_uri="gs://resultsayo2021/",
    project_id = "mywebsite-325009",
    timeout=180)