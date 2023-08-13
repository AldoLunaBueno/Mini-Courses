# Speech to Text <!-- omit in toc -->

## Teoría

Spech-to-Text es una API que usa la tecnología de inteligencia artificial de Google.

Ejemplo de solicitud JSON a la API:

```json
{
    "config": {
        "encoding": "LINEAR16",
        "sampleRateHertz": 16000,
        "languageCode": "en-US",
    },
    "audio": {
        "uri": "gs://bucket-name/path_to_audio_file"
    }
}
```
- La tasa de muestreo óptima es de 16 kHz.
- Solo se admiten tasas de muestreo entre 8 y 48 kHz.

![](sources/2023-08-10-14-03-22.png)

No tenemos una cuenta de servicio.

![](sources/2023-08-10-14-32-37.png)

Para crear una cuenta de servicio, primero habilitamos la API IAM (Identity and Access Management).

![](sources/2023-08-10-17-51-36.png)

![](sources/2023-08-10-18-45-49.png)