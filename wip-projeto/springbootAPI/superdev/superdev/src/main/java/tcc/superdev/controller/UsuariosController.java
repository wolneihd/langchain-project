package tcc.superdev.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import tcc.superdev.model.Usuario;
import tcc.superdev.service.UsuariosService;

import java.util.List;

@RestController
@RequestMapping("/dados")
public class UsuariosController {
    
    @Autowired
    private UsuariosService usuariosService;

    @GetMapping
    public List<Usuario> getUsuarios() {
        return usuariosService.getAllUsuariosWithMessages();
    }
}
