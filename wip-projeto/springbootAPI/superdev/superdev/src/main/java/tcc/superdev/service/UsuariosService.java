package tcc.superdev.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import tcc.superdev.model.Usuario;
import tcc.superdev.model.Mensagem;
import tcc.superdev.repository.MensagensRepository;
import tcc.superdev.repository.UsuariosRepository;

import java.util.List;

@Service
public class UsuariosService {
    
    @Autowired
    private UsuariosRepository usuariosRepository;

    @Autowired
    private MensagensRepository mensagensRepository;

    public List<Usuario> getAllUsuariosWithMessages() {
        List<Usuario> usuarios = usuariosRepository.findAll();
        List<Mensagem> mensagens = mensagensRepository.findAll(); // Move a busca para fora do loop

        for (Usuario usuario : usuarios) {
            System.out.println("-- Usuario: " + usuario.getId());
            for (Mensagem mensagem : mensagens) {
                // Verifica se o usuário da mensagem é o mesmo que o usuário atual
                if (mensagem.getUsuario() != null && mensagem.getUsuario().getId() != null && 
                    mensagem.getUsuario().getId().equals(usuario.getId())) {
                    usuario.addMensagem(mensagem);
                    System.out.println("-- Mensagem adicionada para usuário " + usuario.getId());
                } else {
                    System.out.println("-- Mensagem não pertence ao usuário " + usuario.getId());
                }
            }
        }
        return usuarios;
    }
}
