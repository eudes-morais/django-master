import openai

def get_car_ai_desc(model, brand_id, year):
    # openai.organization = "org-jA7nO9WSCzH8iLdtGvYpyQQG"
    # prompt = ''''
    #     Me mostre uma descrição de venda para o carro {} {} {} em apenas 200 caracteres.
    #     Fale coisas específicas deste modelo.
    #     '''
    # prompt = prompt.format(brand_id, model, year)
    openai.api_key = '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'
    prompt = f'Me mostre uma descrição de venda para o carro {brand_id} {model} {year} em apenas 200 caracteres. Fale coisas específicas deste modelo.'
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=1000,
    )
    print(response)
    return response['choices'][0]['text']
