using System.Transactions;
using ContainRs.Api.Contracts;

namespace ContainRs.Api.Domain;
/// <summary>
/// Uso do padrão Command encapsula cada operação como um objeto separado.
/// tornando as intenções do sistema mais claras e explícitas, 
/// mantendo os casos de uso bem definidos e independentes, favorecendo a leitura, manutenção e testes. 
/// Contudo, é fundamental saber distinguir as informações que fazem parte do problema (o que deve ser feito),
///  das informações que compõem sua solução (como deve ser feito).
/// </summary>
public class AprovarProposta
{
    public AprovarProposta(Guid idPedido, Guid idProposta)
    {
        IdPedido = idPedido;
        IdProposta = idProposta;
    }
    public Guid IdPedido {get;}
    public Guid IdProposta {get;}
}