#!/usr/bin/env python3
"""
Gera PDF de resumo completo de Sistemas Operacionais — FATEC Ourinhos
Cobre AA01–AA10 com simulado de prova
"""
import sys
sys.path.insert(0, '.claude/skills/fatec-estudo-pdf/scripts')
from gerar_pdf import gerar_pdf

dados = {
  "topico": "Resumo Completo para Prova",
  "disciplina": "Sistemas Operacionais",
  "data": "Marco 2026",

  "secoes": [

    # ────────────────────────────────────────────────────────────
    # SECAO 1 — Fundamentos de SO
    # ────────────────────────────────────────────────────────────
    {
      "titulo": "1. Fundamentos de Sistemas Operacionais",
      "conteudo": [
        {"tipo": "texto", "body":
          "Um Sistema Operacional (SO) atua em duas dimensoes fundamentais: como "
          "maquina estendida, abstraindo o hardware e oferecendo ao programador "
          "uma interface de alto nivel; e como gerenciador de recursos, "
          "arbitrando o acesso concorrente de processos a CPU, memoria e dispositivos. "
          "Sem o SO, cada programa precisaria controlar diretamente o hardware — "
          "caotico, inseguro e incompativel entre maquinas."},

        {"tipo": "subtitulo", "body": "Modos de Operacao: Kernel vs. Usuario"},
        {"tipo": "texto", "body":
          "Processadores modernos operam em (no minimo) dois modos de privilegio. "
          "No modo kernel (supervisor), o SO executa com acesso irrestrito ao hardware. "
          "No modo usuario, os processos comuns executam com acesso limitado. "
          "A transicao de usuario para kernel ocorre exclusivamente por interrupcao, "
          "excecao ou chamada de sistema (syscall) — nunca diretamente."},

        {"tipo": "diagrama", "body":
          "  Espaco do Usuario         |  Espaco do Kernel\n"
          "  -------------------------+------------------------\n"
          "  Processo A               |  Escalonador\n"
          "  Processo B               |  Gerenciador de Memoria\n"
          "  Processo C               |  Drivers de Dispositivo\n"
          "          |                |         ^\n"
          "          | syscall (trap) |         |\n"
          "          +----------------+>--------+\n"
          "          (modo usuario)       (modo kernel)",
          "legenda": "Figura 1 — Transicao entre modos via syscall (trap)"},

        {"tipo": "subtitulo", "body": "Chamadas de Sistema (Syscalls)"},
        {"tipo": "texto", "body":
          "Syscalls sao a interface controlada entre o espaco do usuario e o kernel. "
          "Quando um processo precisa de um servico privilegiado (abrir arquivo, alocar "
          "memoria, criar processo), ele executa uma instrucao de trap que transfere o "
          "controle para o kernel, que valida e executa a operacao. No Linux, exemplos "
          "comuns incluem: read(), write(), fork(), exec(), mmap(), exit(). "
          "A tabela de syscalls mapeia cada numero de chamada para o handler correspondente no kernel."},

        {"tipo": "subtitulo", "body": "Tipos e Arquiteturas de SO"},
        {"tipo": "tabela",
         "cabecalho": ["Arquitetura", "Caracteristica", "Exemplo"],
         "linhas": [
           ["Monolitico", "Kernel unico; todos os servicos no mesmo espaco", "Linux, Unix classico"],
           ["Microkernel", "Kernel minimo; servicos em processos de usuario", "MINIX, QNX, Mach"],
           ["Hibrido", "Nucleo microkernel com modulos no kernel por desempenho", "Windows NT, macOS XNU"],
           ["Exokernel", "Kernel expoe hardware diretamente; libOS gerencia abstracoes", "MIT Exokernel"],
         ]},

        {"tipo": "dica", "body":
          "Na prova: monolitico = mais rapido (sem overhead de IPC), microkernel = mais "
          "seguro e modular. Linux usa monolitico com modulos carregaveis (loadable kernel modules)."},
      ]
    },

    # ────────────────────────────────────────────────────────────
    # SECAO 2 — Virtualizacao
    # ────────────────────────────────────────────────────────────
    {
      "titulo": "2. Virtualizacao e Emulacao",
      "conteudo": [
        {"tipo": "texto", "body":
          "Virtualizacao permite que multiplos sistemas operacionais convidados (guests) "
          "executem sobre um unico hardware fisico, cada um acreditando ter acesso "
          "exclusivo ao hardware. O componente que faz isso se chama Hipervisor (ou VMM — "
          "Virtual Machine Monitor). Existem dois tipos fundamentais."},

        {"tipo": "subtitulo", "body": "Hipervisor Tipo 1 (Bare-Metal)"},
        {"tipo": "texto", "body":
          "Executa diretamente sobre o hardware, sem SO hospedeiro. Tem acesso "
          "privilegiado completo ao hardware e menor overhead. Usado em producao e "
          "data centers. Exemplos: VMware ESXi, Microsoft Hyper-V, Xen."},

        {"tipo": "subtitulo", "body": "Hipervisor Tipo 2 (Hosted)"},
        {"tipo": "texto", "body":
          "Executa como processo sobre um SO hospedeiro convencional. Mais facil de "
          "instalar e usar, mas com overhead adicional por passar pelo SO hospedeiro. "
          "Exemplos: VirtualBox, VMware Workstation, QEMU."},

        {"tipo": "diagrama", "body":
          "  Tipo 1 (Bare-Metal)          Tipo 2 (Hosted)\n"
          "  +-----------+----------+     +---------------+\n"
          "  | Guest OS  | Guest OS |     |   Guest OS    |\n"
          "  +-----------+----------+     +---------------+\n"
          "  |    Hipervisor T1     |     | Hipervisor T2 |\n"
          "  +----------------------+     +---------------+\n"
          "  |      Hardware        |     |  SO Hospedeiro|\n"
          "  +----------------------+     +---------------+\n"
          "                               |   Hardware    |\n"
          "                               +---------------+",
          "legenda": "Figura 2 — Hipervisor Tipo 1 vs. Tipo 2"},

        {"tipo": "subtitulo", "body": "Containers vs. Maquinas Virtuais"},
        {"tipo": "tabela",
         "cabecalho": ["Aspecto", "Container (Docker)", "VM Completa"],
         "linhas": [
           ["Isolamento", "Namespace do kernel (parcial)", "Hardware virtualizado (total)"],
           ["Overhead", "Quase zero — compartilha kernel", "Alto — SO completo por VM"],
           ["Boot", "Milissegundos", "Dezenas de segundos"],
           ["Portabilidade", "Imagem de app", "Imagem de SO completo"],
           ["Seguranca", "Menor isolamento", "Maior isolamento"],
         ]},

        {"tipo": "dica", "body":
          "Containers nao sao VMs! Um container compartilha o kernel do host via namespaces "
          "e cgroups. VMs emulam hardware completo e rodam SO proprio. Use VM quando precisar "
          "de isolamento total ou SO diferente; use container para deploy rapido de aplicacoes."},
      ]
    },

    # ────────────────────────────────────────────────────────────
    # SECAO 3 — Processos e Escalonamento
    # ────────────────────────────────────────────────────────────
    {
      "titulo": "3. Processos e Escalonamento",
      "conteudo": [
        {"tipo": "texto", "body":
          "Um processo e um programa em execucao — a unidade basica de atividade gerenciada "
          "pelo SO. E composto por quatro elementos essenciais: (1) conjunto de instrucoes "
          "(o programa), (2) espaco de enderecamento (regiao de memoria), (3) contexto de "
          "hardware (registradores, PC, SP) e (4) contexto de software (descritores de "
          "arquivo abertos, variaveis de ambiente, UID). "
          "O SO mantem um PCB (Process Control Block) para cada processo com todas essas informacoes."},

        {"tipo": "subtitulo", "body": "Estados de um Processo"},
        {"tipo": "diagrama", "body":
          "          fork()\n"
          "            |\n"
          "            v\n"
          "          [NEW]\n"
          "            |\n"
          "    admitido pelo SO\n"
          "            |\n"
          "            v\n"
          "  +------[READY]<---------+\n"
          "  |       ^    preempcao  |\n"
          "  |       |               |\n"
          " escala-  |   despachado  |\n"
          "  mento   +---[RUNNING]---+\n"
          "  (disp.)         |\n"
          "          espera  |  event\n"
          "          I/O ou  |  completo\n"
          "          event   v       ^\n"
          "              [WAITING]---+\n"
          "                  |\n"
          "              exit()\n"
          "                  |\n"
          "                  v\n"
          "            [TERMINATED]",
          "legenda": "Figura 3 — Diagrama de estados de um processo"},

        {"tipo": "subtitulo", "body": "Algoritmos de Escalonamento"},
        {"tipo": "tabela",
         "cabecalho": ["Algoritmo", "Preemptivo?", "Caracteristica", "Problema"],
         "linhas": [
           ["FCFS", "Nao", "Primeiro a chegar, primeiro a ser servido", "Convoy effect: processos curtos bloqueados por longo"],
           ["SJF", "Nao/Sim", "Menor job primeiro — minima espera media", "Requer conhecer tempo de burst (impraticavel em geral)"],
           ["Round-Robin", "Sim", "Cada processo recebe um quantum de CPU", "Quantum pequeno = overhead alto; grande = vira FCFS"],
           ["Prioridade", "Sim/Nao", "CPU vai ao processo de maior prioridade", "Starvation: processos de baixa prioridade nunca executam"],
           ["Multilevel Feedback", "Sim", "Filas de prioridade dinamicas adaptativas", "Mais complexo de implementar"],
         ]},

        {"tipo": "subtitulo", "body": "Round-Robin em Detalhe"},
        {"tipo": "texto", "body":
          "Round-Robin e o algoritmo mais usado em sistemas interativos (Linux usa variante chamada CFS). "
          "Cada processo recebe um quantum (fatia de tempo — tipicamente 10-100ms). Ao esgotar o quantum, "
          "o processo e preemptado e vai para o final da fila READY. Garante fairness: nenhum processo "
          "monopoliza a CPU. Trade-off: quantum muito pequeno gera overhead de troca de contexto; "
          "quantum muito grande degenera em FCFS e aumenta o tempo de resposta medio."},

        {"tipo": "subtitulo", "body": "Starvation (Inanicao)"},
        {"tipo": "texto", "body":
          "Ocorre quando um processo nunca e executado porque processos de maior prioridade continuam "
          "chegando. Solucao classica: aging (envelhecimento) — a prioridade de um processo aumenta "
          "gradativamente com o tempo que ele aguarda na fila, garantindo execucao eventual."},
      ]
    },

    # ────────────────────────────────────────────────────────────
    # SECAO 4 — Threads
    # ────────────────────────────────────────────────────────────
    {
      "titulo": "4. Threads e Modelos de Concorrencia",
      "conteudo": [
        {"tipo": "texto", "body":
          "Thread e a unidade basica de execucao dentro de um processo. Enquanto processos "
          "tem espacos de enderecamento independentes, threads dentro do mesmo processo "
          "compartilham: espaco de enderecamento, descritores de arquivo, variaveis globais e "
          "heap. Cada thread tem seu proprio: contador de programa (PC), pilha de chamadas e "
          "registradores. Isso torna a criacao de thread muito mais barata que a de processo (fork)."},

        {"tipo": "subtitulo", "body": "Processo vs. Thread"},
        {"tipo": "tabela",
         "cabecalho": ["Aspecto", "Processo", "Thread"],
         "linhas": [
           ["Espaco de enderecamento", "Independente (isolado)", "Compartilhado no processo"],
           ["Heap e variaveis globais", "Privados", "Compartilhados"],
           ["Pilha", "Privada", "Privada por thread"],
           ["Custo de criacao", "Alto (fork + copy-on-write)", "Baixo"],
           ["Custo de troca de contexto", "Alto (troca TLB/MMU)", "Baixo (mesma MMU)"],
           ["Comunicacao", "IPC (pipe, socket, shmem)", "Direto via memoria compartilhada"],
           ["Falha isolada?", "Sim (crash nao afeta outros)", "Nao (crash mata o processo todo)"],
         ]},

        {"tipo": "subtitulo", "body": "Modelos de Thread"},
        {"tipo": "texto", "body":
          "Existem tres modelos que descrevem como threads de usuario se mapeiam para threads de kernel:"},
        {"tipo": "lista", "items": [
          "N:1 (many-to-one): N threads de usuario mapeadas para 1 thread de kernel. Troca de contexto rapida (feita em userspace), mas uma syscall bloqueante para TODO o processo. Sem paralelismo real (nao usa multiplos nucleos). Ex: Java Green Threads (legado).",
          "1:1 (one-to-one): Cada thread de usuario tem uma thread de kernel correspondente. Paralelismo real em multicore. Syscall bloqueante afeta apenas a thread. Mais caro de criar/destruir. Ex: pthreads no Linux, Windows threads.",
          "M:N (many-to-many): M threads de usuario mapeadas para N threads de kernel (N <= M). Combina vantagens: pool de kernel threads reusado. Implementacao complexa. Ex: Solaris.",
        ]},

        {"tipo": "subtitulo", "body": "Funcao JOIN"},
        {"tipo": "texto", "body":
          "pthread_join(tid, &retval) bloqueia a thread chamadora ate que a thread tid "
          "termine. Serve para dois fins: (1) sincronizacao — garantir que o resultado de "
          "uma thread esteja pronto antes de continuar; (2) liberacao de recursos — sem "
          "JOIN ou DETACH, os recursos da thread (pilha, bloco de controle) ficam retidos "
          "no kernel mesmo apos a thread encerrar (thread zombie). DETACH configura a thread "
          "para liberar recursos automaticamente ao terminar, sem precisar de JOIN."},

        {"tipo": "codigo", "body":
          "#include <pthread.h>\n"
          "#include <stdio.h>\n\n"
          "void* tarefa(void* arg) {\n"
          "    int id = *(int*)arg;\n"
          "    printf(\"Thread %d executando\\n\", id);\n"
          "    return (void*)(long)id * 2;  // valor de retorno\n"
          "}\n\n"
          "int main(void) {\n"
          "    pthread_t tid;\n"
          "    int id = 42;\n"
          "    pthread_create(&tid, NULL, tarefa, &id);\n\n"
          "    void* retval;\n"
          "    pthread_join(tid, &retval);  // bloqueia ate thread terminar\n"
          "    printf(\"Retorno: %ld\\n\", (long)retval);\n"
          "    return 0;\n"
          "}",
          "legenda": "Codigo 1 — Criacao e JOIN de thread POSIX"},
      ]
    },

    # ────────────────────────────────────────────────────────────
    # SECAO 5 — Sincronizacao
    # ────────────────────────────────────────────────────────────
    {
      "titulo": "5. Sincronizacao e Exclusao Mutua",
      "conteudo": [
        {"tipo": "subtitulo", "body": "Condicao de Corrida (Race Condition)"},
        {"tipo": "texto", "body":
          "Ocorre quando dois ou mais processos/threads acessam e manipulam dados "
          "compartilhados concorrentemente, e o resultado final depende da ordem "
          "especifica de execucao (scheduling). O resultado e imprevisivel e potencialmente "
          "incorreto. Exemplo classico: dois processos incrementando um contador compartilhado."},

        {"tipo": "codigo", "body":
          "// PROBLEMA: race condition no contador\n"
          "int contador = 0;  // variavel compartilhada\n\n"
          "// Thread A:                // Thread B:\n"
          "int tmp = contador;         int tmp = contador;  // ambas lem 0\n"
          "tmp = tmp + 1;              tmp = tmp + 1;       // ambas calculam 1\n"
          "contador = tmp;             contador = tmp;      // ambas escrevem 1\n\n"
          "// Resultado esperado: 2 | Resultado real: 1 (perdeu um incremento!)",
          "legenda": "Codigo 2 — Race condition em contador compartilhado"},

        {"tipo": "subtitulo", "body": "Regiao Critica e Exclusao Mutua"},
        {"tipo": "texto", "body":
          "A regiao critica e o trecho de codigo que acessa recursos compartilhados e "
          "nao pode ser executado por mais de um processo simultaneamente. "
          "Exclusao mutua e a propriedade que garante isso. Quatro condicoes devem "
          "ser satisfeitas por qualquer solucao de exclusao mutua: "
          "(1) Exclusao mutua: so um processo na regiao critica por vez; "
          "(2) Progresso: se nenhum processo esta na RC, quem quer entrar pode entrar; "
          "(3) Espera limitada: um processo nao espera indefinidamente para entrar; "
          "(4) Sem suposicoes sobre velocidade ou numero de CPUs."},

        {"tipo": "subtitulo", "body": "Mecanismos de Sincronizacao"},
        {"tipo": "tabela",
         "cabecalho": ["Mecanismo", "Como funciona", "Uso ideal"],
         "linhas": [
           ["Busy waiting (spinlock)", "Loop ativo verificando flag — desperdicca CPU", "Espera muito curta, multicore"],
           ["Desabilitar interrupcoes", "Impede preempcao — nao funciona em multicore", "SO monousuario, kernel interno"],
           ["Variaveis de lock", "Flag boolean — sofre race condition na propria flag", "Didatico; nao use em producao"],
           ["Algoritmo de Peterson", "Solucao software elegante para 2 processos", "Fundamento teorico"],
           ["Semaforo", "Contador atomico com operacoes P (wait) e V (signal)", "Producao, n processos, contagem"],
           ["Mutex", "Semaforo binario com dono (owner) — so quem travou pode destrar", "Proteger recurso unico"],
           ["Monitor/Condicao", "Abstracao de alto nivel com lock implicito", "Java synchronized, C# lock"],
         ]},

        {"tipo": "subtitulo", "body": "Semaforo vs. Mutex — Diferenca Critica"},
        {"tipo": "texto", "body":
          "Semaforo e um contador inteiro nao-negativo com duas operacoes atomicas: "
          "P (proberen/wait) decrementa — bloqueia se zero; "
          "V (verhogen/signal) incrementa — acorda thread bloqueada se houver. "
          "Pode ser usado para contagem de recursos (ex: 5 licencas disponiveis) ou "
          "para sincronizacao de ordem entre threads. "
          "Mutex (mutual exclusion lock) e especificamente binario (0 ou 1) e tem "
          "o conceito de dono: apenas a thread que adquiriu o mutex pode liberado. "
          "Isso evita o problema de uma thread liberar o lock de outra (bugs sutis)."},

        {"tipo": "codigo", "body":
          "#include <pthread.h>\n"
          "#include <semaphore.h>\n\n"
          "// --- Mutex ---\n"
          "pthread_mutex_t mtx = PTHREAD_MUTEX_INITIALIZER;\n"
          "int contador = 0;\n\n"
          "void* incrementar(void* arg) {\n"
          "    pthread_mutex_lock(&mtx);   // entra na regiao critica\n"
          "    contador++;                  // operacao atomicamente protegida\n"
          "    pthread_mutex_unlock(&mtx); // sai da regiao critica\n"
          "    return NULL;\n"
          "}\n\n"
          "// --- Semaforo para sincronizar ordem ---\n"
          "sem_t sem;\n"
          "// Thread produtor: sem_post(&sem);\n"
          "// Thread consumidor: sem_wait(&sem);  // bloqueia ate produtor sinalizar",
          "legenda": "Codigo 3 — Mutex e semaforo com pthreads"},

        {"tipo": "dica", "body":
          "Regra pratica: use mutex para proteger um recurso unico (exclusao mutua simples). "
          "Use semaforo quando precisar contar recursos (ex: N slots no buffer) ou sincronizar "
          "ordem entre threads (ex: consumidor espera produtor gerar dado)."},
      ]
    },

    # ────────────────────────────────────────────────────────────
    # SECAO 6 — Problemas Classicos IPC
    # ────────────────────────────────────────────────────────────
    {
      "titulo": "6. Problemas Classicos de Concorrencia",
      "conteudo": [
        {"tipo": "subtitulo", "body": "Jantar dos Filosofos"},
        {"tipo": "texto", "body":
          "Cinco filosofos sentam em torno de uma mesa circular. Entre cada par de filosofos "
          "ha exatamente um garfo. Para comer, um filosofo precisa de dois garfos (o da "
          "esquerda e o da direita). O ciclo de cada filosofo: pensar -> pegar garfo esq -> "
          "pegar garfo dir -> comer -> largar garfos. O problema modela alocacao de recursos "
          "com exclusao mutua e e um benchmark classico para solucoes de deadlock."},

        {"tipo": "diagrama", "body":
          "          F0\n"
          "        /    \\\n"
          "      G0      G4\n"
          "      |        |\n"
          "     F4        F1\n"
          "      |        |\n"
          "      G3      G1\n"
          "        \\    /\n"
          "          F3--G2--F2\n\n"
          "  F = Filosofo, G = Garfo (recurso)",
          "legenda": "Figura 4 — Jantar dos Filosofos: 5 filosofos, 5 garfos"},

        {"tipo": "subtitulo", "body": "Como surge o Deadlock no Jantar"},
        {"tipo": "texto", "body":
          "Se todos os filosofos pegarem o garfo esquerdo simultaneamente, cada um tera "
          "um garfo e esperara pelo garfo direito (que esta na mao do vizinho). Resultado: "
          "espera circular — nenhum consegue o segundo garfo, todos ficam bloqueados para "
          "sempre. As quatro condicoes de Coffman estao presentes: exclusao mutua (garfo so "
          "para um), segurar e esperar, nao preempcao, espera circular."},

        {"tipo": "subtitulo", "body": "Solucoes para o Jantar dos Filosofos"},
        {"tipo": "lista", "items": [
          "Assimetria: filosofo de indice par pega garfo esquerdo primeiro; impar pega direito primeiro. Quebra a espera circular.",
          "Limite de filosofos: permitir no maximo 4 filosofos a mesa simultaneamente (semaforo inicializado em 4). Garante que pelo menos um consiga ambos os garfos.",
          "Pegar ambos ou nenhum: verificar disponibilidade dos dois garfos atomicamente antes de pegar qualquer um.",
          "Solucao de Dijkstra com semaforos: cada filosofo eh um processo, cada garfo eh um semaforo binario. Usar semaforo adicional para coordenacao.",
        ]},

        {"tipo": "subtitulo", "body": "Problema dos Leitores e Escritores"},
        {"tipo": "texto", "body":
          "Um banco de dados e acessado por leitores (leitura concorrente e segura) e "
          "escritores (escrita exclusiva — nenhum outro pode acessar). Invariante: "
          "multiplos leitores podem ler simultaneamente, mas um escritor precisa de "
          "acesso exclusivo total. O problema de starvation dos escritores ocorre na "
          "solucao que prioriza leitores: se leitores chegam continuamente, o escritor "
          "nunca consegue acesso. Solucao: quando um escritor sinaliza intencao de "
          "escrever, novos leitores ficam bloqueados — escritor tem prioridade sobre "
          "leitores que chegam apos o pedido de escrita."},

        {"tipo": "subtitulo", "body": "Barbeiro Adormecido"},
        {"tipo": "texto", "body":
          "Barbearia com 1 barbeiro, 1 cadeira de trabalho e N cadeiras de espera. "
          "Se nao ha clientes, o barbeiro dorme. Cliente que chega: (1) se barbeiro "
          "dorme, acorda-o; (2) se ha cadeira de espera livre, senta e aguarda; "
          "(3) se sala cheia, vai embora. Modela o padrao produtor-consumidor com buffer "
          "limitado. A solucao usa semaforos: um para clientes (conta quantos aguardam), "
          "um para barbeiro (conta se barbeiro esta disponivel) e um mutex para proteger "
          "o contador de clientes."},
      ]
    },

    # ────────────────────────────────────────────────────────────
    # SECAO 7 — Deadlocks
    # ────────────────────────────────────────────────────────────
    {
      "titulo": "7. Deadlocks (Impasses)",
      "conteudo": [
        {"tipo": "texto", "body":
          "Um deadlock e uma situacao em que um conjunto de processos ficam bloqueados "
          "permanentemente, cada um esperando por um recurso que esta sendo retido por "
          "outro processo do conjunto. Nenhum progresso e possivel. O termo 'impasse' "
          "em portugues e igualmente usado na literatura brasileira (Tanenbaum)."},

        {"tipo": "subtitulo", "body": "As 4 Condicoes Necessarias de Coffman (1971)"},
        {"tipo": "texto", "body":
          "Para que um deadlock ocorra, TODAS as quatro condicoes abaixo devem estar "
          "presentes simultaneamente. Eliminar qualquer uma previne o deadlock:"},
        {"tipo": "lista", "items": [
          "1. Exclusao Mutua: o recurso so pode ser usado por um processo de cada vez (nao e compartilhavel).",
          "2. Segurar e Esperar (Hold and Wait): um processo que ja possui pelo menos um recurso fica aguardando por outros recursos que estao em posse de outros processos.",
          "3. Nao Preempcao (No Preemption): recursos nao podem ser tomados forcadamente de um processo; so sao liberados voluntariamente por quem os possui.",
          "4. Espera Circular (Circular Wait): existe uma cadeia fechada de processos P0->P1->...->Pn->P0 onde cada Pi espera por um recurso que esta com Pi+1.",
        ]},

        {"tipo": "dica", "body":
          "Mnemonica para as 4 condicoes: EMSeNE-C — Exclusao Mutua, Segurar e Esperar, "
          "Nao preempcao, Espera Circular. Todas necessarias, nenhuma suficiente sozinha."},

        {"tipo": "subtitulo", "body": "As 4 Estrategias de Tratamento"},
        {"tipo": "tabela",
         "cabecalho": ["Estrategia", "Como funciona", "Custo", "Usado em"],
         "linhas": [
           ["Prevencao", "Projetar sistema para negar ao menos uma das 4 condicoes sempre", "Alto (recursos subutilizados)", "Sistemas de seguranca critica"],
           ["Evasao", "Analisar cada pedido e so conceder se estado resultante for seguro (Algoritmo do Banqueiro)", "Medio (precisa declarar max)", "Sistemas com info de max conhecido"],
           ["Deteccao e Recuperacao", "Permitir deadlocks; detectar ciclos no grafo; abortar/reverter processos", "Recuperacao custosa", "BDs com transacoes (rollback)"],
           ["Politica do Avestruz", "Ignorar o problema — muito raro para valer a pena tratar", "Quase zero", "Unix, Windows (na pratica)"],
         ]},

        {"tipo": "subtitulo", "body": "Algoritmo do Banqueiro (Banker's Algorithm)"},
        {"tipo": "texto", "body":
          "Proposto por Dijkstra, o Algoritmo do Banqueiro implementa a estrategia de "
          "evasao. Cada processo declara antecipadamente o numero maximo de recursos "
          "que pode precisar. Quando um processo solicita recursos, o algoritmo simula "
          "a concessao e verifica se o estado resultante e 'seguro' — ou seja, se existe "
          "alguma sequencia de finalizacao em que todos os processos conseguem seus "
          "recursos maximos e terminam. Se o estado for inseguro, a requisicao e negada "
          "e o processo aguarda. Limitacao pratica: processos raramente conhecem seus "
          "maximos de antemao, tornando-o impraticavel em sistemas gerais."},

        {"tipo": "subtitulo", "body": "Prevencao — Negando Cada Condicao"},
        {"tipo": "lista", "items": [
          "Negar Exclusao Mutua: tornar recursos compartilhaveis quando possivel (ex: leitura de arquivo — multiplos leitores). Nem sempre possivel (impressora nao pode ser compartilhada em uso).",
          "Negar Segurar e Esperar: exigir que processos solicitem TODOS os recursos necessarios de uma vez (tudo ou nada). Problema: baixa utilizacao, starvation possivel.",
          "Negar Nao Preempcao: permitir que o SO force a liberacao de recursos. Funciona para recursos cujo estado pode ser salvo/restaurado (CPU, memoria). Nao funciona para impressora.",
          "Negar Espera Circular: impor ordenacao total dos recursos. Todo processo deve solicitar recursos em ordem crescente. Ex: se R1 < R2, so pode pedir R2 depois de pegar R1. Elimina ciclos no grafo.",
        ]},
      ]
    },

  ],  # fim secoes

  # ────────────────────────────────────────────────────────────
  # SIMULADO
  # ────────────────────────────────────────────────────────────
  "simulado": [

    {
      "numero": 1,
      "tipo": "dissertativa",
      "enunciado":
        "Explique a diferenca entre modo kernel e modo usuario em um sistema operacional. "
        "Como e realizada a transicao entre eles? Cite dois exemplos de operacoes que "
        "exigem modo kernel.",
      "gabarito":
        "O SO opera em dois modos de privilegio: modo kernel (supervisor), com acesso irrestrito "
        "ao hardware, e modo usuario, com acesso limitado para proteger o sistema. A transicao "
        "usuario->kernel ocorre por trap (instrucao especial que aciona uma interrupcao de software), "
        "chamada de sistema (syscall) ou interrupcao de hardware — o processador salva o contexto, "
        "muda o bit de modo e salta para o handler do kernel. Retorno: instrucao privilegiada de "
        "retorno de interrupcao (IRET no x86). Exemplos de operacoes que exigem kernel: "
        "acesso a disco (read/write de arquivo) e gerenciamento de memoria (mmap, malloc que chama brk)."
    },

    {
      "numero": 2,
      "tipo": "dissertativa",
      "enunciado":
        "Descreva os cinco estados possiveis de um processo e explique as transicoes entre eles. "
        "Qual e a diferenca entre um processo no estado 'ready' e no estado 'waiting'?",
      "gabarito":
        "Os cinco estados sao: NEW (processo criado, aguardando admissao), READY (pronto para "
        "executar, aguardando CPU), RUNNING (executando na CPU), WAITING (bloqueado aguardando "
        "evento externo como I/O), TERMINATED (encerrado). Transicoes: NEW->READY (admitido); "
        "READY->RUNNING (dispatcher/escalonador escolhe); RUNNING->READY (preempcao por quantum "
        "ou prioridade); RUNNING->WAITING (solicita I/O ou evento); WAITING->READY (evento "
        "concluido, interrupcao); RUNNING->TERMINATED (exit()). "
        "Diferenca Ready vs. Waiting: processo READY tem todos os recursos menos a CPU — pode "
        "executar imediatamente se escalonado. Processo WAITING nao pode executar mesmo que "
        "receba a CPU — esta bloqueado aguardando evento externo (conclusao de I/O, sinal, etc.)."
    },

    {
      "numero": 3,
      "tipo": "multipla",
      "enunciado":
        "Sobre o escalonamento Round-Robin, qual das afirmativas e CORRETA?\n\n"
        "a) Round-Robin e nao-preemptivo — o processo executa ate terminar voluntariamente.\n"
        "b) Um quantum muito grande melhora o tempo de resposta para processos interativos.\n"
        "c) Cada processo recebe uma fatia de tempo (quantum) e, ao esgota-la, vai para o "
        "final da fila READY.\n"
        "d) Round-Robin nao garante fairness porque processos de alta prioridade sempre "
        "ficam em execucao.\n"
        "e) O algoritmo do Banqueiro e uma variante do Round-Robin para multiplos nucleos.",
      "gabarito":
        "Alternativa CORRETA: c. Round-Robin e preemptivo — quando o quantum expira, o processo "
        "e forcado a liberar a CPU e volta para o final da fila READY. a) ERRADA: e preemptivo. "
        "b) ERRADA: quantum grande piora tempo de resposta (degenera em FCFS). "
        "d) ERRADA: RR puro nao considera prioridade — todos recebem o mesmo quantum. "
        "e) ERRADA: Algoritmo do Banqueiro e estrategia de evasao de deadlock, nao tem relacao com RR."
    },

    {
      "numero": 4,
      "tipo": "dissertativa",
      "enunciado":
        "Explique o que e uma condicao de corrida (race condition) e como o uso de mutex "
        "a resolve. Por que simplesmente usar uma variavel de flag booleana compartilhada "
        "nao resolve o problema?",
      "gabarito":
        "Race condition ocorre quando dois ou mais processos/threads acessam dados compartilhados "
        "concorrentemente e o resultado final depende da ordem de execucao imposta pelo escalonador "
        "— nao-deterministico e potencialmente incorreto. O mutex resolve porque lock e unlock sao "
        "operacoes atomicas garantidas pelo hardware (instrucao test-and-set ou similar): so uma "
        "thread consegue adquirir o mutex; as demais ficam bloqueadas (nao desperdicando CPU em "
        "busy waiting, dependendo da implementacao). Uma variavel flag booleana simples nao funciona "
        "porque a propria leitura e escrita da flag nao e atomica — duas threads podem ler flag=0 "
        "simultaneamente, ambas decidirem que podem entrar, e ambas entrarem na regiao critica "
        "(o mesmo race condition que tentavamos evitar)."
    },

    {
      "numero": 5,
      "tipo": "dissertativa",
      "enunciado":
        "Explique a diferenca entre processo e thread quanto ao espaco de enderecamento, "
        "recursos compartilhados e custo de criacao. Em que situacao voce escolheria "
        "threads em vez de processos para paralelizar uma tarefa?",
      "gabarito":
        "Processo: espaco de enderecamento proprio e isolado, recursos privados (heap, pilha, "
        "descritores de arquivo), criacao cara (fork copia tabela de paginas, mesmo com "
        "copy-on-write). Thread: espaco de enderecamento COMPARTILHADO dentro do processo, "
        "compartilha heap, variaveis globais e descritores — cada thread tem apenas pilha e "
        "registradores proprios, criacao muito mais barata. Escolher thread quando: "
        "(1) as tarefas precisam compartilhar dados em alta velocidade (sem overhead de IPC); "
        "(2) a tarefa e paralelizavel com dados compartilhados (ex: processar partes de um "
        "vetor); (3) o overhead de fork seria proibitivo (servidores web com muitas conexoes). "
        "Escolher processo quando: isolamento de falhas e critico (crash de uma instancia nao "
        "afeta as outras)."
    },

    {
      "numero": 6,
      "tipo": "dissertativa",
      "enunciado":
        "No problema do Jantar dos Filosofos com 5 filosofos, descreva exatamente como "
        "o deadlock pode ocorrer. Quais das quatro condicoes de Coffman estao presentes? "
        "Apresente uma solucao que quebre o deadlock.",
      "gabarito":
        "Deadlock surge quando todos os 5 filosofos simultaneamente pegam o garfo a esquerda: "
        "cada um tem 1 garfo e espera pelo garfo direito (que esta com o vizinho) — espera "
        "circular formada. Condicoes de Coffman presentes: (1) Exclusao Mutua: garfo so pode "
        "ser usado por um filosofo; (2) Segurar e Esperar: cada filosofo segura o garfo esquerdo "
        "e espera o direito; (3) Nao Preempcao: nenhum garfo pode ser tomado a forca; "
        "(4) Espera Circular: F0 espera garfo de F1, F1 espera de F2, ..., F4 espera de F0. "
        "Solucao por assimetria: filosofos de indice par pegam garfo esquerdo primeiro, impares "
        "pegam direito primeiro. Isso quebra a espera circular — pelo menos um filosofo consegue "
        "ambos os garfos e come, liberando-os depois."
    },

    {
      "numero": 7,
      "tipo": "multipla",
      "enunciado":
        "Quais das afirmativas sobre deadlock estao CORRETAS?\n\n"
        "I.  Para ocorrer deadlock, as 4 condicoes de Coffman devem estar presentes simultaneamente.\n"
        "II. A Politica do Avestruz consiste em detectar deadlocks e matar o processo mais antigo.\n"
        "III. O Algoritmo do Banqueiro e uma estrategia de evasao que requer que processos "
        "declarem seus recursos maximos antecipadamente.\n"
        "IV. Negar a condicao de Espera Circular pode ser feito impondo uma ordenacao total "
        "dos recursos e exigindo que processos os solicitem em ordem crescente.\n\n"
        "a) Apenas I e II\nb) Apenas I e III\nc) I, III e IV\nd) II, III e IV\ne) Todas",
      "gabarito":
        "Alternativa CORRETA: c (I, III e IV). "
        "I — CORRETA: as 4 condicoes de Coffman sao necessarias simultaneamente para deadlock. "
        "II — ERRADA: Politica do Avestruz IGNORA o problema (finge que nao existe), nao detecta nem mata processos. "
        "III — CORRETA: Banker's Algorithm requer declaracao antecipada do maximo de recursos por processo. "
        "IV — CORRETA: ordenacao total dos recursos quebra a espera circular eliminando ciclos no grafo de alocacao."
    },

    {
      "numero": 8,
      "tipo": "dissertativa",
      "enunciado":
        "Compare os modelos de thread N:1 e 1:1 quanto a: (a) paralelismo real em sistemas "
        "multicore, (b) comportamento quando uma thread realiza uma syscall bloqueante, e "
        "(c) custo de criacao e troca de contexto. Qual modelo e mais comum nos SOs modernos?",
      "gabarito":
        "(a) Paralelismo: no modelo N:1, todas as N threads de usuario mapeiam para 1 thread "
        "de kernel — o SO ve apenas 1 thread e escalona ela em 1 nucleo; nao ha paralelismo real "
        "mesmo em multicore. No 1:1, cada thread de usuario tem uma thread de kernel, o SO pode "
        "escalonar threads diferentes em nucleos diferentes — paralelismo real. "
        "(b) Syscall bloqueante: no N:1, se uma thread faz read() bloqueante, TODA a thread de "
        "kernel bloqueia, parando TODAS as N threads de usuario do processo. No 1:1, apenas a "
        "thread que fez a syscall bloqueia; as demais continuam executando. "
        "(c) Custo: no N:1, criar/trocar threads e barato (feito em userspace pelo runtime). "
        "No 1:1, cada thread requer syscall ao kernel para criar e troca de contexto passa pelo kernel. "
        "Modelo moderno: 1:1 e o mais usado (Linux pthreads, Windows threads) pois o ganho de "
        "paralelismo justifica o custo adicional de criacao em hardware multicore."
    },

    {
      "numero": 9,
      "tipo": "multipla",
      "enunciado":
        "Sobre virtualizacao, qual afirmativa e CORRETA?\n\n"
        "a) Um hipervisor Tipo 2 executa diretamente sobre o hardware sem SO hospedeiro.\n"
        "b) Containers Docker fornecem maior isolamento que VMs porque cada container tem "
        "seu proprio kernel.\n"
        "c) Um hipervisor Tipo 1 (bare-metal) tem menor overhead que o Tipo 2 porque acessa "
        "o hardware diretamente, sem intermediario.\n"
        "d) Paravirtualizacao exige que o SO convidado seja identicome ao hospedeiro.\n"
        "e) VirtualBox e um exemplo de hipervisor Tipo 1.",
      "gabarito":
        "Alternativa CORRETA: c. Tipo 1 executa diretamente sobre o hardware, sem SO hospedeiro "
        "intermediando — logo, menor latencia e maior desempenho. "
        "a) ERRADA: Tipo 2 executa SOBRE um SO hospedeiro (ex: VirtualBox roda no Windows). "
        "b) ERRADA: containers compartilham o kernel do host via namespaces — menor isolamento. "
        "VMs tem kernel proprio e maior isolamento. "
        "d) ERRADA: paravirtualizacao exige modificacao do SO convidado para usar hypercalls, mas "
        "nao exige que seja identico ao hospedeiro. "
        "e) ERRADA: VirtualBox e Tipo 2 (hosted). Tipo 1: VMware ESXi, Hyper-V, Xen."
    },

    {
      "numero": 10,
      "tipo": "dissertativa",
      "enunciado":
        "Liste as quatro estrategias para lidar com deadlocks e explique brevemente "
        "como cada uma funciona. Qual delas e adotada pelo Linux e Windows na pratica? Por que?",
      "gabarito":
        "(1) Prevencao: projeta o sistema para garantir que ao menos uma das 4 condicoes de "
        "Coffman nunca ocorra. Ex: exigir que processos solicitem todos os recursos de uma vez "
        "(nega Segurar e Esperar). Restricao estrutural — recursos ficam subutilizados. "
        "(2) Evasao: antes de conceder recursos, analisa se o estado resultante e seguro. "
        "Algoritmo do Banqueiro e o exemplo classico. Exige conhecimento previo dos maximos. "
        "(3) Deteccao e Recuperacao: permite que deadlocks ocorram; periodicamente executa "
        "algoritmo de deteccao de ciclo no grafo de recursos; ao detectar, abort ou rollback "
        "processos envolvidos. Caro em termos de overhead de recuperacao. "
        "(4) Politica do Avestruz: ignora o problema completamente — assume que deadlocks sao "
        "raros demais para justificar o custo de tratamento. "
        "Linux e Windows adotam a Politica do Avestruz na pratica: deadlocks sao suficientemente "
        "raros em aplicacoes comuns e o overhead de prevencao/deteccao seria continuo e custoso "
        "para todos os usuarios, mesmo os que jamais encontrariam um deadlock."
    },

  ]  # fim simulado
}  # fim dados


if __name__ == "__main__":
    caminho = gerar_pdf(dados, "sistemas-operacionais/resumo-prova-so.pdf")
    print(f"PDF gerado: {caminho}")
