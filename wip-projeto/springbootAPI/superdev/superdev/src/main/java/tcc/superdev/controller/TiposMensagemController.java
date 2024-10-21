package tcc.superdev.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import tcc.superdev.model.TiposMensagem;
import tcc.superdev.service.TiposMensagemService;

import java.util.List;

@RestController
public class TiposMensagemController {
 
    @Autowired
    private TiposMensagemService tiposMensagemService;

    @GetMapping("/tipos-mensagem")
    public List<TiposMensagem> getTiposMensagem() {
        return tiposMensagemService.getAllTiposMensagem();
    }
    
}
