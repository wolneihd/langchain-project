package tcc.superdev.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import tcc.superdev.model.TiposMensagem;

public interface TiposMensagemRepository extends JpaRepository<TiposMensagem, Integer> {
    
}
