from django.shortcuts import render
from . models  import*

def consulta(request):
    consultas = {
         'consultas':Livro.objects.all()
        }

    return render(request,'consulta/consulta.html',consultas)

def autor(request):
    autores = {
         'autores':Autor.objects.all()
        }

    return render(request,'autor/autor.html',autores)

def editora(request):
    editoras = {
         'editoras':Editora.objects.all()
        }

    return render(request,'editora/editora.html',editoras)

def genero(request):
    generos = {
         'generos':Genero.objects.all()
        }

    return render(request,'genero/genero.html',generos)

def leitor(request):
    leitores = {
         'leitores':Leitor.objects.all()
        }

    return render(request,'leitor/leitor.html',leitores)

def cidade(request):
    cidades = {
         'cidades':Cidade.objects.all()
        }

    return render(request,'cidade/cidade.html',cidades)

def emprestimo(request):
    emprestimos = {
         'emprestimos':Emprestimo.objects.all()
        }

    return render(request,'emprestimo/emprestimo.html',emprestimos)

def reserva(request):
     if request.POST:
        nova_reserva= Emprestimo()
        nova_reserva.data_emprestimo = request.POST.get('data')
        nova_reserva.data_devolucao = request.POST.get('data2')
        try:
            leitor = Leitor.objects.get(pk=request.POST.get('leitor'))
            livro = Livro.objects.get(pk=request.POST.get('livro'))
            nova_reserva.leitor = leitor
            nova_reserva.livro = livro
            nova_reserva.save() 
        except Leitor.DoesNotExist:
                print("Leitor não encontrado")
        except Livro.DoesNotExist:
                print("Livro não encontrado")
        except Exception as e:
                print("Erro de integridade:", e)
     reservas = {
         'leitor':Leitor.objects.all(),
         'livro':Livro.objects.all(),
        }
        
     return render(request,'reserva/reserva.html',reservas)
   
   

