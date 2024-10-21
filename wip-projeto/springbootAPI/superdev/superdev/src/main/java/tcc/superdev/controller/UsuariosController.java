package tcc.superdev.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import tcc.superdev.model.Usuarios;
import tcc.superdev.service.UsuariosService;

import java.util.List;

@RestController
public class UsuariosController {
    
    @Autowired
    private UsuariosService usuariosService;

    @GetMapping("/usuarios")
    public List<Usuarios> getUsuarios() {
        return usuariosService.getAllUsuarios();
    }
}
