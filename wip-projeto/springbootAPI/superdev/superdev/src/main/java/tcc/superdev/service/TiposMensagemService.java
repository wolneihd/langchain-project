package tcc.superdev.service;

import org.springframework.beans.factory.annotation.Autowired;
import tcc.superdev.model.TiposMensagem;
import tcc.superdev.repository.TiposMensagemRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TiposMensagemService {
    
    @Autowired
    private TiposMensagemRepository tiposMensagemRepository;

    public List<TiposMensagem> getAllTiposMensagem() {
        return tiposMensagemRepository.findAll();
    }

}
