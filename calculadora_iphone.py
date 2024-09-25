import flet as ft 
def main(page: ft.page):
    page.bgcolor=ft.colors.BLACK
    page.window_resizable=False
    page.window_width=280
    page.window_height=400
    page.title='calculadora iphone'.upper()
    page.window_always_on_top = True
    
    def calculate(operador,value_at):
        try:
            value = eval(value_at)
            if operador == '%':
                value/=100
            elif operador == "§":
                value= -value
            return value
        except:
            return 'error'
    def select(e):
        value_at=result.value if result.value not in ('0','error') else ''
        value=e.control.content.value
        if value.isdigit():
            value=value_at+value
        elif value == 'AC':
            value='0'
        else:
            if value_at and value_at[-1] in ('/','*','+','-','.'):
                value_at=value_at[:-1]
            value=value_at+value
            if value[-1] in ('=','%','§'):
                value=calculate(value[-1],value_at=value_at)
        result.value=value
        result.update()
    botoes=[
        {'operador':'AC','fonte':ft.colors.BLACK,'fundo':ft.colors.BLUE_GREY_100},
        {'operador':'§','fonte':ft.colors.BLACK,'fundo':ft.colors.BLUE_GREY_100},
        {'operador':'%','fonte':ft.colors.BLACK,'fundo':ft.colors.BLUE_GREY_100},
        {'operador':'/','fonte':ft.colors.WHITE,'fundo':ft.colors.AMBER},
        {'operador':'7','fonte':ft.colors.WHITE,'fundo':ft.colors.WHITE24},
        {'operador':'8','fonte':ft.colors.WHITE,'fundo':ft.colors.WHITE24},
        {'operador':'9','fonte':ft.colors.WHITE,'fundo':ft.colors.WHITE24},
        {'operador':'*','fonte':ft.colors.WHITE,'fundo':ft.colors.AMBER},
        {'operador':'4','fonte':ft.colors.WHITE,'fundo':ft.colors.WHITE24},
        {'operador':'5','fonte':ft.colors.WHITE,'fundo':ft.colors.WHITE24},
        {'operador':'6','fonte':ft.colors.WHITE,'fundo':ft.colors.WHITE24},
        {'operador':'-','fonte':ft.colors.WHITE,'fundo':ft.colors.AMBER},
        {'operador':'1','fonte':ft.colors.WHITE,'fundo':ft.colors.WHITE24},
        {'operador':'2','fonte':ft.colors.WHITE,'fundo':ft.colors.WHITE24},
        {'operador':'3','fonte':ft.colors.WHITE,'fundo':ft.colors.WHITE24},
        {'operador':'+','fonte':ft.colors.WHITE,'fundo':ft.colors.AMBER},
        {'operador':'0','fonte':ft.colors.WHITE,'fundo':ft.colors.WHITE24},
        {'operador':'.','fonte':ft.colors.WHITE,'fundo':ft.colors.WHITE24},
        {'operador':'=','fonte':ft.colors.WHITE,'fundo':ft.colors.AMBER},
    ]
    result=ft.Text(value='0',color=ft.colors.WHITE,size=20)
    btn=[ft.Container(
        content=ft.Text(
            value=btn['operador'],
            color=btn['fonte'],),
        width=50,
        height=50,
        bgcolor=btn['fundo'],
        border_radius=ft.border_radius.all(100),
        alignment=ft.alignment.center,
        on_click=select,
    )for btn in botoes]
    keybord=ft.Row(
        width=280,
        wrap=True,
        controls=btn,
        alignment='end',
    )
    layout=ft.Row(
        width=280,
        alignment='end',
        controls=[
            result,
            
        ]
    )
    page.add(layout,keybord)
    
if __name__ == '__main__':
    ft.app(target=main)