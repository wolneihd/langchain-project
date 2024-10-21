package tcc.superdev.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import tcc.superdev.model.Mensagem;

import java.util.List;

public interface MensagensRepository extends JpaRepository<Mensagem, Integer>{
    //List<Mensagem> findByUsuarioId(Integer usuarioId);
}
