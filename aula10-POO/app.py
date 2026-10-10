from aluno import Aluno
from disciplina import Disciplina

# criar / instanciar 1 aluno
aluno1 = Aluno("João", "123456", "Ciência da Computação")
# print(aluno1.disciplinas)

dsa = Disciplina("Data Strucutre", "Álvaro")
cs = Disciplina("Computer Science", "Lucas")
# print(cs.professor)
# cs.exibir_infos()

# MATRICULAR o aluno nas disciplinas
aluno1.matricular(dsa)
aluno1.matricular(cs)
# print(aluno1.disciplinas[1].professor)
# print(aluno1.notas_por_disciplina)

aluno1.adicionar_nota(dsa, 10)
aluno1.adicionar_nota(dsa, 8)
aluno1.adicionar_nota(cs, 5)
aluno1.adicionar_nota(cs, 3)
print(aluno1.notas_por_disciplina)

print(aluno1.calcular_media_d(cs))