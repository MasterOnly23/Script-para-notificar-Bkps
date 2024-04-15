from check_folders_bkp import check_folder_update
from send_mail import send_email
import time

def check_all_folders():
    # ID de la carpeta "Destacados" en Google Drive
    starred_folder_id = "ID_DE_LA_CARPETA_DESTACADOS"

    # Lista de IDs de las carpetas dentro de "Destacados"
    folder_ids = [
    "1--jgGG_wIcEoqvxZHrY_Tbog6kLWrS1w",
    "1-3VPVix6G1Eo1ckquBgnHqobiOEQQ5XL",
    "1-0xDKZVV7sM8I1uJkPy4GjYx2TIeCvqH",
    "1--mAxPhkpTuP6KjsJvRggTKQ8b007CYp",
    "1-7lkuojvLtInRsvdd1BsOlJ4kFvQXS7O",
    "1-8zidTIocwZIkD8VoR9ZQm9UXRq-yUiL",
    "1--G7L-b5VwzhGRHP8tXMwoqza4SzI9Ij",
    "1-0XTNR2GOgAU_SgbR7lEj1JoFgv79STi",
    "1-1lyMld1pC9tS-QFkanTso3TVxsq9KD7",
    "1--b3fD7PkMM2D6me8G4foQICWhBGI6vE",
    "1-6T_GO40ak7v4i7qp1_lbuNZb1f5baSd",
    "1-8pcMuXdj3uiwAbDhGynFvrw8YQ3wvkS",
    "1-2RAsEtpDw_ZhKGkFh7GDjoesCKMIa-0",
    "1-2NkOm3bvmwx54Msgv1LgBDKjV1zb7Ne",
    "1--VwjWXeh_NzYwb31Wr2Jk-DdtiE7o_a",
    "1-0giFsA7b0euZcsVpZIthqUXBCDxHg6I",
    "1-2I7tOPRIirvXCM-ZmIkosWcKM-bvmmD",
    "1-HqdoAkPOvqSzbtwgAfAw9dTBH3YLPrM",
    "1-5uQOymysXABotHpW_YF24WHiOVpbmgj",
    "1-5of6qw0DVACELwNvnef1iKYsBwj3_Qa",
    "1-2-Y79r8NZKmFPEtXqZg-Vf7H4xWUqTy",
    "1-07DwGcg3vHCAbUFoH7odfmRq9d5I67x",
    "1-1d5BfM-uykhdBaOFYuplTRoz7pbwyQF",
    "1-4Pwf358KBptZ2__PAGY8bp-hBaha6C_",
    "1-47ZUuONC4F3EJy2hcG7K7mVIdf0WjGN",
    "1-6SBQDOHD1MG9yQlyMe7C-J3DkptG1t-",
    "1-1NDwTsAZvq2gLIKcnz4vHKYXAqcRUB7",
    "1--w5wrGKpf4Mg1dDz8I4a-gaJvZXoPO8",
    "1-1_FGt73e-CGO58flxXSrJUcJu0P2Scb",
    "1-LBT-PLy8cI4UHRFPj089j3-bTN1jjBa",
    "1-4ejzMyNjx-cfiMvK3uPvIKDYOQ8NhrX",
    "1-3uStr8V6d87b2gtZ1fUrxA5PlwJIIm5",
    "1-4qNyr__eo5yz9zsnX8nH1yj7HHGJUNo",
    "1-0tQ20lU6q4RO3Nx_QixpODZngY7WsT2",
    "1-0BGhDcXrrJzpp735BW7lAGlpzSTZvD8",
    "1-09E1rr84nvMGOh-rPbe6E3tQ4LiJJc_",
    "1-006V5tF6xawvRYAKCba98BxRhxQBsaj",
    "1-0ioLEHsOBDIR7fMNudwlHXvY_OVRjb1",
    "1-1GLj69FJrl247CbkZl2QQZql5uI_r4Q",
    "1-8TbUTLm_uRVx-C3PQy00td77cWg-eaq",
    "1-1h3qFqB_Csrv3JMw0VMVpw6a-WnqM_m",
    "1--KWOcdKI6xGagkD98jhDerXKiZoFSfo",
    "1--nBDHriTnXDfx7-fHM4XNHBkm_DlFAV",
    "1--SFVcET6B8N9Bfxud1mixRLOHLOkc0R",
    "10zPnmOMjaUI4Ynk03g83k2WMIzT3W-9x",
    "1-3hhmrVznMEwZXPHZ9NJk7eDMbKfsYKt",
    "1-8_8BDBfxBgzXRva3mqgGAXHWVxc0tuf",
    "1-4VQwiPiQF3A6oZxzFUYkIptZUJrA_XF",
    "1--2YvDY5fiK75sSG2ZinUAkMv4QOr4Hk",
    "1-6NR6sXAcCg40JY377sRZa-QYpWsvVVu",
    "1-0DyAmvkjbQOdFh1b9k3FPtFVQAsFj8w",
]

    messages = []

     # Verificar cada carpeta
    for folder_id in folder_ids:
        updated, message = check_folder_update(folder_id)
        print(message)
        messages.append(message)
        
        # Retardo de 2 segundos entre las verificaciones
        time.sleep(1)

    # Enviar un correo electrónico con los resultados
    if all("La carpeta" in message for message in messages):
        send_email("Ultima actividad de carpetas backups, Todos Subidos", "\n".join(messages))
    else:
        send_email("Actividad drive Bkps", "\n".join(messages))



# Ejecutar la función para verificar todas las carpetas
check_all_folders()