package tcc.superdev.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import tcc.superdev.model.Mensagens;

public interface MensagensRepository extends JpaRepository<Mensagens, Long> {
}