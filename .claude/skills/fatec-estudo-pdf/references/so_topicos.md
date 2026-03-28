# Referência — Sistemas Operacionais (FATEC Ourinhos)

Livro base: *Sistemas Operacionais Modernos* — Andrew S. Tanenbaum, 4.ª edição

## Tópicos cobertos (AA01–AA10)

| AA   | Tópico                                   | Conceitos-chave                                                      |
|------|------------------------------------------|----------------------------------------------------------------------|
| AA01 | Fundamentos de SO / Instalação           | Tipos de SO, história, kernel vs. userspace, monolítico vs. microkernel |
| AA02 | Mainframes e supercomputadores           | Arquiteturas de hardware, NUMA, SMP, clusters                        |
| AA03 | Chamadas de sistema (syscalls)           | Trap, modo kernel vs. usuário, tabela de syscalls, POSIX             |
| AA04 | Virtualização e emulação                 | Hipervisor tipo 1 e 2, paravirtualização, containers vs. VMs         |
| AA05 | CLI / Shell                              | Shell como processo, pipes, redirecionamento, scripts básicos         |
| AA06 | Processos e escalonamento                | PCB, estados (new/ready/running/waiting/terminated), FCFS, SJF, RR  |
| AA07 | Threads e modelos                        | Modelo N:1, 1:1, M:N, pthreads, contexto de thread                  |
| AA08 | Condições de corrida / Exclusão mútua    | Race condition, seção crítica, mutex, semáforo, spinlock             |
| AA09 | Problemas clássicos IPC                  | Jantar dos Filósofos, Leitores-Escritores, Barbeiro Adormecido       |
| AA10 | Deadlocks                                | 4 condições necessárias, detecção, prevenção, esquiva (Banker's Alg) |

## Tópicos prováveis (próximas AAs)

### Gerenciamento de Memória

- **Particionamento fixo vs. variável**, fragmentação interna vs. externa
- **Paginação:** página, frame, tabela de páginas, endereço virtual = (número de página, offset)
- **TLB (Translation Lookaside Buffer):** cache de tradução de endereços
- **Segmentação:** divisão lógica em segmentos (código, pilha, heap)
- **Memória virtual e page fault:** working set, thrashing, algoritmos de substituição (FIFO, LRU, ótimo)

### Sistemas de Arquivos

- Estrutura: superbloco, inode, bloco de dados
- FAT vs. ext4 vs. NTFS
- **Journaling:** garante consistência após falha
- Permissões POSIX: `rwx` para owner/group/other

### Segurança

- Controle de acesso: ACL, capabilities
- Autenticação vs. Autorização
- Buffer overflow (base de exploits clássicos)

## Conceitos que sempre caem nas dissertativas FATEC

1. **Diferença entre processo e thread** — espaço de endereçamento, recursos compartilhados
2. **O que é deadlock?** — As 4 condições de Coffman (mútua exclusão, hold & wait, no preemption, espera circular)
3. **Escalonamento Round-Robin** — quantum, preempção, fairness, tradeoff latência × throughput
4. **Semáforo vs. Mutex** — semáforo é contador, mutex tem dono; quando usar cada um
5. **Jantar dos Filósofos** — problema de deadlock, solução com ordenação de recursos ou semáforo assimétrico
6. **Virtualização Tipo 1 vs. Tipo 2** — exemplos (VMware ESXi vs. VirtualBox), overhead

## Padrões de questão dissertativa

- "Explique o que é uma condição de corrida e como o uso de mutex a resolve."
- "Descreva os estados de um processo e as transições entre eles."
- "Quais são as quatro condições necessárias para ocorrência de deadlock? Como a negação de cada uma pode preveni-lo?"
- "Compare os modelos de thread N:1 e 1:1 quanto a paralelismo real e chamadas de sistema bloqueantes."
- "No Jantar dos Filósofos com 5 filósofos, explique como surge o deadlock e apresente uma solução."
