from sympy import symbols, diff, sqrt, sympify

def calculate_error():

    
    formula = input("\nВведите физическую формулу (например: m*g*h): ").strip()
    
    try:

        expr = sympify(formula)
        

        variables = list(expr.free_symbols)
        
        if not variables:
            print("Ошибка: в формуле нет переменных!")
            return
        

        var_names = sorted([str(var) for var in variables])
        print(f"\nНайдены переменные: {', '.join(var_names)}")
        

        values = {}
        errors = {}
        

        print("\nВведите значения и погрешности:")
        for var_name in var_names:
            while True:
                try:
                    val_input = input(f"{var_name} = ").strip()
                    if not val_input:
                        print("Пожалуйста, введите значение!")
                        continue
                    
                    err_input = input(f"Δ{var_name} = ").strip()
                    if not err_input:
                        print("Пожалуйста, введите погрешность!")
                        continue
                    

                    value = float(val_input)
                    error = float(err_input)
                    
                    if error < 0:
                        print("Погрешность не может быть отрицательной!")
                        continue
                    
                    values[var_name] = value
                    errors[var_name] = error
                    break
                    
                except ValueError:
                    print("Ошибка: введите число!")
        

        subs_dict = {symbols(var): val for var, val in values.items()}
        main_value = expr.subs(subs_dict)
        

        error_sum = 0
        
        for var_name in var_names:

            var_symbol = symbols(var_name)
            derivative = diff(expr, var_symbol)
            

            deriv_value = derivative.subs(subs_dict)
            

            error_contribution = (deriv_value * errors[var_name]) ** 2
            error_sum += error_contribution
        

        absolute_error = sqrt(error_sum)
        

        if abs(float(main_value)) > 1e-12:  
            relative_error = (absolute_error / abs(main_value)) * 100
        else:
            relative_error = float('inf')
        

        print(f"\n" + "=" * 50)
        print("РЕЗУЛЬТАТЫ РАСЧЕТА:")
        print(f"Формула: {formula}")
        print(f"\nВведенные значения:")
        
        for var_name in var_names:
            print(f"{var_name} = {values[var_name]} ± {errors[var_name]}")
        
        print(f"\nОсновной результат:")
        print(f"Значение = {float(main_value):.8g}")
        print(f"Абсолютная погрешность = {float(absolute_error):.8g}")
        
        if relative_error != float('inf'):
            print(f"Относительная погрешность = {float(relative_error):.6f}%")
        else:
            print(f"Относительная погрешность = ∞ (значение слишком близко к нулю)")
        
        print(f"\nФинальный ответ:")
        print(f"{float(main_value):.6g} ± {float(absolute_error):.6g}")
        
        if relative_error != float('inf'):
            print(f"ε = {float(relative_error):.4f}%")
        
        # Дополнительно: интервал значений
        lower_bound = float(main_value - absolute_error)
        upper_bound = float(main_value + absolute_error)
        print(f"\nИнтервал значений: [{lower_bound:.6g}, {upper_bound:.6g}]")
        
    except Exception as e:
        print(f"\nОШИБКА: {e}")
        print("Проверьте правильность введенной формулы!")

def main():

    print("Используйте: + - * / ** для степени, sin, cos, exp, log, sqrt, pi")

    print("=" * 60)
    
    while True:
        calculate_error()


while True:
    main()