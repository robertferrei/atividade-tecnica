from datetime import datetime

def calculate_termination(remuneration,admission_date,termination_date):
    
  if termination_date <= admission_date:
    raise ValueError("a data de Demissão deve ser posterior à data de admissão")
  
  #ultimo aniversário antes da demissão
  last_birthday = admission_date.replace(year=termination_date.year)
  if last_birthday > termination_date:
    last_birthday = last_birthday.replace(year=termination_date.year - 1)


  #ferias
  vacation_months =  (termination_date.year -last_birthday.year) * 12 + (termination_date.month -last_birthday.month) ##calcula  quantos se passaram desde o último aniversário
  print(f"Meses de férias proporcionais: {vacation_months}")

  vacation = (remuneration / 12) * vacation_months

  # Décimo terceiro proporcional
  if termination_date.day < 15:
    months_13 = termination_date.month - 1
  else:
    months_13 = termination_date.month

  thirteenth = (remuneration / 12) * months_13

  total = vacation + thirteenth

  return {
    "férias_proporcionais": round(vacation, 2),
    "décimo_terceiro_proporcional": round(thirteenth, 2),
    "total_a_receber": round(total, 2)
 }



try:
  remuneration = float(input("Informe o salário mensal (ex: 3500.00): "))
  admission_str = input("Informe a data de admissão (DD/MM/AAAA): ")
  termination_str = input("Informe a data de demissão (DD/MM/AAAA): ")

  admission_date = datetime.strptime(admission_str, "%d/%m/%Y")
  termination_date = datetime.strptime(termination_str, "%d/%m/%Y")

  resultado = calculate_termination(remuneration, admission_date, termination_date)

  print("\n Resultado:")
  print(f"Férias proporcionais: R$ {resultado['férias_proporcionais']:.2f}")
  print(f"Décimo terceiro proporcional: R$ {resultado['décimo_terceiro_proporcional']:.2f}")
  print(f"Total a receber: R$ {resultado['total_a_receber']:.2f}")

except ValueError as e:
  print(f"Erro: {e}")
except Exception:
  print("Erro: Verifique os dados digitados.")