#include <stdio.h>
#include <locale.h>

void menu() {
    printf("\nSeja bem-vindo ao sistema de escolher opções, escolha uma das seguintes opções:\n");
    printf("1. Opção 1, é uma boa escolha.\n");
    printf("2. Opção 2, também é uma boa escolha.\n");
    printf("3. Opção 3, boa escolha também.\n");
    printf("0. Sair do programa\n");
} // Função mostrando todas as opções para o usuário.

void opcao1() {
    printf("Você escolheu a opção 1, boa!\n");
} // Função responsável pela mensagem da opção 1.

void opcao2() {
    printf("Você escolheu a opção 2, boa!\n");
} // Função responsável pela mensagem da opção 2.

void opcao3() {
    printf("Você escolheu a opção 3, boa!\n");
} // Função responsável pela mensagem da opção 3.

void opcaoInvalida() {
    printf("Opção inválida, escolhe uma que dê certo (0, 1, 2 ou 3).\n");
} // Função para avisar quando a opção não existe, caso, ele escolhe alguma nada haver.

int main() {
    setlocale(LC_ALL, ""); // Biblioteca que vai deixar o programa ter acentos.

    int resposta = -1; // Variável para armazenar a resposta do usuário.

    while (resposta != 0) { // O programa só para quando ele digitar 0.
        menu();

        printf("Digite o número da opção desejada: ");
        scanf("%d", &resposta); // Aqui ele lê a resposta e armazena na variável.

        if (resposta == 1) {
            opcao1();
        } else if (resposta == 2) {
            opcao2();
        } else if (resposta == 3) {
            opcao3();
        } else if (resposta == 0) {
            printf("Saindo do programa...\n");
        } else {
            opcaoInvalida();
        }
    }

    return 0;
}