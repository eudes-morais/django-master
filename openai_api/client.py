import openai

def get_car_ai_desc(model, brand_id, year):
    # openai.organization = "org-jA7nO9WSCzH8iLdtGvYpyQQG"
    prompt = ''''
        Me mostre uma descrição de venda para o carro {} {} {} em apenas 200 caracteres.
        Fale coisas específicas deste modelo.
        '''
    openai.api_key = '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'
    prompt = prompt.format(brand_id, model, year)
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=1000,
    )
    print(response)
    return response['choices'][0]['text']
