from .models import Pessoa
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


# Create your views here.
def home(request):
    context = {}
    """Página que lista todos os produtos, com possibilidade de ordenação"""
    pessoas = Pessoa.objects.all().order_by("nome")
    if request.method == "POST":
        if "deletar" in request.POST:
            id_pessoa = request.POST.get("id_pessoa")
            pessoa = get_object_or_404(Pessoa, id=id_pessoa)
            pessoa.delete()
            return redirect("home")

        if "editar" in request.POST:
            id_pessoa = request.POST.get("id_pessoa")
            pessoa = get_object_or_404(Pessoa, id=id_pessoa)
            nome = request.POST.get("nome")
            try:
                idade = int(request.POST.get("idade"))
            except:
                messages.error(request, "Use um número para idade")
                return redirect("home")
            cpf = request.POST.get("cpf").replace(".", "").replace("-", "")

            pessoa.nome = nome if nome else pessoa.nome
            pessoa.idade = idade if idade else pessoa.idade
            pessoa.cpf = cpf if cpf else pessoa.cpf

            pessoa.save()
            return redirect("home")

        if "add_pessoa" in request.POST:
            nome = request.POST.get("nome")
            try:
                idade = int(request.POST.get("idade"))
            except:
                messages.error(request, "Use um número para idade")
                return redirect("home")
            cpf = request.POST.get("cpf").replace(".", "").replace("-", "")

            campo_falta = []

            campo_falta.append("Nome da Pessoa") if not nome else None
            campo_falta.append("Idade") if not idade else None
            campo_falta.append("CPF") if not cpf else None

            if campo_falta:
                mensagem = "Estão faltando os seguintes campos: " + ", ".join(
                    campo_falta
                )
                messages.error(request, mensagem)
                return redirect("home")

            pessoa = Pessoa.objects.create(
                nome=nome,
                idade=idade,
                cpf=cpf,
            )
            return redirect("home")

    context["pessoas"] = pessoas

    return render(
        request,
        "1_app_crud/home/home.html",
        context,
    )
