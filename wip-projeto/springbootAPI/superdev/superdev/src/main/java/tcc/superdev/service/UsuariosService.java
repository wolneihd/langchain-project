package tcc.superdev.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import tcc.superdev.model.Usuarios;
import tcc.superdev.repository.UsuariosRepository;

import java.util.List;

@Service
public class UsuariosService {
    
    @Autowired
    private UsuariosRepository usuariosRepository;

    public List<Usuarios> getAllUsuarios() {
        return usuariosRepository.findAll();
    }
}
