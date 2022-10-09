from typing import Union

import httpx

base_url = 'https://hackathon.lsp.team/hk'


# функция для генерации кошелька
def gen_wallet() -> (str, str):
    """

    :return: private_key, public_key
    """
    response = httpx.post(f'{base_url}/v1/wallets/new')
    return response.json().get('privateKey'), response.json().get('publicKey')


# функция для проверки статуса транзакции
def get_trx_status(trx_hash: str) -> Union[str, Exception]:
    """

    :param trx_hash:
    :return: status
    """
    try:
        response = httpx.get(f'{base_url}/v1/transfers/status/{trx_hash}')
    except Exception as e:
        return e
    else:
        return response.json().get('status')


# функция для получения информации об нфт
def get_nft_info(token_id: int) -> Union[dict, Exception]:
    """

    :param token_id:
    :return: dict {tokenId: int, uri: str, publicKey: str}
    """
    try:
        response = httpx.get(f'{base_url}/v1/nft/{token_id}')
    except Exception as e:
        return e
    else:
        return response.json()


# функция для отправки matic
def transfer_matic(from_private_key: str, to_public_key: str, amount: float) -> Union[str, Exception]:
    """

    :param from_private_key: sender_private_key
    :param to_public_key: receiver_public_key
    :param amount: amount in matic
    :return: trx_hash
    """
    try:
        payload = {
            "fromPrivateKey": from_private_key,
            "toPublicKey": to_public_key,
            "amount": amount
        }
        response = httpx.post(f'{base_url}/v1/transfers/matic', json=payload)
    except Exception as e:
        return e
    else:
        return response.json().get('transaction')


# функция для отправки ruble
def transfer_ruble(from_private_key: str, to_public_key: str, amount: float) -> Union[str, Exception]:
    """

    :param from_private_key: sender_private_key
    :param to_public_key: receiver_public_key
    :param amount: amount in rubles
    :return: trx_hash
    """
    try:
        payload = {
            "fromPrivateKey": from_private_key,
            "toPublicKey": to_public_key,
            "amount": amount
        }
        response = httpx.post(f'{base_url}/v1/transfers/ruble', json=payload)
    except Exception as e:
        return e
    else:
        return response.json().get('transaction')


# функция для отправки nft
def transfer_nft(from_private_key: str, to_public_key: str, token_id: int) -> Union[str, Exception]:
    """

    :param from_private_key: sender_private_key
    :param to_public_key: receiver_public_key
    :param token_id: nfts id
    :return:
    """
    try:
        payload = {
            "fromPrivateKey": from_private_key,
            "toPublicKey": to_public_key,
            "tokenId": token_id
        }
        response = httpx.post(f'{base_url}/v1/transfers/nft', json=payload)
    except Exception as e:
        return e
    else:
        return response.json().get('transaction_hash')


# функция для получения баланса кошелька
def get_wallet_balance(public_key: str) -> Union[dict, Exception]:
    """

    :param public_key:
    :return: dict {maticAmount: float, coinsAmount: float}
    """
    try:
        response = httpx.get(f'{base_url}/v1/wallets/{public_key}/balance')
    except Exception as e:
        return e
    else:
        return response.json()


# функция для получения баланса nft кошелька
def get_wallet_nft_balance(public_key: str) -> Union[list, Exception]:
    """

    :param public_key:
    :return: list
    [
    {
      "URI": "ipfs://bafybeifesqvvmmtcjlmeso3zaqh56mhttgza2eglw7zwy4ryuyifduy4i/images/star.png",
      "tokens": [5, 3, 4, 6]
    }
    ]
    """
    try:
        response = httpx.get(f'{base_url}/v1/wallets/{public_key}/nft/balance', timeout=15)
    except Exception as e:
        return e
    else:
        return response.json().get('balance')


# функция для генерации nft
def mint_nft(to_public_key: str, amount: int, uri: str) -> Union[str, Exception]:
    """

    :param to_public_key: receiver_public_key
    :param amount: quantity of nfts
    :param uri: url or any other data to work with
    :return: trx_hash
    """
    try:
        payload = {
            "toPublicKey": to_public_key,
            "uri": uri,
            "nftCount": amount
        }
        response = httpx.post(f'{base_url}/v1/nft/generate', json=payload)
    except Exception as e:
        return e
    else:
        return response.json().get('transaction_hash')


# функция для получения сгенерированных nft
def get_mint_status(trx_hash: str) -> Union[dict, Exception]:
    """

    :param trx_hash:
    :return: dict
    {
    "wallet_id": "0x15Cc4abzz27647ec9fE70D892E55586074263dF0",
    "tokens": [5, 3, 4, 6]
    }
    """
    try:
        response = httpx.get(f'{base_url}/v1/nft/generate/{trx_hash}')
    except Exception as e:
        return e
    else:
        return response.json()


# функция для получения транзакций по кошельку
def get_wallet_history(public_key: str, page: int = 0, offset: int = 20, sort='asc') -> Union[list, Exception]:
    """

    :param public_key:
    :param page:
    :param offset:
    :param sort:
    :return: list
    [
    { # nft
      "blockNumber": 0,
      "timeStamp": 0,
      "contractAddress": "string",
      "from": "0x15Cc4abzz27647ec9fE70D892E55586074263dF0",
      "to": "0x15Cc4abzz27647ec9fE70D892E55586074263dF0",
      "tokenId": 158456332942182445758440449393,
      "tokenName": "NFT",
      "tokenSymbol": "NFT",
      "gasUsed": 120026,
      "confirmations": 4920439
    },
    { # transfer
      "blockNumber": 0,
      "timeStamp": 0,
      "contractAddress": "string",
      "from": "0x15Cc4abzz27647ec9fE70D892E55586074263dF0",
      "to": "0x15Cc4abzz27647ec9fE70D892E55586074263dF0",
      "value": 7777090721429512000,
      "tokenName": "Wrapped Matic",
      "tokenSymbol": "WMATIC",
      "gasUsed": 120026,
      "confirmations": 4920439
    }
  ]
    """
    try:
        payload = {
            "page": page,
            "offset": offset,
            "sort": sort
        }
        response = httpx.post(f'{base_url}/v1/wallets/{public_key}/history', json=payload)
    except Exception as e:
        return e
    else:
        return response.json().get('history')


# private_key, public_key = gen_wallet()

# private_key = '30896a066123d16109d9a97e1482fab40c04d37406154308f49e1c50633e444f'
# public_key = '0x7D3D3e00d5ba56220A388aE97B61e5F1Cc39D390'
#
# receiver = '0xE85de2FA515433f7c17314191453a7a2ac2aBEe6'
# receiver_private_key = '13ce2cc871b9a4eb91437f9e126a34d875e2a0a9b8e788f181987b3b6adf673c'
#
# print('Private key:', private_key)
# print('Public key:', public_key)
#
# balance = get_wallet_balance(public_key)
# print(f'{public_key} has {balance.get("maticAmount")} MATIC')
# print(f'{public_key} has {balance.get("coinsAmount")} rubles')
#
# trx_hash = transfer_matic(private_key, receiver, 0.000001)
# print('Transaction hash:', trx_hash)
# status = get_trx_status(trx_hash)
# print('Transaction status:', status)
#
# # trx_hash = '0xb3aaa5ddd47bb146f4bf3fa75357ab0cdf8de7b01febe91ee6330d15b8748207'
# # status = get_trx_status(trx_hash)
# # print('Transaction status:', status)
#
# trx_hash = transfer_ruble(receiver_private_key, public_key, 1)
# print('Transaction hash:', trx_hash)
# status = get_trx_status(trx_hash)
# print('Transaction status:', status)
#
# # trx_hash = mint_nft(
# #     to_public_key=public_key,
# #     amount=3,
# #     uri='https://lh3.googleusercontent.com/tNpcMqMfrcvWjtSkEiAScBP2-1gswh3bgffbz4_yuzlfk7ierfl7upiwqx1rk9gfxufilxkju2p937bahkgzcr8go43ngrhp0iexkg'
# # )
# trx_hash = '0x2418df36da5f5c2a13deb300cf45a8b3919acb2a82b9dffd53dbdf3c4919bbe9'
# print('Mint transaction:', trx_hash)
# mint_status = get_mint_status(trx_hash)
# print('Mint status:', mint_status)
#
# nfts = get_wallet_nft_balance(public_key)
# print(f'{public_key} has {nfts} nfts')
#
# token_id = 357
# nft_info = get_nft_info(token_id)
# print(f'NFT info {nft_info}')
#
# # trx_hash = transfer_nft(private_key, receiver, token_id)
# trx_hash = '0x825e5b4047757ab2a879da207db1b2e501d740e488d34eb1e6b43ac7b599a22c'
# print('NFT transfer transaction:', trx_hash)
#
# status = get_trx_status('0x825e5b4047757ab2a879da207db1b2e501d740e488d34eb1e6b43ac7b599a22c')
# print('NFT transfer status:', status)