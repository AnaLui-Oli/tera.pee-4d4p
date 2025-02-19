from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Pacientes, Tarefas, Consultas
from django.contrib import messages
from django.contrib.messages import constants


def cadastrar_pacientes(request):
    
    if request.method == 'GET':
        pacientes = Pacientes.objects.all()

        opcoes = Pacientes.queixa_choices
        for p in pacientes:
            print(p.queixa)
            print(p.get_queixa_display())
        return render(request, 'index.html', {'queixas': opcoes, 'pacientes': pacientes})
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        tel = request.POST.get('telefone')
        queixa = request.POST.get('queixa')
        foto = request.FILES.get('foto')

        if len(nome.strip()) == 0 or not foto:
            messages.add_message(request,constants.ERROR, 'Preencha todos os campos')
            return redirect('pacientes')


        paciente = Pacientes(nome=nome, email=email, tel=tel, foto=foto, queixa=queixa)
        paciente.save()
        messages.add_message(request,constants.SUCCESS, 'Cadastro efetuado com sucesso')

        return redirect('pacientes')

# def deletar_paciente():

#     for i in range(1, 4):
#         paciente = Pacientes.objects.get(id=i)
#         print(paciente)
#     return HttpResponse("hi")

def paciente_infos(request, id):
    pessoa = Pacientes.objects.get(id=id)
    if request.method == "GET":
        tarefas = Tarefas.objects.all()
        consultas = Consultas.objects.filter(paciente=pessoa)
        
        consultas_list = []
        humor_list = []
        for i in consultas:
            consultas_list.append(str(i.data))
            humor_list.append(str(i.humor))

        tupla_grafico = (consultas_list, humor_list)

        ''' versão avançada:
            tuple_grafico = ([str(i.data) for i in consultas], [str(i.humor) for i in consultas])
        '''
    
        return render(request, 'paciente.html', {'paciente': pessoa, 'tarefas':tarefas, 'consultas':consultas, 'infos_grafico': tupla_grafico})
    elif request.method == 'POST':
        humor = request.POST.get('humor')
        registro_geral = request.POST.get('registro_geral')
        video = request.FILES.get('video')
        tarefas = request.POST.getlist('tarefas')

        consulta = Consultas(humor=int(humor), registro_geral=registro_geral, video=video, paciente=pessoa)
        consulta.save()

        for i in tarefas:
            tarefa = Tarefas.objects.get(id=i)
            consulta.tarefas.add(tarefa)
        consulta.save()
        messages.add_message(request,constants.SUCCESS, 'Consulta salva com sucesso')

        return redirect(f'/pacientes/{id}')
        

def atualizar_paciente(request, id):
    pagamento_em_dia = request.POST.get('pagamento_em_dia')
    pessoa = Pacientes.objects.get(id=id)

    if pagamento_em_dia == 'ativo':
        pessoa.pagamento_em_dia = True
    else:
        pessoa.pagamento_em_dia = False

    ''' versão mais avançada:
        status = True if pagamento_em_dia == 'ativo else False
        pessoa.pagamento_em_dia = status
    '''
    pessoa.save()
    return redirect(f"/pacientes/{id}")

def excluir_consulta(request, id):
    consulta = Consultas.objects.get(id=id)
    consulta.delete() 
    paciente_id = consulta.paciente.id
    messages.add_message(request,constants.SUCCESS, 'Consulta excluída com sucesso')
    return redirect(f'/pacientes/{paciente_id}')

def consulta_publica(request, id):
    consulta = Consultas.objects.get(id=id)
    if not consulta.paciente.pagamento_em_dia:
        raise Http404()

    return render(request, 'consulta_publica.html', {'consulta': consulta})

#TODO visualizações (???)
