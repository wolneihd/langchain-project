package tcc.superdev.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import tcc.superdev.model.Usuarios;

public interface UsuariosRepository extends JpaRepository<Usuarios, Long> {
}
