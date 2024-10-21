package tcc.superdev.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import tcc.superdev.model.Mensagens;
import tcc.superdev.service.MensagensService;

import java.util.List;

@RestController
public class MensagensController {
    
    @Autowired
    private MensagensService mensagensService;

    @GetMapping("/mensagens")
    public List<Mensagens> getMensagens() {
        return mensagensService.getAllMensagens();
    }
}
